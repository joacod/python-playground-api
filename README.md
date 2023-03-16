# Python Playground
Python playground Web API using [Flask](https://flask.palletsprojects.com/en/2.2.x//)

## Prerequisites
- [Install Python](https://www.python.org/downloads/)

## Setup
- At root of project, create a virtual environment:
     - `python3 -m venv .venv` (macOS/Linux)
     - `python -m venv .venv` (Windows)

- Activate the virtual environment:
     - `. .venv/bin/activate` (macOS/Linux)
     - `.venv\Scripts\activate` (Windows)

- Install dependencies:
    - `pip install -r requirements.txt`

## Run the application
At "/src" folder run:
- `flask --app=app run`