import os
import shutil
import datetime

def listar(ruta):
    """
    Lista el contenido de una carpeta.

    Args:
        ruta (str): La ruta de la carpeta.

    Returns:
        str: Un mensaje con el contenido de la carpeta.
    """
    if not os.path.exists(ruta):
        return f"ERROR: Ruta no encontrada: {ruta}"
    items = os.listdir(ruta)
    if not items:
        return f"Carpeta vacia: {ruta}"
    resultado = f"Contenido de {ruta}:\n"
    carpetas = []
    archivos = []
    for item in sorted(items):
        ruta_item = os.path.join(ruta, item)
        if os.path.isdir(ruta_item):
            carpetas.append(f"  [DIR] {item}")
        else:
            size = os.path.getsize(ruta_item)
            size_str = f"{size} bytes" if size < 1024 else f"{round(size/1024, 1)} KB"
            archivos.append(f"  [FILE] {item} ({size_str})")
    resultado += "\n".join(carpetas + archivos)
    resultado += f"\n\nTotal: {len(carpetas)} carpetas, {len(archivos)} archivos"
    return resultado

def buscar(ruta, patron):
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

def crear_carpeta(ruta):
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
        return f"ERROR: {e}"

def copiar(origen, destino):
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
        return f"ERROR: {e}"

def mover(origen, destino):
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
        return f"ERROR: {e}"

def leer(ruta):
    """
    Lee el contenido de un archivo.

    Args:
        ruta (str): La ruta del archivo.

    Returns:
        str: Un mensaje con el contenido del archivo.
    """
    if not os.path.exists(ruta):
        return f"ERROR: Archivo no encontrado: {ruta}"
    try:
        with open(ruta, "r", encoding="utf-8", errors="ignore") as f:
            contenido = f.read()
        lineas = contenido.split("\n")
        if len(lineas) > 50:
            return f"Primeras 50 lineas de {ruta}:\n" + "\n".join(lineas[:50]) + f"\n...({len(lineas)} lineas total)"
        return f"Contenido de {ruta}:\n{contenido}"
    except Exception as e:
        return f"ERROR: {e}"

def info(ruta):
    """
    Muestra información sobre un archivo o carpeta.

    Args:
        ruta (str): La ruta del archivo o carpeta.

    Returns:
        str: Un mensaje con la información del archivo o carpeta.
    """
    if not os.path.exists(ruta):
        return f"ERROR: Ruta no encontrada: {ruta}"
    stat = os.stat(ruta)
    modificado = datetime.datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    size = stat.st_size
    size_str = f"{size} bytes" if size < 1024 else f"{round(size/1024/1024, 2)} MB"
    tipo = "Carpeta" if os.path.isdir(ruta) else "Archivo"
    return f"Info de {ruta}:\nTipo: {tipo}\nTamanio: {size_str}\nModificado: {modificado}"

def ejecutar(accion, texto):
    """
    Ejecuta una acción según el texto ingresado.

    Args:
        accion (str): La acción a realizar.
        texto (str): El texto ingresado.

    Returns:
        str: Un mensaje con el resultado de la acción.
    """
    palabras = texto.split()
    t = texto.lower()

    if "listar" in t or "ver" in t or "mostrar" in t:
        ruta = palabras[-1] if len(palabras) > 1 else "C:/"
        return listar(ruta)

    elif "buscar" in t:
        if len(palabras) >= 3:
            patron = palabras[-2]
            ruta = palabras[-1]
        else:
            return "ERROR: Uso: explorar buscar patron C:/ruta"
        return buscar(ruta, patron)

    elif "crear carpeta" in t:
        ruta = palabras[-1]
        return crear_carpeta(ruta)

    elif "copiar" in t:
        if len(palabras) >= 3:
            return copiar(palabras[-2], palabras[-1])
        return "ERROR: Uso: explorar copiar origen destino"

    elif "mover" in t:
        if len(palabras) >= 3:
            return mover(palabras[-2], palabras[-1])
        return "ERROR: Uso: explorar mover origen destino"

    elif "leer" in t:
        if len(palabras) >= 2:
            ruta = palabras[-1]
            return leer(ruta)
        return "ERROR: Uso: explorar leer C:/ruta"

    elif "info" in t:
        if len(palabras) >= 2:
            ruta = palabras[-1]
            return info(ruta)
        return "ERROR: Uso: explorar info C:/ruta"

    else:
        return "ERROR: Acción no reconocida."