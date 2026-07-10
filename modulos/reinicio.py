import os
import sys
import subprocess

# Lista de palabras clave
KEYWORDS = ["reiniciar", "restart"]

def reiniciar():
    """
    Reinicia el proceso actual y vuelve a lanzar python mecanico.py
    """
    try:
        # Obtenemos el nombre del archivo actual
        archivo_actual = sys.argv[0]
        
        # Ejecutamos el comando para reiniciar el proceso
        subprocess.Popen([sys.executable, archivo_actual])
        
        # Matamos el proceso actual
        os._exit(0)
    except Exception as e:
        print(f"Error al reiniciar: {str(e)}")

def ejecutar(accion, texto):
    """
    Interpreta el texto y llama a las funciones del módulo
    """
    try:
        # Convertimos el texto a minúsculas
        texto = texto.lower()
        
        # Verificamos si el texto contiene alguna palabra clave
        for keyword in KEYWORDS:
            if keyword in texto:
                # Llamamos a la función de reiniciar
                reiniciar()
                break
    except Exception as e:
        print(f"Error al ejecutar la acción: {str(e)}")

# Llamamos a la función ejecutar
if __name__ == "__main__":
    # Simulamos una llamada a la función ejecutar
    ejecutar("reiniciar", "reiniciar el proceso")