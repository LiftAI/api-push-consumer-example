#!/usr/bin/env bash

# Check for python
if ! command -v python &>/dev/null; then
  echo "Python could not be found"
  exit
fi

# Create a virtual environment if it doesn't exist
if [ ! -d venv ]; then
  python -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Update pip
pip install --upgrade pip

# Install the requirements
pip install -r requirements.txt

# Deactivate the virtual environment
deactivate
