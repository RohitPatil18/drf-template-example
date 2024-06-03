#!/bin/bash

# Check if virtual environment is requested
if [ "{{ cookiecutter.create_virtualenv }}" == "yes" ]; then
    # Create a virtual environment
    python3 -m venv .venv
    echo "Virtual environment created."
    
    # Activate the virtual environment
    source venv/bin/activate
    
    # Install requirements if requirements.txt exists
    if [ -f "requirements/base.txt" ]; then
        pip install -r requirements.txt
        echo "Requirements installed."
    fi

    # Install isort and black
    pip install isort black
    echo "isort and black installed."
    
    # Run isort and black
    isort .
    black .
    echo "Code formatted with isort and black."

    echo "To activate the virtual environment, run: source venv/bin/activate"
else
    echo "Virtual environment creation skipped."
fi
