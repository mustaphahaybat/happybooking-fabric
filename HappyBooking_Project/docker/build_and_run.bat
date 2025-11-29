@echo off
echo ====================================
echo Hotel Booking Stream Producer
echo ====================================

cd /d %~dp0

echo.
echo [1/3] Building Docker image...
docker build -t hotel-stream-producer:latest -f Dockerfile .

if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Build failed!
    pause
    exit /b 1
)

echo.
echo [2/3] Build successful!
echo.
echo [3/3] Starting stream producer...
echo.
echo Press Ctrl+C to stop streaming
echo.

docker run --rm --env-file .env hotel-stream-producer:latest

pause