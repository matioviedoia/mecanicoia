import logging
import platform
import psutil
import time
from typing import Optional

# Configuración de logging
LOG_LEVEL = logging.INFO
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(
    level=LOG_LEVEL,
    format=LOG_FORMAT,
    datefmt=LOG_DATE_FORMAT
)

class Sistema:
    def __init__(self) -> None:
        self.boot_time: Optional[float] = None

    def obtener_boot_time(self) -> Optional[float]:
        """Obtiene el tiempo de arranque del sistema"""
        if self.boot_time is None:
            try:
                self.boot_time = psutil.boot_time()
            except psutil.Error as e:
                logging.error(f"Error al obtener el tiempo de arranque: {str(e)}")
        return self.boot_time

    def calcular_uptime(self) -> Optional[str]:
        """Calcula el tiempo de actividad del sistema"""
        boot_time = self.obtener_boot_time()
        if boot_time is not None:
            uptime = time.time() - boot_time
            horas = int(uptime // 3600)
            minutos = int((uptime % 3600) // 60)
            segundos = int(uptime % 60)
            return f"{horas} horas, {minutos} minutos y {segundos} segundos"
        else:
            return None

    def ejecutar(self, texto: str) -> None:
        """Interpreta el texto y llama a las funciones del módulo"""
        if not texto:
            logging.error("Texto de entrada vacío")
            return

        if any(palabra in texto.lower() for palabra in ["uptime", "tiempo", "corriendo"]):
            try:
                uptime = self.calcular_uptime()
                if uptime is not None:
                    logging.info(f"El sistema lleva {uptime} en ejecución")
            except Exception as e:
                logging.error(f"Error al ejecutar la acción: {str(e)}")
        else:
            logging.info("Acción no reconocida")

def main() -> None:
    sistema = Sistema()
    texto = "¿Cuánto tiempo lleva el sistema en ejecución?"
    sistema.ejecutar(texto)

if __name__ == "__main__":
    main()