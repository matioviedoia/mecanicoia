import json
import re

KEYWORDS = []

MODULOS_DISPONIBLES = {
    "analizar": "analizar <ruta_archivo.py> - analiza UN archivo Python. analizar proyecto <ruta_carpeta> - analiza TODOS los archivos de una carpeta (usar este para carpetas/proyectos). analizar ia <ruta_archivo.py> - analisis profundo con IA de un archivo",
    "reparar": "reparar <ruta> - corrige bugs y errores en un archivo",
    "mejorar": "mejorar <ruta> - aplica mejoras de calidad y arquitectura",
    "revertir": "revertir <archivo> - restaura el ultimo backup. revertir listar <archivo> para ver backups",
    "explorar": "explorar listar <ruta> / explorar buscar <patron> <ruta> / explorar leer <ruta> / explorar info <ruta>",
    "leer": "leer <ruta> y <pregunta> - lee un archivo y responde una pregunta sobre el con IA",
    "git": "git estado / git push / git historial - operaciones de control de versiones",
    "generar": "generar <descripcion> como <nombre> - crea un modulo nuevo desde cero",
    "github": "github leer <url> - analiza un repo de GitHub e implementa si es chico",
    "scout": "scout <tema> - busca repos de GitHub utiles",
    "tokens": "tokens / tokens historial / tokens limites - consumo de las APIs",
    "creador_proyecto": "creador_proyecto descripcion del proyecto nombre_del_proyecto - crea un PROYECTO NUEVO EXTERNO completo desde cero como un bot script o app en la carpeta proyectos_generados, usar este para pedidos de crear bots scripts o programas nuevos, es diferente de generar que solo crea modulos internos de MECANICO"
}

def intentar_modelos_nvidia(prompt, preguntar_fn):
    try:
        from config import NVIDIA_FALLBACK
    except ImportError:
        NVIDIA_FALLBACK = ["moonshotai/kimi-k2.6"]
    import os
    from dotenv import load_dotenv
    load_dotenv("C:/IA/AGENTE/MECANICO/.env")
    key = os.getenv("NVIDIA_API_KEY")
    import requests
    for modelo in NVIDIA_FALLBACK:
        try:
            headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
            body = {"model": modelo, "messages": [{"role": "user", "content": prompt}], "max_tokens": 2000, "stream": False}
            r = requests.post("https://integrate.api.nvidia.com/v1/chat/completions", headers=headers, json=body, timeout=60)
            data = r.json()
            contenido = data["choices"][0]["message"]["content"]
            if "<think>" in contenido and "</think>" in contenido:
                contenido = contenido.split("</think>")[-1].strip()
            return contenido, modelo
        except Exception:
            continue
    try:
        return preguntar_fn(prompt), "fallback-auto"
    except Exception:
        return None, None

