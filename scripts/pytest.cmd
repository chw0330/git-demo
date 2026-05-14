@echo off
set "PYTHONPATH=%~dp0..\.python-packages;%PYTHONPATH%"
python -m pytest %*

