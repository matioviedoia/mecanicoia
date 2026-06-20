@echo off
echo Creando modulo git_manager...

(
echo # ============================================
echo # MECANICO IA - Modulo Git Manager
echo # ============================================
echo.
echo import os
echo import subprocess
echo import datetime
echo.
echo BASE = CIAAGENTEMECANICO
echo.
echo def ejecutar_git^(comando^)
echo     try
echo         resultado = subprocess.run^(comando, cwd=BASE, capture_output=True, text=True, shell=True^)
echo         if resultado.returncode == 0
echo             return True, resultado.stdout.strip^(^)
echo         else
echo             return False, resultado.stderr.strip^(^)
echo     except Exception as e
echo         return False, str^(e^)
echo.
echo def commit_automatico^(mensaje=None^)
echo     if not mensaje
echo         fecha = datetime.datetime.now^(^).strftime^(%Y-%m-%d %H%M%S^)
echo         mensaje = fMECANICO auto-commit {fecha}
echo     ok, out = ejecutar_git^(git add .^)
echo     if not ok
echo         return fERROR en git add {out}
echo     ok, out = ejecutar_git^(f'git commit -m {mensaje}'^)
echo     if not ok
echo         if nothing to commit in out
echo             return INFO No hay cambios para commitear
echo         return fERROR en git commit {out}
echo     return fOK Commit {mensaje}n{out}
echo.
echo def push^(^)
echo     ok, out = ejecutar_git^(git push origin master^)
echo     if not ok
echo         return fERROR en git push {out}
echo     return fOK Push exitoson{out}
echo.
echo def commit_y_push^(mensaje=None^)
echo     resultado_commit = commit_automatico^(mensaje^)
echo     if ERROR in resultado_commit
echo         return resultado_commit
echo     resultado_push = push^(^)
echo     return f{resultado_commit}n{resultado_push}
echo.
echo def ver_estado^(^)
echo     ok, out = ejecutar_git^(git status^)
echo     return out
echo.
echo def ver_historial^(n=5^)
echo     ok, out = ejecutar_git^(fgit log --oneline -{n}^)
echo     return out
echo.
echo def ejecutar^(accion, texto^)
echo     t = texto.lower^(^)
echo     if push in t
echo         return commit_y_push^(^)
echo     elif estado in t or status in t
echo         return ver_estado^(^)
echo     elif historial in t or log in t
echo         return ver_historial^(^)
echo     else
echo         return commit_automatico^(^)
)  CIAAGENTEMECANICOmodulosgit_manager.py

echo OK git_manager.py creado!
pause