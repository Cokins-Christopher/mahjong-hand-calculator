@echo off
echo Starting Mahjong Hand Calculator...
echo.

echo Starting Backend (Flask)...
start "Backend" cmd /k "cd backend && python app.py"

echo Waiting 5 seconds for backend to start...
timeout /t 5 /nobreak > nul

echo Starting Frontend (React)...
start "Frontend" cmd /k "cd frontend && npm start"

echo.
echo Both services are starting...
echo Backend will be available at: http://localhost:5000
echo Frontend will be available at: http://localhost:3000
echo.
echo Press any key to close this window...
pause > nul 