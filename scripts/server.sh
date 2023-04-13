#!/usr/bin/env bash

# Check for python
if ! command -v python &>/dev/null; then
  echo "Python could not be found"
  exit
fi

# Activate the virtual environment
source venv/bin/activate

# Run the server
uvicorn main:app --reload
