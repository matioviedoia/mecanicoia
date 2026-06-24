# Este módulo analiza código Python en busca de errores, advertencias y problemas de rendimiento, 
# y ofrece opciones para analizar archivos y proyectos utilizando técnicas de inteligencia artificial.

import os
import ast
import json

BASE = "C:/IA/AGENTE/MECANICO"

def leer_archivo(ruta: str) -> str:
    """Lee el contenido de un archivo."""
    try:
        with open(ruta, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception as e:
        return f"ERROR: {str(e)}"

def analizar_python(ruta: str) -> str:
    """Analiza un archivo Python en busca de errores y advertencias."""
    codigo = leer_archivo(ruta)
    if codigo.startswith("ERROR"):
        return codigo
    errores = []
    advertencias = []
    try:
        ast.parse(codigo)
    except SyntaxError as e:
        errores.append(f"SyntaxError en línea {e.lineno}: {e.msg}")
    lineas = codigo.split("\n")
    for i, linea in enumerate(lineas, 1):
        if "except:" in linea and "except Exception" not in linea:
            advertencias.append(f"Línea {i}: except demasiado amplio")
        if len(linea) > 120:
            advertencias.append(f"Línea {i}: línea muy larga ({len(linea)} chars)")
        if "print(" in linea and "#" not in linea:
            advertencias.append(f"Línea {i}: print() encontrado (puede ser debug)")
    resumen = f"Archivo: {ruta}\n"
    resumen += f"Líneas: {len(lineas)}\n"
    resumen += f"Errores: {len(errores)}\n"
    resumen += f"Advertencias: {len(advertencias)}\n"
    if errores:
        resumen += "\nERRORES:\n" + "\n".join(errores)
    if advertencias:
        resumen += "\nADVERTENCIAS:\n" + "\n".join(advertencias[:10])
    return resumen

def analizar_proyecto(carpeta: str) -> str:
    """Analiza un proyecto en busca de errores en los archivos Python."""
    if not os.path.exists(carpeta):
        return f"ERROR: Carpeta no encontrada: {carpeta}"
    reporte = []
    total_errores = 0
    total_archivos = 0
    for raiz, dirs, archivos in os.walk(carpeta):
        dirs[:] = [d for d in dirs if d not in ["__pycache__", ".git", "node_modules"]]
        for archivo in archivos:
            if archivo.endswith(".py"):
                ruta = os.path.join(raiz, archivo)
                total_archivos += 1
                analisis = analizar_python(ruta)
                if "Errores: 0" not in analisis and not analisis.startswith("ERROR"):
                    total_errores += 1
                    reporte.append(analisis)
    resumen = f"ANÁLISIS DE PROYECTO: {carpeta}\n"
    resumen += f"Archivos Python analizados: {total_archivos}\n"
    resumen += f"Archivos con errores: {total_errores}\n"
    resumen += "=" * 40 + "\n"
    if reporte:
        resumen += "\n".join(reporte)
    else:
        resumen += "No se encontraron errores de sintaxis."
    return resumen

def analizar_con_ia(ruta: str, preguntar_fn) -> str:
    """Analiza un archivo con la ayuda de la inteligencia artificial."""
    codigo = leer_archivo(ruta)
    if codigo.startswith("ERROR"):
        return codigo
    prompt = f"""Analizá este código y encontrá:
1. Errores o bugs
2. Problemas de rendimiento
3. Mejoras posibles
4. Código duplicado

Archivo: {ruta}
Código:
{codigo[:3000]}

Respondé en español, sé conciso y directo."""
    return preguntar_fn(prompt)

def ejecutar(accion: str, texto: str) -> str:
    """Ejecuta la acción solicitada."""
    t = texto.lower()
    palabras = texto.split()

    if "proyecto" in t:
        carpeta = palabras[-1] if len(palabras) > 1 else BASE
        return analizar_proyecto(carpeta)
    elif "ia" in t or "inteligente" in t:
        ruta = palabras[-1] if len(palabras) > 1 else ""
        if not ruta or not os.path.exists(ruta):
            return "ERROR: Especifica la ruta del archivo. Ej: analizar ia C:/ruta/archivo.py"
        from mecanico import preguntar
        return analizar_con_ia(ruta, preguntar)
    elif "archivo" in t:
        ruta = palabras[-1] if len(palabras) > 1 else ""
        if not ruta or not os.path.exists(ruta):
            return "ERROR: Especifica la ruta del archivo. Ej: analizar archivo C:/ruta/archivo.py"
        return analizar_python(ruta)
    else:
        return "ERROR: Acción no válida. Ej: analizar proyecto, analizar archivo, analizar ia"