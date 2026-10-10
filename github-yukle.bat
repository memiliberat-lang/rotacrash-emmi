@echo off
title GitHub'a Yukle - RotaMaster
cd /d "%~dp0"
echo ============================================================
echo   GitHub'a Yukleniyor...
echo   Hedef: https://github.com/memiliberat-lang/rotacrash-emmi.git
echo ============================================================
echo.
echo Eger tarayici acilirsa GitHub girisinizi onaylayin.
echo.

git remote remove origin >nul 2>&1
git remote add origin https://github.com/memiliberat-lang/rotacrash-emmi.git
git branch -M main
git push -u origin main

echo.
echo ============================================================
echo   ISLEM TAMAMLANDI!
echo ============================================================
pause
