@echo off
python -m nuitka --onefile --standalone --follow-imports latencia.py -o "Latencia.exe"
