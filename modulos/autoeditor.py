import os
import json
import shutil
import datetime
import ast

BASE = "C:/IA/AGENTE/MECANICO"

def hacer_backup(archivo):
    ruta = os.path.join(BASE, archivo)
    if os.path.exists(ruta):
        fecha = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup = os.path.join(BASE, "memoria/backups", os.path.basename(archivo) + f".backup_{fecha}")
        shutil.copy2(ruta, backup)
        return f"Backup: {backup}"
    return None

def validar_python(codigo):
    try:
        ast.parse(codigo)
        return True, "Codigo valido"
    except SyntaxError as e:
        return False, f"Error de sintaxis: {e}"

def crear_archivo(archivo, contenido):
    ruta = os.path.join(BASE, archivo)
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)
    return f"OK Archivo creado: {ruta}"

def modificar_archivo(archivo, buscar, agregar=None, reemplazar=None):
    ruta = os.path.join(BASE, archivo)
    if not os.path.exists(ruta):
        return f"ERROR: Archivo no encontrado: {ruta}"
    with open(ruta, "r", encoding="utf-8") as f:
        contenido = f.read()
    if buscar not in contenido:
        return f"ERROR: Texto no encontrado en {archivo}"
    if reemplazar is not None:
        contenido = contenido.replace(buscar, reemplazar, 1)
    elif agregar is not None:
        contenido = contenido.replace(buscar, buscar + "\n" + agregar, 1)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)
    return f"OK Modificado: {ruta}"

def leer_archivo(archivo):
    ruta = os.path.join(BASE, archivo)
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as f:
            return f.read()
    return f"ERROR: Archivo no encontrado: {ruta}"

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
    modificaciones = instruccion.get("modificar", [])

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
        resultado = crear_archivo(archivo, contenido)
        log.append(resultado)

    elif accion == "leer_archivo":
        return leer_archivo(archivo)

    elif accion == "modificar_archivo":
        buscar = instruccion.get("buscar", "")
        agregar = instruccion.get("agregar", None)
        reemplazar = instruccion.get("reemplazar", None)
        resultado = modificar_archivo(archivo, buscar, agregar, reemplazar)
        log.append(resultado)

    for mod in modificaciones:
        arch = mod.get("archivo", "")
        if backup:
            b = hacer_backup(arch)
            if b:
                log.append(b)
        resultado = modificar_archivo(
            arch,
            mod.get("buscar", ""),
            mod.get("agregar", None),
            mod.get("reemplazar", None)
        )
        log.append(resultado)

    log.append("OK Instruccion ejecutada correctamente")
    return "\n".join(log)

def ejecutar(accion, texto):
    inicio = texto.find("{")
    fin = texto.rfind("}") + 1
    if inicio == -1 or fin == 0:
        return "ERROR: No encontre un JSON valido"
    return ejecutar_instruccion(texto[inicio:fin])
