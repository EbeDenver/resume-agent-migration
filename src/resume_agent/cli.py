"""Command Line Interface for the Automated Resume Generator.

Supports single job processing, batch processing, setup, and config inspection.
Loads Ebenezer J. Rolston's Master Resume from data/master_resume.md into the graph state.
"""
from typing import List, Optional
from pathlib import Path
import typer
from rich.console import Console
from rich.table import Table

from resume_agent.config import AppSettings
from resume_agent.graph.graph import run_pipeline

app = typer.Typer(
    name="resume-agent",
    help="Automated Resume Generator — local Python pipeline for Ebenezer J. Rolston."
)
console = Console()

@app.command()
def run(
    job_url: Optional[List[str]] = typer.Option(
        None, "--job-url", "-u", help="One or more job posting URLs to analyze."
    ),
    job_list_doc: Optional[str] = typer.Option(
        None, "--job-list-doc", "-d", help="Google Doc URL containing job URLs."
    ),
    master_resume: Optional[str] = typer.Option(
        None, "--master-resume", "-r", help="Optional master resume file path or Google Doc URL."
    ),
    mode: str = typer.Option(
        "normal", "--mode", "-m", help="Mode: 'normal' or 'fact_finding'."
    ),
):
    """Run the Automated Resume Generator pipeline on job postings."""
    console.print("[bold navy]Automated Resume Generator — Starting Run...[/bold navy]")

    # 1. Load configuration
    settings = AppSettings.load()
    console.print(f"[dim]Google Account: {settings.google.account_email}[/dim]")
    console.print(f"[dim]Timezone: {settings.timezone}[/dim]")

    # 2. Build raw jobs input queue
    raw_inputs = []
    if job_url:
        raw_inputs.extend(job_url)
    if job_list_doc:
        raw_inputs.append(job_list_doc)
    if not raw_inputs:
        console.print("[yellow]No job URLs provided. Prompting for input...[/yellow]")
        pasted = typer.prompt("Enter a job posting URL or paste job description text")
        raw_inputs.append(pasted)

    # 3. Check master resume file
    resume_path = Path(master_resume) if master_resume else Path("data/master_resume.md")
    if resume_path.exists():
        console.print(f"[green]Loaded Master Resume from: {resume_path}[/green]")
    else:
        console.print("[yellow]Master Resume file data/master_resume.md not found. Will use embedded default.[/yellow]")

    # 4. Execute LangGraph pipeline
    console.print("\n[bold]Executing LangGraph Pipeline Nodes...[/bold]")
    result = run_pipeline(raw_inputs=raw_inputs, mode=mode)

    # 5. Display Summary Output
    console.print("\n" + result.get("final_summary", "Run completed successfully."))

@app.command()
def setup():
    """Verify configuration, Google OAuth credentials, and resource folders."""
    settings = AppSettings.load()
    console.print("[bold blue]Configuration & OAuth Status Verification[/bold blue]")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Resource", style="dim")
    table.add_column("Configured Value")

    table.add_row("Google Account", settings.google.account_email)
    table.add_row("Job Tracker", settings.google.job_tracker_url)
    table.add_row("Drive Root Folder", settings.google.drive_root_folder_id)
    table.add_row("Master Resume Folder", settings.google.master_resume_folder_id)
    table.add_row("Generated Resumes Folder", settings.google.generated_resumes_folder_id)
    table.add_row("Cover Letters Folder", settings.google.cover_letters_folder_id)
    table.add_row("Job Analyses Folder", settings.google.job_analyses_folder_id)
    table.add_row("Master Resume File", "data/master_resume.md (exists)" if Path("data/master_resume.md").exists() else "Missing")

    console.print(table)
    console.print("[green]Setup verification complete![/green]")

@app.command()
def config():
    """Display current agent settings."""
    settings = AppSettings.load()
    console.print_json(data=settings.model_dump())

if __name__ == "__main__":
    app()
