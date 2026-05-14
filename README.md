# git-demo

Django development environment for this project.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Optional test tooling:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
```

## Useful Commands

```powershell
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py test
.\.venv\Scripts\python.exe manage.py runserver
```

When `pytest` and `pytest-django` are installed:

```powershell
.\.venv\Scripts\python.exe -m pytest
```
