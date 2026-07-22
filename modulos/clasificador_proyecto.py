import os
import json
import re

KEYWORDS = ['test', 'prueba', 'backup', 'old', 'copia', 'viejo', 'draft', 'temp']

def get_files(folder):
    """
    Obtiene la lista de archivos de código en una carpeta de manera recursiva,
    ignorando las carpetas __pycache__, .git, node_modules y venv.
    """
    files = []
    for root, dirs, filenames in os.walk(folder):
        for dir in dirs:
            if dir in ['__pycache__', '.git', 'node_modules', 'venv']:
                dirs.remove(dir)
        for filename in filenames:
            if filename.endswith(('.py', '.java', '.js', '.cpp', '.c', '.swift', '.php', '.ruby', '.go', '.kt', '.scala', '.vb', '.cs', '.twig', '.blade')):
                files.append(os.path.join(root, filename))
    return files

def classify_files(files, preguntar_fn):
    """
    Clasifica los archivos en activos o sospechosos según sus nombres.
    """
    salto_linea = "\n"
    prompt = f"Clasifica los siguientes archivos en activos y sospechosos:{salto_linea}{json.dumps([os.path.basename(file) for file in files])}{salto_linea}Responde SOLO con JSON valido sin texto adicional sin markdown en este formato exacto con las claves activos y sospechosos cada una con una lista de strings. No pongas ninguna explicacion antes ni despues del JSON."
    respuesta = preguntar_fn(prompt)
    with open('C:/IA/AGENTE/MECANICO/memoria/debug_clasificador.txt', 'w', encoding='utf-8') as archivo:
        archivo.write(respuesta)
    json_match = re.search(r"{.*}", respuesta, re.DOTALL)
    if json_match:
        return json.loads(json_match.group())
    else:
        return {'activos': [], 'sospechosos': []}

def ejecutar(accion, texto):
    """
    Interpreta el texto y llama a las funciones del módulo.
    """
    folder = None
    for palabra in texto.lower().split():
        if os.path.isdir(palabra):
            folder = palabra
            break
    if folder:
        files = get_files(folder)
        from mecanico import preguntar
        classifications = classify_files(files, preguntar)
        activos = classifications.get('activos', [])
        sospechosos = classifications.get('sospechosos', [])
        reporte = "Archivos activos:\n"
        for file in [os.path.basename(file) for file in files if os.path.basename(file) in activos]:
            reporte += file + "\n"
        reporte += "\nArchivos sospechosos:\n"
        for file in [os.path.basename(file) for file in files if os.path.basename(file) in sospechosos]:
            reporte += file + "\n"
        return reporte
    else:
        return "No se encontró una carpeta válida en el texto."