import os
import json
import shutil
import datetime
import ast

BASE = "C:/IA/AGENTE/MECANICO"

# ============================================
# MECANICO - Modulo Autoeditor con IA
# ============================================

def crear_directorio(ruta):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)

def hacer_backup(archivo):
    ruta = os.path.join(BASE, archivo) if not os.path.isabs(archivo) else archivo
    if not os.path.isfile(ruta):
        return None
    fecha = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = os.path.join(BASE, "memoria/backups", os.path.basename(ruta) + f".backup_{fecha}")
    crear_directorio(backup)
    shutil.copy2(ruta, backup)
    return f"Backup: {backup}"

def validar_python(codigo):
    try:
        ast.parse(codigo)
        return True, "Codigo valido"
    except SyntaxError as e:
        return False, f"Error de sintaxis linea {e.lineno}: {e.msg}"

def leer_archivo(archivo):
    ruta = os.path.join(BASE, archivo) if not os.path.isabs(archivo) else archivo
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None
    except Exception as e:
        return None

def escribir_archivo(archivo, contenido):
    ruta = os.path.join(BASE, archivo) if not os.path.isabs(archivo) else archivo
    crear_directorio(ruta)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)
    return f"OK Archivo guardado: {ruta}"

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

def ejecutar_instruccion(json_str):
    try:
        instruccion = json.loads(json_str)
    except json.JSONDecodeError as e:
        return f"ERROR: JSON invalido: {e}"

    log = []
    accion = instruccion.get("accion")
    archivo = instruccion.get("archivo", "")
    contenido = instruccion.get("contenido", "")
    backup = instruccion.get("backup", True)
    descripcion = instruccion.get("descripcion", "")

    if backup and archivo:
        b = hacer_backup(archivo)
        if b:
            log.append(b)

    if accion in ["crear_modulo", "crear_archivo"]:
        if archivo.endswith(".py"):
            valido, msg = validar_python(contenido)
            log.append(msg)
            if not valido:
                return "\n".join(log)
        resultado = escribir_archivo(archivo, contenido)
        log.append(resultado)

    elif accion == "leer_archivo":
        contenido_leido = leer_archivo(archivo)
        if contenido_leido:
            return f"Contenido de {archivo}:\n{contenido_leido}"
        return f"ERROR: No encontrado: {archivo}"

    elif accion == "modificar_con_ia":
        contenido_actual = leer_archivo(archivo)
        if not contenido_actual:
            return f"ERROR: Archivo no encontrado: {archivo}"
        try:
            from mecanico import preguntar
            prompt = (
                "Sos un experto en Python. Modifica este archivo segun la instruccion.\n"
                f"Instruccion: {descripcion}\n"
                "Devolvé SOLO el codigo Python completo y modificado entre triple backticks.\n"
                "No agregues explicaciones.\n\n"
                f"Archivo actual:\n```python\n{contenido_actual}\n```\n\n"
                "Devolvé SOLO el codigo modificado:"
            )
            respuesta = preguntar(prompt)
            codigo_nuevo = extraer_codigo(respuesta)
            if not codigo_nuevo:
                return "ERROR: La IA no devolvio codigo"
            if archivo.endswith(".py"):
                valido, msg = validar_python(codigo_nuevo)
                if not valido:
                    return f"ERROR: Codigo invalido: {msg}"
                log.append("Codigo valido")
            resultado = escribir_archivo(archivo, codigo_nuevo)
            log.append(resultado)
        except Exception as e:
            return f"ERROR: {e}"

    log.append("OK Instruccion ejecutada correctamente")
    return "\n".join(log)

def ejecutar(accion, texto):
    inicio = texto.find("{")
    fin = texto.rfind("}") + 1
    if inicio == -1 or fin == 0:
        return "ERROR: No encontre un JSON valido"
    return ejecutar_instruccion(texto[inicio:fin])
