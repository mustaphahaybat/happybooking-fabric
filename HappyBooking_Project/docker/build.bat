@echo off
echo ====================================
echo Docker Image Build Script
echo ====================================

REM Ana dizine git
cd ..

REM Image build et
echo Building Docker image...
docker build -t hotel-stream-producer:latest -f docker/Dockerfile .

echo.
echo ====================================
echo Build tamamlandi!
echo ====================================
echo.
echo Calistirmak icin:
echo docker run --rm -e EVENTSTREAM_URL=your-url hotel-stream-producer:latest
pause