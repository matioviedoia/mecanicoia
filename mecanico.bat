@echo off
title MECANICO IA - Instalador
color 0A
echo ================================================
echo    MECANICO IA - Instalador Automatico
echo ================================================
echo.

:: ============================================
:: PASO 1 - Crear estructura de carpetas
:: ============================================
echo [1/6] Creando estructura de carpetas...
mkdir C:\IA\MECANICO\modulos 2>nul
mkdir C:\IA\MECANICO\memoria\sesiones 2>nul
mkdir C:\IA\MECANICO\memoria\errores 2>nul
mkdir C:\IA\MECANICO\memoria\backups 2>nul
mkdir C:\IA\MECANICO\workspace 2>nul
mkdir C:\IA\MECANICO\proyectos 2>nul
mkdir C:\IA\MECANICO\apis 2>nul
echo    OK Carpetas creadas
echo.

:: ============================================
:: PASO 2 - Instalar librerias Python
:: ============================================
echo [2/6] Instalando librerias Python...
pip install groq google-generativeai gitpython python-dotenv requests colorama --quiet
echo    OK Librerias instaladas
echo.

:: ============================================
:: PASO 3 - Configurar API keys
:: ============================================
echo [3/6] Configurando API keys...
echo.
set /p GROQ_KEY="   Pega tu API key de Groq: "
set /p GEMINI_KEY="   Pega tu API key de Gemini: "
set /p GITHUB_REPO="   URL de tu repositorio GitHub (ej: https://github.com/usuario/mecanico): "
set /p GIT_EMAIL="   Tu email de GitHub: "
set /p GIT_NAME="   Tu nombre para Git: "
echo.

:: Guardar en .env
echo GROQ_API_KEY=%GROQ_KEY% > C:\IA\MECANICO\.env
echo GEMINI_API_KEY=%GEMINI_KEY% >> C:\IA\MECANICO\.env
echo GITHUB_REPO=%GITHUB_REPO% >> C:\IA\MECANICO\.env
echo OLLAMA_URL=http://localhost:11434 >> C:\IA\MECANICO\.env
echo    OK API keys guardadas en .env
echo.

:: ============================================
:: PASO 4 - Configurar Git
:: ============================================
echo [4/6] Configurando Git...
git config --global user.email "%GIT_EMAIL%"
git config --global user.name "%GIT_NAME%"
cd C:\IA\MECANICO
git init
git remote add origin %GITHUB_REPO%
echo    OK Git configurado
echo.

:: ============================================
:: PASO 5 - Crear archivos base
:: ============================================
echo [5/6] Creando archivos base...

:: config.py
(
echo # ============================================
echo # MECANICO IA - Configuracion central
echo # ============================================
echo import os
echo from dotenv import load_dotenv
echo.
echo load_dotenv^("C:/IA/MECANICO/.env"^)
echo.
echo RUTAS = {
echo     "workspace":  "C:/IA/MECANICO/workspace",
echo     "proyectos":  "C:/IA/MECANICO/proyectos",
echo     "sesiones":   "C:/IA/MECANICO/memoria/sesiones",
echo     "errores":    "C:/IA/MECANICO/memoria/errores",
echo     "backups":    "C:/IA/MECANICO/memoria/backups",
echo     "modulos":    "C:/IA/MECANICO/modulos",
echo }
echo.
echo APIS = {
echo     "groq":   {"key": os.getenv^("GROQ_API_KEY"^),    "activa": True,  "modelo": "llama-3.3-70b-versatile"},
echo     "gemini": {"key": os.getenv^("GEMINI_API_KEY"^),  "activa": True,  "modelo": "gemini-2.0-flash"},
echo     "ollama": {"key": None,                           "activa": True,  "modelo": "gemma3:4b",  "url": "http://localhost:11434"},
echo }
echo.
echo MODOS = {
echo     "auto":   "MECANICO trabaja solo sin pedir confirmacion",
echo     "manual": "MECANICO pide confirmacion antes de cada accion",
echo     "mixto":  "MECANICO decide segun la complejidad",
echo }
echo.
echo MODO_ACTUAL = "manual"
echo GITHUB_REPO = os.getenv^("GITHUB_REPO"^)
) > C:\IA\MECANICO\config.py

:: .gitignore
(
echo .env
echo __pycache__/
echo *.pyc
echo memoria/sesiones/
echo memoria/errores/
echo memoria/backups/
) > C:\IA\MECANICO\.gitignore

echo    OK Archivos base creados
echo.

:: ============================================
:: PASO 6 - Primer commit
:: ============================================
echo [6/6] Primer commit en GitHub...
cd C:\IA\MECANICO
git add .
git commit -m "MECANICO IA - Instalacion inicial"
echo    OK Listo para push ^(necesitas autenticarte en GitHub^)
echo.

echo ================================================
echo    MECANICO IA instalado correctamente!
echo ================================================
echo.
echo Proximos pasos:
echo  1. cd C:\IA\MECANICO
echo  2. python mecanico.py
echo.
pause
