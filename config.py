# ============================================
# MECANICO IA - Configuracion central
# ============================================
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

# Define constant variables
RUTAS = {
    "workspace":  os.path.join(os.path.dirname(__file__), "workspace"),
    "proyectos":  os.path.join(os.path.dirname(__file__), "proyectos"),
    "sesiones":   os.path.join(os.path.dirname(__file__), "memoria", "sesiones"),
    "errores":    os.path.join(os.path.dirname(__file__), "memoria", "errores"),
    "backups":    os.path.join(os.path.dirname(__file__), "memoria", "backups"),
    "modulos":    os.path.join(os.path.dirname(__file__), "modulos"),
}

APIS = {
    "groq":     {"key": os.getenv("GROQ_API_KEY"),     "activa": True,  "modelo": "llama-3.3-70b-versatile"},
    "gemini":   {"key": os.getenv("GEMINI_API_KEY"),   "activa": True,  "modelo": "gemini-2.5-flash"},
    "ollama":   {"key": None,                           "activa": True,  "modelo": "gemma3:4b", "url": "http://localhost:11434"},
    "cerebras": {"key": os.getenv("CEREBRAS_API_KEY"), "activa": True, "modelo": "gpt-oss-120b"},
    "nvidia": {"key": os.getenv("NVIDIA_API_KEY"), "activa": True, "modelo": "nvidia/nemotron-3-super-120b"},
    "zai": {"key": os.getenv("ZAI_API_KEY"), "activa": True, "modelo": "glm-4.7-flash"},
}

MODOS = {
    "auto":   "MECANICO trabaja solo sin pedir confirmacion",
    "manual": "MECANICO pide confirmacion antes de cada accion",
    "mixto":  "MECANICO decide segun la complejidad",
}

MODO_ACTUAL = "manual"
GITHUB_REPO = os.getenv("GITHUB_REPO")

BASE = os.path.dirname(__file__)