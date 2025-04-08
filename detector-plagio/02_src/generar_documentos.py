import os
import random
import string

def generar_texto_aleatorio(longitud=100):
    """
    Genera un texto aleatorio de una longitud específica.

    Args:
        longitud (int): Longitud del texto aleatorio a generar.

    Returns:
        str: Texto aleatorio generado.
    """
    return ''.join(random.choices(string.ascii_lowercase + ' ', k=longitud))

# Crear carpeta para los documentos
carpeta_documentos = 'documentos'
os.makedirs(carpeta_documentos, exist_ok=True)

# Generar 100 documentos
for i in range(1, 101):
    nombre_archivo = f'documento_{i}.txt'
    ruta_archivo = os.path.join(carpeta_documentos, nombre_archivo)
    contenido = generar_texto_aleatorio(longitud=random.randint(50, 200))
    with open(ruta_archivo, 'w') as archivo:
        archivo.write(contenido)

print("Se han generado 100 documentos en la carpeta 'documentos'.")