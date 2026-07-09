import os
import json
import datetime

BASE = "C:/IA/AGENTE/MECANICO"
OUTPUT = "C:/IA/AGENTE/MECANICO/MASTER_CONTEXT2.md"

def leer_archivo(ruta):
    try:
        with open(ruta, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except:
        return ""

def generar_contexto():
    md = []
    md.append(f"# MASTER CONTEXT - MECANICO IA")
    md.append(f"Generado: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

    # Estructura
    md.append("## ESTRUCTURA")
    md.append("```")
    for raiz, dirs, archivos in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in ["__pycache__", ".git", "node_modules", "backups"]]
        nivel = raiz.replace(BASE, "").count(os.sep)
        indent = "  " * nivel
        md.append(f"{indent}{os.path.basename(raiz)}/")
        for archivo in archivos:
            md.append(f"{indent}  {archivo}")
    md.append("```\n")

    # Modulos
    md.append("## MODULOS")
    carpeta_modulos = os.path.join(BASE, "modulos")
    for archivo in sorted(os.listdir(carpeta_modulos)):
        if archivo.endswith(".py") and not archivo.startswith("_"):
            ruta = os.path.join(carpeta_modulos, archivo)
            contenido = leer_archivo(ruta)
            md.append(f"\n### {archivo}")
            md.append(f"```python\n{contenido[:2000]}\n```")

    # Config
    md.append("\n## CONFIG")
    md.append(f"```python\n{leer_archivo(os.path.join(BASE, 'config.py'))}\n```")

    # Mecanico principal (solo estructura)
    md.append("\n## MECANICO.PY - TRIGGERS ACTIVOS")
    mecanico = leer_archivo(os.path.join(BASE, "mecanico.py"))
    triggers = [l.strip() for l in mecanico.split("\n") if "startswith(" in l]
    for t in triggers:
        md.append(f"- {t}")

    # APIs disponibles
    md.append("\n## APIS CONFIGURADAS")
    md.append("- groq: llama-3.3-70b-versatile")
    md.append("- gemini: gemini-2.5-flash")
    md.append("- cerebras: gpt-oss-120b")
    md.append("- nvidia: moonshotai/kimi-k2.6 (fallback: mistral-large, nemotron, deepseek-v4, llama-3.3)")
    md.append("- zai: glm-4.7-flash")
    md.append("- ollama: gemma3:4b (local)")

    # Pendientes
    md.append("\n## PENDIENTES PROXIMA SESION")
    md.append("- Arreglar orquestador (devuelve None en pedidos complejos)")
    md.append("- Implementar Headoom MCP")
    md.append("- Implementar CodeBase Memory MCP")
    md.append("- Auto-reparacion y auto-mejora de MECANICO")
    md.append("- Estabilizar modo Auto (orquestador)")

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("\n".join(md))

    print(f"OK Contexto generado: {OUTPUT}")

generar_contexto()
