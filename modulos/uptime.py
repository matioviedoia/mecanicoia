import logging
import platform
import psutil
import time
import os

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Palabras clave reconocidas
PALABRAS_CLAVE_RECONOCIDAS = ["uptime", "tiempo", "corriendo"]

class Sistema:
    def __init__(self):
        self.boot_time = None

    def obtener_boot_time(self) -> float:
        """Obtiene el tiempo de arranque del sistema"""
        if self.boot_time is None:
            try:
                self.boot_time = psutil.boot_time()
            except Exception as e:
                logging.error(f"Error al obtener el tiempo de arranque: {str(e)}")
        return self.boot_time

    def calcular_uptime(self) -> str:
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
        if any(palabra in texto.lower() for palabra in PALABRAS_CLAVE_RECONOCIDAS):
            try:
                uptime = self.calcular_uptime()
                if uptime is not None:
                    logging.info(f"El sistema lleva {uptime} en ejecución")
            except Exception as e:
                logging.error(f"Error al ejecutar la acción: {str(e)}")
        else:
            logging.info("Acción no reconocida")

def obtener_sistema_operativo():
    """Obtiene el sistema operativo actual"""
    return platform.system()

def obtener_boot_time():
    """Obtiene el tiempo de arranque del sistema"""
    try:
        boot_time = psutil.boot_time()
        return boot_time
    except Exception as e:
        logging.error(f"Error al obtener el tiempo de arranque: {str(e)}")
        return None

def calcular_uptime():
    """Calcula el tiempo de actividad del sistema"""
    boot_time = obtener_boot_time()
    if boot_time is not None:
        uptime = time.time() - boot_time
        return uptime
    else:
        return None

def obtener_uptime_en_horas(uptime):
    """Convierte el uptime a horas, minutos y segundos"""
    if uptime is not None:
        horas = int(uptime // 3600)
        minutos = int((uptime % 3600) // 60)
        segundos = int(uptime % 60)
        return f"{horas} horas, {minutos} minutos y {segundos} segundos"
    else:
        return None

def main():
    sistema = Sistema()
    texto = "¿Cuánto tiempo lleva el sistema en ejecución?"
    sistema.ejecutar(texto)

if __name__ == "__main__":
    main()