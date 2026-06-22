import os
import shutil
import glob

BASE = "C:/IA/AGENTE/MECANICO"
BACKUPS = "C:/IA/AGENTE/MECANICO/memoria/backups"

def listar_backups(archivo):
    nombre = os.path.basename(archivo)
    patron = os.path.join(BACKUPS, f"{nombre}.backup_*")
    backups = sorted(glob.glob(patron), reverse=True)
    if not backups:
        return f"No hay backups de {nombre}"
    resultado = f"Backups de {nombre}:\n"
    for i, b in enumerate(backups[:5]):
        resultado += f"  {i+1}. {os.path.basename(b)}\n"
    return resultado

def revertir(archivo):
    nombre = os.path.basename(archivo)
    patron = os.path.join(BACKUPS, f"{nombre}.backup_*")
    backups = sorted(glob.glob(patron), reverse=True)
    if not backups:
        return f"ERROR: No hay backups de {nombre}"
    backup_reciente = backups[0]
    if os.path.isabs(archivo):
        ruta_destino = archivo
    else:
        ruta_destino = os.path.join(BASE, archivo)
    shutil.copy2(backup_reciente, ruta_destino)
    return f"OK Revertido a: {os.path.basename(backup_reciente)}\nArchivo restaurado: {ruta_destino}"

def ejecutar(accion, texto):
    palabras = texto.split()
    archivo = palabras[-1] if len(palabras) > 1 else ""
    if not archivo:
        return "ERROR: Especifica el archivo. Ej: revertir mecanico.py"
    if "listar" in texto.lower():
        return listar_backups(archivo)
    return revertir(archivo)
