@echo off
echo Setting up Mahjong Hand Calculator...
echo.

echo Installing Frontend Dependencies...
cd frontend
call npm install
if %errorlevel% neq 0 (
    echo Error installing frontend dependencies
    pause
    exit /b 1
)
cd ..

echo.
echo Installing Backend Dependencies...
cd backend
call pip install Flask==2.3.3 Flask-CORS==4.0.0 opencv-python==4.8.1.78 numpy>=1.26.0 Pillow>=10.0.0 python-dotenv==1.0.0 pytest==7.4.2
if %errorlevel% neq 0 (
    echo Error installing backend dependencies
    pause
    exit /b 1
)
cd ..

echo.
echo Setup complete!
echo.
echo To start the application, run: start.bat
echo.
pause 