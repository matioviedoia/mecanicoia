import pyperclip
import json

# Lista de palabras clave para el modulo
KEYWORDS = ['copiar', 'portapapeles', 'clipboard']

def copiar_a_portapapeles(texto):
    """
    Copia el contenido al portapapeles de Windows.
    
    Args:
        texto (str): El texto a copiar.
    
    Returns:
        None
    """
    try:
        pyperclip.copy(texto)
        print("Texto copiado al portapapeles con éxito.")
    except Exception as e:
        print(f"Error al copiar texto al portapapeles: {str(e)}")

def ejecutar(accion, texto):
    """
    Interpreta el texto y llama a las funciones del modulo.
    
    Args:
        accion (str): El nombre del trigger del modulo (no se utiliza).
        texto (str): El texto a interpretar.
    
    Returns:
        None
    """
    try:
        # Buscar palabras clave en el texto
        if 'copiar' in texto.lower() or 'portapapeles' in texto.lower() or 'clipboard' in texto.lower():
            # Extraer el texto a copiar del mensaje
            texto_a_copiar = texto.split(' ', 1)[1] if len(texto.split(' ', 1)) > 1 else ''
            copiar_a_portapapeles(texto_a_copiar)
        else:
            print("No se encontraron palabras clave en el texto.")
    except Exception as e:
        print(f"Error al interpretar el texto: {str(e)}")