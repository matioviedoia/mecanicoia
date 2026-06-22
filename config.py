# ============================================
# MECANICO IA - Configuracion central
# ============================================
import os
from dotenv import load_dotenv

load_dotenv("C:/IA/AGENTE/MECANICO/.env")

RUTAS = {
    "workspace":  "C:/IA/AGENTE/MECANICO/workspace",
    "proyectos":  "C:/IA/AGENTE/MECANICO/proyectos",
    "sesiones":   "C:/IA/AGENTE/MECANICO/memoria/sesiones",
    "errores":    "C:/IA/AGENTE/MECANICO/memoria/errores",
    "backups":    "C:/IA/AGENTE/MECANICO/memoria/backups",
    "modulos":    "C:/IA/AGENTE/MECANICO/modulos",
}

APIS = {
    "groq":     {"key": os.getenv("GROQ_API_KEY"),     "activa": True,  "modelo": "llama-3.3-70b-versatile"},
    "gemini":   {"key": os.getenv("GEMINI_API_KEY"),   "activa": True,  "modelo": "gemini-2.5-flash"},
    "ollama":   {"key": None,                           "activa": True,  "modelo": "gemma3:4b", "url": "http://localhost:11434"},
    "cerebras": {"key": os.getenv("CEREBRAS_API_KEY"), "activa": True, "modelo": "gpt-oss-120b"},
    "zai": {"key": os.getenv("ZAI_API_KEY"), "activa": True, "modelo": "glm-4.7-flash"},
}

MODOS = {
    "auto":   "MECANICO trabaja solo sin pedir confirmacion",
    "manual": "MECANICO pide confirmacion antes de cada accion",
    "mixto":  "MECANICO decide segun la complejidad",
}

MODO_ACTUAL = "manual"
GITHUB_REPO = os.getenv("GITHUB_REPO")

BASE = "C:/IA/AGENTE/MECANICO"
