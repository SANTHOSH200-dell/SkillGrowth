@echo off
title SkillGrowth Platform
cd /d "%~dp0"
start "SkillGrowth Backend" cmd /k "cd /d %~dp0backend && if not exist venv python -m venv venv && call venv\Scripts\activate && pip install -r requirements.txt && uvicorn app.main:app --reload"
timeout /t 5 /nobreak >nul
start "SkillGrowth Frontend" cmd /k "cd /d %~dp0 && python -m http.server 5500"
timeout /t 2 /nobreak >nul
start "" "http://127.0.0.1:5500/index.html"
