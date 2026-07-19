import logging
import psutil
import time

# Configuración de logging
LOG_LEVEL = logging.INFO
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(
    level=LOG_LEVEL,
    format=LOG_FORMAT,
    datefmt=LOG_DATE_FORMAT
)

KEYWORDS = ["uptime", "tiempo", "corriendo"]

def calcular_uptime() -> str:
    """Calcula el tiempo de actividad del sistema"""
    boot_time = psutil.boot_time()
    uptime = time.time() - boot_time
    horas = int(uptime // 3600)
    minutos = int((uptime % 3600) // 60)
    segundos = int(uptime % 60)
    return f"{horas} horas, {minutos} minutos y {segundos} segundos"

def ejecutar(accion: str, texto: str) -> str:
    """Interpreta el texto y llama a las funciones del módulo"""
    if not texto:
        logging.error("Texto de entrada vacío")
        return "Error: Texto de entrada vacío"

    if any(palabra in texto.lower() for palabra in KEYWORDS):
        try:
            uptime = calcular_uptime()
            return f"El sistema lleva {uptime} en ejecución"
        except Exception as e:
            logging.error(f"Error al ejecutar la acción: {str(e)}")
            return f"Error: {str(e)}"
    else:
        return "Acción no reconocida"

def main() -> None:
    texto = "¿Cuánto tiempo lleva el sistema en ejecución?"
    resultado = ejecutar("accion", texto)
    logging.info(resultado)

if __name__ == "__main__":
    main()