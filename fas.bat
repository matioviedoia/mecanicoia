# Crea todos los modulos de MECANICO

import os

BASE = "C:/IA/AGENTE/MECANICO/modulos"

git_manager = '''import os
import subprocess
import datetime

BASE = "C:/IA/AGENTE/MECANICO"

def ejecutar_git(comando):
    try:
        resultado = subprocess.run(comando, cwd=BASE, capture_output=True, text=True, shell=True)
        if resultado.returncode == 0:
            return True, resultado.stdout.strip()
        else:
            return False, resultado.stderr.strip()
    except Exception as e:
        return False, str(e)

def commit_automatico(mensaje=None):
    if not mensaje:
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mensaje = f"MECANICO auto-commit {fecha}"
    ok, out = ejecutar_git("git add .")
    if not ok:
        return f"ERROR en git add: {out}"
    ok, out = ejecutar_git(f\'git commit -m "{mensaje}"\')
    if not ok:
        if "nothing to commit" in out:
            return "INFO: No hay cambios para commitear"
        return f"ERROR en git commit: {out}"
    return f"OK Commit: {mensaje}"

def push():
    ok, out = ejecutar_git("git push origin master")
    if not ok:
        return f"ERROR en git push: {out}"
    return f"OK Push exitoso"

def commit_y_push(mensaje=None):
    resultado_commit = commit_automatico(mensaje)
    if "ERROR" in resultado_commit:
        return resultado_commit
    return push()

def ver_estado():
    ok, out = ejecutar_git("git status")
    return out

def ver_historial(n=5):
    ok, out = ejecutar_git(f"git log --oneline -{n}")
    return out

def ejecutar(accion, texto):
    t = texto.lower()
    if "push" in t:
        return commit_y_push()
    elif "estado" in t or "status" in t:
        return ver_estado()
    elif "historial" in t or "log" in t:
        return ver_historial()
    else:
        return commit_automatico()
'''

with open(os.path.join(BASE, "git_manager.py"), "w", encoding="utf-8") as f:
    f.write(git_manager)

print("OK git_manager.py creado!")