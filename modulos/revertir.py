import os
import shutil
import glob
import re
from typing import List

BASE: str = os.environ.get('BASE_DIR', "C:/IA/AGENTE/MECANICO")
BACKUPS: str = os.path.join(BASE, "memoria", "backups")

def listar_backups(archivo: str) -> List[str]:
    """
    Lista los backups de un archivo.

    Args:
    archivo (str): Ruta del archivo.

    Returns:
    List[str]: Lista de nombres de los backups del archivo.
    """
    if not archivo:
        raise ValueError("El archivo no puede ser vacío")

    nombre = os.path.basename(archivo)
    patron = os.path.join(BACKUPS, f"{nombre}.backup_*")
    backups = sorted(glob.glob(patron), reverse=True)
    if not backups:
        raise ValueError(f"No hay backups de {nombre}")

    return [os.path.basename(b) for b in backups[:5]]

def revertir(archivo: str, indice: int = 0) -> str:
    """
    Revierte un archivo a su versión más reciente.

    Args:
    archivo (str): Ruta del archivo.
    indice (int): Indice del backup a utilizar (0 para el más reciente).

    Returns:
    str: Mensaje de confirmación de la reversión.
    """
    if not archivo:
        raise ValueError("El archivo no puede ser vacío")

    if indice < 0:
        raise ValueError("El indice no puede ser negativo")

    nombre = os.path.basename(archivo)
    patron = os.path.join(BACKUPS, f"{nombre}.backup_*")
    backups = sorted(glob.glob(patron), reverse=True)
    if not backups:
        raise ValueError(f"No hay backups de {nombre}")

    if indice == 0 or indice > len(backups):
        indice = 0

    backup_seleccionado = backups[indice]
    ruta_destino = os.path.abspath(archivo)
    try:
        shutil.copy2(backup_seleccionado, ruta_destino)
        return f"OK Revertido a: {os.path.basename(backup_seleccionado)}\nArchivo restaurado: {ruta_destino}"
    except Exception as e:
        raise ValueError(f"Error al revertir el archivo: {e}")

def ejecutar(accion, texto):
    """
    Ejecuta una acción sobre un archivo.
    
    Parametros:
    accion (str): Acción a realizar.
    texto (str): Texto que contiene la ruta del archivo.
    
    Retorno:
    str: Mensaje de confirmación o error.
    """
    palabras = texto.split()
    match_num = re.search(r'\d+$', texto)
    if match_num and len(palabras) > 2:
        archivo = palabras[-2]
    else:
        archivo = palabras[-1] if len(palabras) > 1 else ""
    if not archivo:
        return "ERROR: Especifica el archivo. Ej: revertir mecanico.py"
    if "listar" in texto.lower():
        return "\n".join(listar_backups(archivo))

    match = re.search(r'\d+$', texto)
    if match:
        try:
            indice = int(match.group()) - 1  # Restamos 1 para convertir a 0-index
        except ValueError:
            return "ERROR: Indice no es un numero"
    else:
        indice = 0

    return revertir(archivo, indice)

def main():
    accion = input("Ingrese la acción (listar o revertir): ")
    archivo = input("Ingrese la ruta del archivo (puede incluir el indice del backup, por ejemplo revertir mecanico.py 3): ")
    texto = f"{accion} {archivo}"
    if "listar" in texto.lower():
        try:
            print("\n".join(listar_backups(archivo)))
        except ValueError as e:
            print(e)
    elif "revertir" in texto.lower():
        try:
            resultado = revertir(archivo) if " " not in archivo else ejecutar(accion, texto)
            print(resultado)
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
