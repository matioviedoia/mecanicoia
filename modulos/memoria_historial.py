import os
import logging
from datetime import datetime

# Configura el logging
logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Variable KEYWORDS con lista de palabras clave
KEYWORDS = ["registrar", "ver", "historial"]

# Constante global para la ruta del historial
HISTORIAL_PATH = "C:/IA/AGENTE/MECANICO/memoria/historial.log"

def registrar_evento(accion, detalle):
    """
    Registra un evento en el historial.log
    """
    try:
        # Crea el directorio si no existe
        os.makedirs(os.path.dirname(HISTORIAL_PATH), exist_ok=True)
        
        # Escribe la fecha, hora, accion y detalle en el archivo
        with open(HISTORIAL_PATH, "a", encoding='utf-8') as archivo:
            fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            archivo.write(f"{fecha_hora} - {accion} - {detalle}\n")
    except Exception as e:
        logging.error(f"Error al registrar evento: {e}")

def ver_historial():
    """
    Lee las ultimas 20 lineas del historial.log
    """
    try:
        # Verifica si el archivo historial.log existe
        if os.path.exists(HISTORIAL_PATH):
            # Lee las ultimas 20 lineas del archivo
            with open(HISTORIAL_PATH, "r", encoding='utf-8') as archivo:
                lineas = archivo.readlines()
                ultimas_lineas = lineas[-20:]
                return "".join(ultimas_lineas)
        else:
            return "No hay historial registrado"
    except Exception as e:
        logging.error(f"Error al ver historial: {e}")

def ejecutar(accion, texto):
    try:
        t = texto.lower()
        if "registrar" in t:
            partes = texto.split("registrar", 1)
            detalle = partes[1].strip() if len(partes) > 1 else texto
            registrar_evento("registro", detalle)
            return f"Evento registrado: {detalle}"
        else:
            return ver_historial()
    except Exception as e:
        logging.error(f"Error al ejecutar accion: {e}")
        return f"Error al ejecutar accion: {e}"

# Ejemplo de uso
if __name__ == "__main__":
    print(ejecutar("registrar", "cambio de aceite"))
    print(ejecutar("ver", ""))