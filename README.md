# Python Playground
Python playground Web API using [Flask](https://flask.palletsprojects.com/en/2.2.x/)

<p align="center">
  <img height="200" src="https://res.cloudinary.com/practicaldev/image/fetch/s--yfF3_q8k--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/f0i5oszdj3gwk686xuc0.JPG">
</p>

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
At root folder run:
- `flask --app=app run`

## Run Tests
At root folder run:
- `python -m unittest discover -p "*_test.py" -vv`
