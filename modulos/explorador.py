import os
import shutil
import datetime

def listar(ruta):
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
    try:
        os.makedirs(ruta, exist_ok=True)
        return f"OK Carpeta creada: {ruta}"
    except Exception as e:
        return f"ERROR: {e}"

def copiar(origen, destino):
    try:
        if os.path.isdir(origen):
            shutil.copytree(origen, destino)
        else:
            shutil.copy2(origen, destino)
        return f"OK Copiado: {origen} -> {destino}"
    except Exception as e:
        return f"ERROR: {e}"

def mover(origen, destino):
    try:
        shutil.move(origen, destino)
        return f"OK Movido: {origen} -> {destino}"
    except Exception as e:
        return f"ERROR: {e}"

def leer(ruta):
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
    if not os.path.exists(ruta):
        return f"ERROR: Ruta no encontrada: {ruta}"
    stat = os.stat(ruta)
    modificado = datetime.datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    size = stat.st_size
    size_str = f"{size} bytes" if size < 1024 else f"{round(size/1024/1024, 2)} MB"
    tipo = "Carpeta" if os.path.isdir(ruta) else "Archivo"
    return f"Info de {ruta}:\nTipo: {tipo}\nTamanio: {size_str}\nModificado: {modificado}"

def ejecutar(accion, texto):
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
        ruta = palabras[-1]
        return leer(ruta)

    elif "info" in t:
        ruta = palabras[-1]
        return info(ruta)

    else:
        ruta = palabras[-1] if len(palabras) > 1 else "C:/"
        return listar(ruta)
