import os
import shutil
from datetime import datetime

def listar(ruta: str) -> str:
    """
    Lista el contenido de una carpeta.

    Args:
        ruta (str): La ruta de la carpeta.

    Returns:
        str: Un mensaje con el contenido de la carpeta.

    Raises:
        FileNotFoundError: Si la ruta no existe.
        PermissionError: Si no se tiene permiso para acceder a la carpeta.
    """
    try:
        items = os.scandir(ruta)
    except FileNotFoundError:
        return f"ERROR: Ruta no encontrada: {ruta}"
    except PermissionError:
        return f"ERROR: No se tiene permiso para acceder a la carpeta {ruta}"

    carpetas = []
    archivos = []
    for item in items:
        if item.is_dir():
            carpetas.append(f"  [DIR] {item.name}")
        else:
            size = item.stat().st_size
            size_str = f"{size} bytes" if size < 1024 else f"{round(size/1024, 1)} KB"
            archivos.append(f"  [FILE] {item.name} ({size_str})")

    resultado = f"Contenido de {ruta}:\n"
    resultado += "\n".join(carpetas + archivos)
    resultado += f"\n\nTotal: {len(carpetas)} carpetas, {len(archivos)} archivos"
    return resultado

def buscar(ruta: str, patron: str) -> str:
    """
    Busca archivos que contengan un patrón en una carpeta y sus subcarpetas.

    Args:
        ruta (str): La ruta de la carpeta.
        patron (str): El patrón a buscar.

    Returns:
        str: Un mensaje con los archivos encontrados.
    """
    if not os.path.exists(ruta):
        return f"ERROR: Ruta no encontrada: {ruta}"
    encontrados = []
    for raiz, dirs, archivos in os.walk(ruta):
        dirs[:] = [d for d in dirs if d not in ["__pycache__", ".git", "node_modules"]]
        for archivo in archivos:
            if patron.lower() in archivo.lower():
                ruta_completa = os.path.join(raiz, archivo)
                encontrados.append(ruta_completa)
    if not encontrados:
        return f"No se encontro '{patron}' en {ruta}"
    return f"Encontrados {len(encontrados)} archivos:\n" + "\n".join(encontrados[:20])

def crear_carpeta(ruta: str) -> str:
    """
    Crea una carpeta.

    Args:
        ruta (str): La ruta de la carpeta.

    Returns:
        str: Un mensaje con el resultado de la operación.
    """
    try:
        os.makedirs(ruta, exist_ok=True)
        return f"OK Carpeta creada: {ruta}"
    except Exception as e:
        return f"ERROR: {str(e)}"

def copiar(origen: str, destino: str) -> str:
    """
    Copia un archivo o carpeta.

    Args:
        origen (str): La ruta del archivo o carpeta original.
        destino (str): La ruta del archivo o carpeta destino.

    Returns:
        str: Un mensaje con el resultado de la operación.
    """
    try:
        if os.path.isdir(origen):
            shutil.copytree(origen, destino)
        else:
            shutil.copy2(origen, destino)
        return f"OK Copiado: {origen} -> {destino}"
    except Exception as e:
        return f"ERROR: {str(e)}"

def mover(origen: str, destino: str) -> str:
    """
    Mueve un archivo o carpeta.

    Args:
        origen (str): La ruta del archivo o carpeta original.
        destino (str): La ruta del archivo o carpeta destino.

    Returns:
        str: Un mensaje con el resultado de la operación.
    """
    try:
        shutil.move(origen, destino)
        return f"OK Movido: {origen} -> {destino}"
    except Exception as e:
        return f"ERROR: {str(e)}"

def ejecutar() -> None:
    print("Ejecutando...")
    # Agrega la lógica para ejecutar las funciones anteriores
    pass