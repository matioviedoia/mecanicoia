import os
import ast
import importlib

BASE = "C:/IA/AGENTE/MECANICO"

def extraer_codigo(texto):
    if "```python" in texto:
        inicio = texto.find("```python") + 9
        fin = texto.find("```", inicio)
        if fin > inicio:
            return texto[inicio:fin].strip()
    if "```" in texto:
        inicio = texto.find("```") + 3
        fin = texto.find("```", inicio)
        if fin > inicio:
            return texto[inicio:fin].strip()
    return texto.strip()

def validar_python(codigo):
    try:
        ast.parse(codigo)
        return True, "OK"
    except SyntaxError as e:
        return False, f"SyntaxError linea {e.lineno}: {e.msg}"

def generar_modulo(descripcion, nombre, preguntar_fn):
    log = []
    log.append(f"Generando modulo: {nombre}")
    prompt = (
        "Sos un experto en Python. Crea un modulo Python completo segun esta descripcion.\n"
        "REGLAS CRITICAS:\n"
        "1. El modulo DEBE tener una funcion llamada ejecutar(accion, texto) al final.\n"
        "2. La funcion ejecutar interpreta el texto y llama a las funciones del modulo.\n"
        "3. El modulo debe tener una variable KEYWORDS con lista de palabras clave.\n"
        "4. Usa solo librerias de Python estandar o muy comunes (requests, os, json, etc).\n"
        "5. Maneja todos los errores con try/except.\n"
        "6. Responde SOLO con el codigo Python entre triple backticks.\n\n"
        f"Descripcion del modulo: {descripcion}\n\n"
        "Devolvé SOLO el codigo Python completo:"
    )
    from config import APIS
    apis_orden = ["groq", "gemini", "cerebras", "zai", "ollama"]
    apis_activas = [a for a in apis_orden if a in APIS and APIS[a]["activa"] and (APIS[a]["key"] or a == "ollama")]
    codigo_nuevo = None
    api_usada = None
    for api in apis_activas:
        try:
            respuesta = preguntar_fn(prompt, api=api)
            codigo = extraer_codigo(respuesta)
            if not codigo:
                continue
            valido, msg = validar_python(codigo)
            if not valido:
                log.append(f"  {api}: codigo invalido - {msg}")
                continue
            if "def ejecutar(" not in codigo:
                log.append(f"  {api}: falta funcion ejecutar")
                continue
            codigo_nuevo = codigo
            api_usada = api
            break
        except Exception as e:
            log.append(f"  {api}: error - {e}")
            continue
    if not codigo_nuevo:
        return "\n".join(log) + "\nERROR: Ninguna API pudo generar el modulo"
    nombre_archivo = nombre.lower().replace(" ", "_").replace("-", "_")
    if not nombre_archivo.endswith(".py"):
        nombre_archivo += ".py"
    ruta = os.path.join(BASE, "modulos", nombre_archivo)
    if os.path.exists(ruta):
        return f"ERROR: El modulo {nombre_archivo} ya existe. Usa otro nombre."
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(codigo_nuevo)
    log.append(f"Codigo valido generado por {api_usada}")
    log.append(f"Modulo guardado: {ruta}")
    log.append(f"Lineas: {len(codigo_nuevo.splitlines())}")
    log.append("OK Modulo generado exitosamente")
    log.append(f"Reinicia MECANICO para cargar el modulo {nombre_archivo}")
    return "\n".join(log)

def ejecutar(accion, texto):
    partes = texto.split(" como ", 1)
    if len(partes) < 2:
        partes = texto.split(" llamado ", 1)
    if len(partes) < 2:
        return "ERROR: Uso: generar modulo que hace X como nombre_modulo"
    descripcion = partes[0].replace("generar ", "").strip()
    nombre = partes[1].strip()
    from mecanico import preguntar
    return generar_modulo(descripcion, nombre, preguntar)
