import os
import subprocess
import datetime

BASE = os.path.abspath(os.path.dirname(__file__))

def ejecutar_git(comando):
    """
    Ejecuta un comando git en el directorio base.
    
    Args:
        comando (str): Comando git a ejecutar.
    
    Returns:
        tuple: (boolean, str) Indicando si el comando fue exitoso y el resultado.
    """
    try:
        resultado = subprocess.run(comando, cwd=BASE, capture_output=True, text=True, shell=True, check=False)
        if resultado.returncode == 0:
            return True, resultado.stdout.strip()
        else:
            return False, resultado.stderr.strip()
    except Exception as e:
        return False, str(e)

def commit_automatico(mensaje=None):
    """
    Realiza un commit automático con un mensaje.
    
    Args:
        mensaje (str, optional): Mensaje del commit. Si no se proporciona, se utiliza la fecha y hora actual.
    
    Returns:
        str: Mensaje de resultado del commit.
    """
    if not mensaje:
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mensaje = f"MECANICO auto-commit {fecha}"
    ok, out = ejecutar_git("git add .")
    if not ok:
        return f"ERROR en git add: {out}"
    ok, out = ejecutar_git(f'git commit -m "{mensaje}"')
    if not ok:
        if "nothing to commit" in out:
            return "INFO: No hay cambios para commitear"
        return f"ERROR en git commit: {out}"
    return f"OK Commit: {mensaje}"

def push():
    """
    Realiza un push a la rama master del origen.
    
    Returns:
        str: Mensaje de resultado del push.
    """
    ok, out = ejecutar_git("git push origin master")
    if not ok:
        return f"ERROR en git push: {out}"
    return f"OK Push exitoso"

def commit_y_push(mensaje=None):
    """
    Realiza un commit automático y luego un push.
    
    Args:
        mensaje (str, optional): Mensaje del commit.
    
    Returns:
        str: Mensaje de resultado del commit y push.
    """
    resultado_commit = commit_automatico(mensaje)
    if "ERROR" in resultado_commit:
        return resultado_commit
    return push()

def ver_estado():
    """
    Muestra el estado actual del repositorio.
    
    Returns:
        str: Estado del repositorio.
    """
    ok, out = ejecutar_git("git status")
    return out

def ver_historial(n=5):
    """
    Muestra el historial de commits.
    
    Args:
        n (int, optional): Número de commits a mostrar. Por defecto, 5.
    
    Returns:
        str: Historial de commits.
    """
    ok, out = ejecutar_git(f"git log --oneline -{n}")
    return out

def ejecutar(accion, texto):
    """
    Ejecuta una acción en función del texto proporcionado.
    
    Args:
        accion (str): Acción a realizar.
        texto (str): Texto que determina la acción a realizar.
    
    Returns:
        str: Mensaje de resultado de la acción.
    """
    t = texto.lower()
    if "push" in t:
        return commit_y_push()
    elif "estado" in t or "status" in t:
        return ver_estado()
    elif "historial" in t or "log" in t:
        return ver_historial()
    else:
        return commit_automatico()

# Uso ejemplos:
# print(ejecutar("commit", "commit"))
# print(ejecutar("push", "push"))
# print(ejecutar("estado", "estado"))
# print(ejecutar("historial", "historial"))