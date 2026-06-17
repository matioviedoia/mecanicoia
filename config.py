# ============================================
# MECANICO IA - Configuracion central
# ============================================
import os
from dotenv import load_dotenv

load_dotenv("C:/IA/MECANICO/.env")

RUTAS = {
    "workspace":  "C:/IA/MECANICO/workspace",
    "proyectos":  "C:/IA/MECANICO/proyectos",
    "sesiones":   "C:/IA/MECANICO/memoria/sesiones",
    "errores":    "C:/IA/MECANICO/memoria/errores",
    "backups":    "C:/IA/MECANICO/memoria/backups",
    "modulos":    "C:/IA/MECANICO/modulos",
}

APIS = {
    "groq":   {"key": os.getenv("GROQ_API_KEY"),    "activa": True,  "modelo": "llama-3.3-70b-versatile"},
    "gemini": {"key": os.getenv("GEMINI_API_KEY"),  "activa": True,  "modelo": "gemini-2.0-flash"},
    "ollama": {"key": None,                           "activa": True,  "modelo": "gemma3:4b",  "url": "http://localhost:11434"},
}

MODOS = {
    "auto":   "MECANICO trabaja solo sin pedir confirmacion",
    "manual": "MECANICO pide confirmacion antes de cada accion",
    "mixto":  "MECANICO decide segun la complejidad",
}

MODO_ACTUAL = "manual"
GITHUB_REPO = os.getenv("GITHUB_REPO")
