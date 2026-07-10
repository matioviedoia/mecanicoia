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
        reiniciar()
        return "Reiniciando MECANICO..."
    except Exception as e:
        return f"Error al ejecutar la acción: {str(e)}"

# Llamamos a la función ejecutar
if __name__ == "__main__":
    # Simulamos una llamada a la función ejecutar
    ejecutar("reiniciar", "reiniciar el proceso")
