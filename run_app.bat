@echo off
title Luyen Thi SPT HNUE
echo =======================================================
echo     DANG KHOI DONG HE THONG LUYEN THI SPT HNUE...
echo =======================================================
echo.

:: 1. Khoi dong Backend Server trong cua so rieng
echo [1/3] Dang khoi dong Backend Server (FastAPI)...
start "SPT Backend" cmd /c "cd backend && python -m uvicorn app.main:app"

:: Doi 3 giay de Backend khoi tao xong co so du lieu
timeout /t 3 /nobreak > NUL

:: 2. Tu dong mo trinh duyet den trang web
echo [2/3] Dang mo trang web tren trinh duyet...
start http://localhost:5173

:: 3. Khoi dong Frontend Server trong cua so hien tai
echo [3/3] Dang khoi dong Frontend Server (Vite)...
echo.
echo (De dung toan bo he thong, hay dong cua so nay lai)
echo.
cd frontend
npm run dev

pause
