#!/bin/bash
# Double-click to launch the Job Intelligence Dashboard Server on macOS
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

echo "============================================================"
echo "🚀 Starting Job Intelligence Dashboard Server..."
echo "============================================================"
python3 dashboard/server.py
