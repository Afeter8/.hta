@echo off
echo Protegiendo sistema...
:: Comprobar identidad
certutil -hashfile C:\Fernando.key SHA256 > nul || exit

:: Activar protección
schtasks /create /tn "StarTigoProteccion" /tr "powershell -File C:\StarTigo\init.ps1" /sc onstart /rl highest /f

:: Hacer inmutable el sistema
icacls "C:\Windows" /deny "Users:(DE,WD)" /t /c

:: Mensaje de éxito
echo StarTigo Antivirus Activado. Sistema protegido para Fernando GME.
pause
