@echo off
set "PYTHONPATH=%~dp0..\.python-packages;%PYTHONPATH%"
python "%~dp0..\manage.py" runserver %*

