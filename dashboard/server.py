#!/usr/bin/env python3
"""Local Dashboard Server with Agent Execution Bridge.

Serves the Job Intelligence Dashboard on http://localhost:8765 and provides
REST endpoints to execute the Resume Agent and open generated deliverables on macOS.
Zero external pip dependencies (uses Python standard library only).
"""
import os
import sys
import json
import subprocess
import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
PROJECT_ROOT = Path(__file__).resolve().parent.parent

class DashboardHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        clean_path = self.path.split("?")[0]
        if clean_path in ["/", "/index.html"]:
            filepath = PROJECT_ROOT / "dashboard" / "index.html"
            if filepath.exists():
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                with open(filepath, "rb") as f:
                    self.wfile.write(f.read())
                return

        elif clean_path == "/api/status":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ready", "cwd": str(PROJECT_ROOT)}).encode("utf-8"))
            return

        elif clean_path == "/api/jobs":
            # Retrieve persistent jobs from SQLite (data/jobs.db)
            try:
                if str(PROJECT_ROOT / "src") not in sys.path:
                    sys.path.insert(0, str(PROJECT_ROOT / "src"))
                import resume_agent.db
                import importlib
                importlib.reload(resume_agent.db)
                jobs = resume_agent.db.get_all_jobs(min_score=0)
                tiers = resume_agent.db.get_tier_counts()
                resp = {"success": True, "jobs": jobs, "tier_counts": tiers}
            except Exception as e:
                json_file = PROJECT_ROOT / "data" / "jobs.json"
                if json_file.exists():
                    with open(json_file, "r", encoding="utf-8") as f:
                        jobs = json.load(f)
                    resp = {"success": True, "jobs": jobs, "notice": f"Loaded from json: {e}"}
                else:
                    resp = {"success": False, "error": str(e), "jobs": []}

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(resp).encode("utf-8"))
            return

        self.send_response(404)
        self.end_headers()
        self.wfile.write(b"Not Found")

    def do_POST(self):
        clean_path = self.path.split("?")[0]
        if clean_path == "/api/run-agent":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            data = json.loads(body) if body else {}

            cmd = data.get("command", "")
            job_title = data.get("jobTitle", "Job")
            output_dir = data.get("outputDir", "")

            # Prepare execution environment with project root and src/ in PYTHONPATH
            env = os.environ.copy()
            src_dir = str(PROJECT_ROOT / "src")
            root_dir = str(PROJECT_ROOT)
            existing_pp = env.get("PYTHONPATH", "")
            env["PYTHONPATH"] = f"{src_dir}{os.pathsep}{root_dir}" + (f"{os.pathsep}{existing_pp}" if existing_pp else "")

            # Ensure subprocess uses the active Python interpreter
            py_exec = sys.executable
            exec_cmd = cmd
            if cmd.startswith("python3 "):
                exec_cmd = f'"{py_exec}" {cmd[len("python3 "):]}'
            elif cmd.startswith("python "):
                exec_cmd = f'"{py_exec}" {cmd[len("python "):]}'

            try:
                proc = subprocess.run(
                    exec_cmd,
                    shell=True,
                    cwd=str(PROJECT_ROOT),
                    env=env,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=180
                )
                output = proc.stdout + ("\n" + proc.stderr if proc.stderr else "")
                success = proc.returncode == 0
            except subprocess.TimeoutExpired:
                success = False
                output = "Execution timed out after 3 minutes."
            except Exception as e:
                success = False
                output = f"Execution error: {str(e)}"

            target_out = PROJECT_ROOT / output_dir if output_dir else PROJECT_ROOT / "output"

            response_data = {
                "success": success,
                "jobTitle": job_title,
                "output": output,
                "outputDir": str(target_out)
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode("utf-8"))

        elif clean_path == "/api/open-folder":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            data = json.loads(body) if body else {}
            folder = data.get("folder", "")
            full_path = PROJECT_ROOT / folder if not folder.startswith("/") else Path(folder)
            
            if not full_path.exists() and "output" in str(full_path):
                full_path.mkdir(parents=True, exist_ok=True)

            if full_path.exists():
                subprocess.run(["open", str(full_path)])
                res = {"success": True}
            else:
                fallback_output = PROJECT_ROOT / "output"
                if fallback_output.exists():
                    subprocess.run(["open", str(fallback_output)])
                    res = {"success": True, "notice": "Opened output base folder"}
                else:
                    res = {"success": False, "error": f"Folder not found: {full_path}"}

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(res).encode("utf-8"))

        elif clean_path == "/api/job-status":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            data = json.loads(body) if body else {}

            job_id = data.get("id")
            status = data.get("status", "active")
            applied_at = data.get("appliedAt")

            try:
                if str(PROJECT_ROOT / "src") not in sys.path:
                    sys.path.insert(0, str(PROJECT_ROOT / "src"))
                from resume_agent.db import update_job_status
                ok = update_job_status(job_id, status, applied_at)
                res = {"success": ok}
            except Exception as e:
                res = {"success": False, "error": str(e)}

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(res).encode("utf-8"))

        elif clean_path == "/api/run-job-search":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8") if content_length > 0 else "{}"
            data = json.loads(body) if body else {}
            min_score = data.get("minScore", 60)

            py_exec = sys.executable
            cmd = f'"{py_exec}" job_search_engine.py --min-score {min_score}'
            env = os.environ.copy()
            src_dir = str(PROJECT_ROOT / "src")
            root_dir = str(PROJECT_ROOT)
            env["PYTHONPATH"] = f"{src_dir}{os.pathsep}{root_dir}" + (f"{os.pathsep}{env.get('PYTHONPATH', '')}" if env.get('PYTHONPATH') else "")

            try:
                proc = subprocess.run(
                    cmd,
                    shell=True,
                    cwd=str(PROJECT_ROOT),
                    env=env,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=120
                )
                output = proc.stdout + ("\n" + proc.stderr if proc.stderr else "")
                success = proc.returncode == 0
            except Exception as e:
                output = f"Error running job search: {e}"
                success = False

            try:
                if str(PROJECT_ROOT / "src") not in sys.path:
                    sys.path.insert(0, str(PROJECT_ROOT / "src"))
                from resume_agent.db import get_all_jobs, get_tier_counts
                jobs = get_all_jobs(min_score=min_score)
                tiers = get_tier_counts()
            except Exception:
                jobs = []
                tiers = {}

            res = {
                "success": success,
                "output": output,
                "jobs": jobs,
                "tier_counts": tiers
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(res).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

def main():
    os.chdir(PROJECT_ROOT)
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, DashboardHandler)
    url = f"http://localhost:{PORT}/"
    print(f"============================================================")
    print(f"🚀 Job Intelligence Dashboard Server running at:")
    print(f"   {url}")
    print(f"   Agent bridge active: Click '▶ Run Resume Agent' directly in browser!")
    print(f"============================================================")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")

if __name__ == "__main__":
    main()
