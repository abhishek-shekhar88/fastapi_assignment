# FastAPI Project with Poetry

## Overview

This project is a FastAPI application that provides an endpoint for performing addition on input lists of integers. The application uses Python's multiprocessing pool to handle addition tasks efficiently. It includes request and response validation using Pydantic models and is organized following the MVC (Model-View-Controller) format. Unit tests are provided to cover edge cases and scenarios, and the project uses Poetry for dependency management and testing.

## Prerequisites

- Python 3.8 or higher
- Poetry

## Installation

### Step 1: Install Python
```bash 
python3 --version
pip install virtualenv
virtualenv venv --python=python3.8
source venv/bin/activate
```

### Step 2: Install Poetry

Follow the official [Poetry installation guide](https://python-poetry.org/docs/#installation) to install Poetry.
pip install poetry
poetry shell
poetry install
poetry add <module> # if want to add any module
poetry lock # to create lock file

### Step 3: Clone the Repository

Clone the repository to your local machine:
```bash
git clone <repository-url>
cd fastapi_project
```

### Step 4: Install Dependencies
Use Poetry to install the project dependencies:
```bash
poetry install
```
### Running the Application
To start the FastAPI application, use the following command:

```bash
Copy code
poetry run uvicorn fastapi_project.main:app --reload
```

### Running Tests
To run the tests and check code coverage, use the following command:

```bash
Copy code
poetry run coverage run -m pytest
```