def armar_plan(pedido_usuario, preguntar_fn):
    lista_modulos = "\n".join([f"- {k}: {v}" for k, v in MODULOS_DISPONIBLES.items()])
    prompt = (
        "Sos el orquestador de MECANICO, un agente que analiza y repara codigo Python.\n"
        "Tenes disponibles estos comandos exactos:\n\n"
        f"{lista_modulos}\n\n"
        "Los proyectos del usuario estan en C:/IA/AGENTE/. Si menciona un nombre de proyecto sin ruta completa,\n"
        "asumi que esta en C:/IA/AGENTE/NOMBRE_PROYECTO (ej: MAT.ONE esta en C:/IA/AGENTE/MAT.ONE).\n\n"
        f"El usuario pidio: {pedido_usuario}\n\n"
        "Arma un plan de pasos usando SOLO los comandos de arriba, con sus rutas y parametros reales.\n"
        "IMPORTANTE: si la ruta es una carpeta (no termina en .py ni otra extension), usa 'analizar proyecto <ruta>', NUNCA 'analizar <ruta>' solo para carpetas.\n"
        "Respondé SOLO con un JSON valido con este formato exacto, nada mas:\n"
        '{"pasos": ["comando1 parametro1", "comando2 parametro2"], "explicacion": "breve resumen de lo que se va a hacer"}\n\n'
        "Si no sabes exactamente que archivo reparar, SIEMPRE agrega primero explorar listar carpeta para ver los archivos disponibles, luego repara el archivo correcto.\n"
        "Para proyectos Node.js el archivo principal suele ser server.js o index.js. Para Python suele ser main.py o __init__.py.\n"
        "Si el pedido es ambiguo o falta informacion critica, pedila en el campo explicacion y deja pasos vacio.\n"
        "Responde SOLO el JSON, sin texto antes ni despues, sin backticks."
    )
    respuesta, modelo_usado = intentar_modelos_nvidia(prompt, preguntar_fn)
    if not respuesta:
        return None, "ERROR: Ninguna IA pudo armar el plan", None
    match = re.search(r'\{.*\}', respuesta, re.DOTALL)
    if not match:
        return None, f"ERROR: No se genero un plan valido.\nRespuesta: {respuesta[:300]}", None
    try:
        plan = json.loads(match.group())
        return plan.get("pasos", []), plan.get("explicacion", ""), modelo_usado
    except json.JSONDecodeError as e:
        return None, f"ERROR: JSON invalido del plan: {e}", None

def ejecutar_plan(pasos, modulos_cargados):
    resultados = []
    for i, paso in enumerate(pasos, 1):
        paso_lower = paso.lower().strip()
        resultado = None
        try:
            if paso_lower.startswith("reparar") and "reparador" in modulos_cargados:
                resultado = modulos_cargados["reparador"].ejecutar("reparar", paso)
            elif paso_lower.startswith("mejorar") and "reparador" in modulos_cargados:
                resultado = modulos_cargados["reparador"].ejecutar("mejorar", paso)
            elif paso_lower.startswith("revertir") and "revertir" in modulos_cargados:
                resultado = modulos_cargados["revertir"].ejecutar("revertir", paso)
            elif paso_lower.startswith("analizar") and "analizador" in modulos_cargados:
                resultado = modulos_cargados["analizador"].ejecutar("analizar", paso)
            elif paso_lower.startswith("explorar") and "explorador" in modulos_cargados:
                resultado = modulos_cargados["explorador"].ejecutar("explorar", paso)
            elif paso_lower.startswith("leer") and "lector_contexto" in modulos_cargados:
                resultado = modulos_cargados["lector_contexto"].ejecutar("leer", paso)
            elif paso_lower.startswith("git") and "git_manager" in modulos_cargados:
                resultado = modulos_cargados["git_manager"].ejecutar("git", paso)
            elif paso_lower.startswith("generar") and "generador" in modulos_cargados:
                resultado = modulos_cargados["generador"].ejecutar("generar", paso)
            elif paso_lower.startswith("github") and "github_reader" in modulos_cargados:
                resultado = modulos_cargados["github_reader"].ejecutar("github", paso)
            elif paso_lower.startswith("scout") and "github_scout" in modulos_cargados:
                resultado = modulos_cargados["github_scout"].ejecutar("scout", paso)
            elif paso_lower.startswith("tokens") and "token_monitor" in modulos_cargados:
                resultado = modulos_cargados["token_monitor"].ejecutar("tokens", paso)
            elif paso_lower.startswith("creador_proyecto") and "creador_proyecto" in modulos_cargados:
                resultado = modulos_cargados["creador_proyecto"].ejecutar("creador_proyecto", paso)
            else:
                resultado = f"No se reconoce el comando: {paso}"
        except Exception as e:
            resultado = f"ERROR ejecutando '{paso}': {e}"
        resultados.append(f"[Paso {i}/{len(pasos)}] {paso}\n{resultado}\n")
    return "\n".join(resultados)