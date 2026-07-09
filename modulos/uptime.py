import os
import time
import platform
import psutil

KEYWORDS = ["uptime", "tiempo", "corriendo"]

def obtener_sistema_operativo():
    """Obtiene el sistema operativo actual"""
    return platform.system()

def obtener_boot_time():
    """Obtiene el tiempo de arranque del sistema"""
    try:
        boot_time = psutil.boot_time()
        return boot_time
    except Exception as e:
        print(f"Error al obtener el tiempo de arranque: {str(e)}")
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

def ejecutar(accion, texto):
    """Interpreta el texto y llama a las funciones del modulo"""
    palabras = texto.lower().split()
    if "uptime" in texto or "tiempo" in texto or "corriendo" in texto:
        try:
            uptime = calcular_uptime()
            uptime_en_horas = obtener_uptime_en_horas(uptime)
            if uptime_en_horas is not None:
                print(f"El sistema lleva {uptime_en_horas} en ejecución")
            else:
                print("No se pudo calcular el uptime")
        except Exception as e:
            print(f"Error al ejecutar la acción: {str(e)}")
    else:
        print("Acción no reconocida")

# Ejemplo de uso:
# ejecutar("calcular", "Cuanto tiempo lleva corriendo el sistema")