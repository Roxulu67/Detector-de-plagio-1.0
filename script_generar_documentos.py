import os
import random

def generar_texto_aleatorio(longitud=100):
    """Genera un texto aleatorio de una longitud dada."""
    palabras = ['lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit', 
                'sed', 'do', 'eiusmod', 'tempor', 'incididunt', 'ut', 'labore', 'et', 'dolore', 
                'magna', 'aliqua', 'ut', 'enim', 'ad', 'minim', 'veniam', 'quis', 'nostrud', 
                'exercitation', 'ullamco', 'laboris', 'nisi', 'ut', 'aliquip', 'ex', 'ea', 
                'commodo', 'consequat', 'duis', 'aute', 'irure', 'dolor', 'in', 'reprehenderit', 
                'in', 'voluptate', 'velit', 'esse', 'cillum', 'dolore', 'eu', 'fugiat', 
                'nulla', 'pariatur', 'excepteur', 'sint', 'occaecat', 'cupidatat', 'non', 
                'proident', 'sunt', 'in', 'culpa', 'qui', 'officia', 'deserunt', 'mollit', 
                'anim', 'id', 'est', 'laborum']
    
    texto = ' '.join(random.choices(palabras, k=longitud))
    return texto

def crear_documentos(cantidad=10, carpeta='documentos'):
    """Crea una cantidad específica de documentos de texto con contenido aleatorio."""
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)  # Crea la carpeta si no existe

    for i in range(cantidad):
        nombre_archivo = f"documento_{i + 1}.txt"
        ruta_archivo = os.path.join(carpeta, nombre_archivo)
        
        # Generar un texto aleatorio de longitud 500
        texto = generar_texto_aleatorio(longitud=500)
        
        # Escribir el texto en el archivo
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(texto)

    print(f"{cantidad} documentos han sido creados en la carpeta '{carpeta}'.")

if __name__ == "__main__":
    crear_documentos()