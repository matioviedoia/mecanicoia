import subprocess
import json

KEYWORDS = ["buscar web", "buscar internet", "buscar en internet", "investigar", "verificar"]

def ejecutar_comando(comando):
    import os
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    try:
        resultado = subprocess.run(comando, capture_output=True, text=True, timeout=30, shell=True, encoding="utf-8", errors="ignore", env=env)
        return resultado.stdout.strip() if resultado.returncode == 0 else f"ERROR: {resultado.stderr.strip()}"
    except Exception as e:
        return f"ERROR: {e}"

def buscar(query, max_resultados=5):
    comando = f'zero-search "{query}" --json'
    salida = ejecutar_comando(comando)
    if salida.startswith("ERROR"):
        return salida
    try:
        data = json.loads(salida)
        sources = data.get("sources", [])
        texto = f"Resultados para '{query}':\n\n"
        for i, r in enumerate(sources[:max_resultados], 1):
            titulo = r.get("title", "Sin titulo")
            url = r.get("url", "")
            snippet = (r.get("snippet", ""))[:200]
            texto += f"{i}. {titulo}\n   {snippet}\n   {url}\n\n"
        if not sources:
            texto += "(sin fuentes encontradas)"
        return texto
    except Exception as e:
        return f"ERROR parseando: {e}\n{salida[:500]}"

def obtener_contexto(query):
    comando = f'zero-context "{query}"'
    return ejecutar_comando(comando)

def verificar(afirmacion):
    comando = f'zero-verify "{afirmacion}" --json'
    salida = ejecutar_comando(comando)
    if salida.startswith("ERROR"):
        return salida
    try:
        data = json.loads(salida)
        return json.dumps(data, indent=2, ensure_ascii=False)[:1500]
    except Exception:
        return salida[:1500]

def ejecutar(accion, texto):
    t = texto.lower()
    palabras = texto.split()
    if "verificar" in t:
        afirmacion = " ".join(palabras[1:])
        return verificar(afirmacion)
    elif "contexto" in t:
        query = " ".join(palabras[1:])
        return obtener_contexto(query)
    else:
        for kw in ["buscar web", "buscar internet", "buscar en internet", "investigar"]:
            texto = texto.replace(kw, "", 1) if kw in texto.lower() else texto
        query = texto.strip()
        if not query:
            return "ERROR: Especifica que buscar. Ej: buscar web python 3.13 novedades"
        return buscar(query)
