import os
import datetime
from os import path

# Lista de palabras clave
KEYWORDS = ["registrar", "evento", "ver", "historial"]

def registrar_evento(accion, detalle):
    """
    Registra un evento en el historial.
    
    :param accion: La accion realizada
    :param detalle: El detalle del evento
    """
    try:
        # Obtener la fecha y hora actuales
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Abrir el archivo de historial en modo append
        with open("historial.log", "a") as archivo:
            # Escribir la linea con la fecha y hora, accion y detalle
            archivo.write(f"{fecha_hora} - {accion}: {detalle}\n")
    except Exception as e:
        print(f"Error al registrar evento: {e}")

def ver_historial():
    """
    Lee las ultimas 20 lineas del historial.
    
    :return: Las ultimas 20 lineas del historial
    """
    try:
        # Verificar si el archivo de historial existe
        if not path.exists("historial.log"):
            return []
        
        # Abrir el archivo de historial en modo read
        with open("historial.log", "r") as archivo:
            # Leer todas las lineas del archivo
            lineas = archivo.readlines()
            
            # Devolver las ultimas 20 lineas
            return lineas[-20:]
    except Exception as e:
        print(f"Error al ver historial: {e}")

def ejecutar(accion, texto):
    """
    Interpreta el texto y llama a las funciones del modulo.
    
    :param accion: La accion a realizar
    :param texto: El texto a interpretar
    """
    try:
        # Interpretar el texto
        if accion == "registrar":
            # Registrar un evento
            detalle = texto
            registrar_evento(accion, detalle)
        elif accion == "ver":
            # Ver el historial
            historial = ver_historial()
            for linea in historial:
                print(linea.strip())
        else:
            print("Accion no reconocida")
    except Exception as e:
        print(f"Error al ejecutar accion: {e}")