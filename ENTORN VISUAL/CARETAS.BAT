@echo off
chcp 65001 >nul
echo ============================================
echo   MECANICO IA - Creando Entorno Visual
echo ============================================
echo.

set BASE=C:\IA\AGENTE\MECANICO
set VISUAL=%BASE%\visual

echo [1/6] Creando directorio raiz visual...
mkdir "%VISUAL%" 2>nul

echo [2/6] Creando subdirectorios...
mkdir "%VISUAL%\css" 2>nul
mkdir "%VISUAL%\js" 2>nul
mkdir "%VISUAL%\assets" 2>nul
mkdir "%VISUAL%\assets\icons" 2>nul
mkdir "%VISUAL%\assets\fonts" 2>nul
mkdir "%VISUAL%\pages" 2>nul
mkdir "%VISUAL%\components" 2>nul
mkdir "%VISUAL%\data" 2>nul

echo [3/6] Creando directorio de logs visuales...
mkdir "%VISUAL%\logs" 2>nul

echo [4/6] Creando directorio de temas...
mkdir "%VISUAL%\themes" 2>nul

echo [5/6] Creando directorio de plantillas...
mkdir "%VISUAL%\templates" 2>nul

echo [6/6] Estructura creada exitosamente!
echo.
echo Estructura final:
echo   %VISUAL%
echo   ├── css\
echo   ├── js\
echo   ├── assets\
echo   │   ├── icons\
echo   │   └── fonts\
echo   ├── pages\
echo   ├── components\
echo   ├── data\
echo   ├── logs\
echo   ├── themes\
echo   └── templates\
echo.
echo Presiona cualquier tecla para continuar...
pause >nul