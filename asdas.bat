import os
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
    ok, out = ejecutar_git(f'git commit -m "{mensaje}"')
    if not ok:
        if "nothing to commit" in out: