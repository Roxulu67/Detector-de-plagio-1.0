import os
import re

def preprocesar_documentos(carpeta):
    """
    Preprocesa los documentos en la carpeta especificada, limpiando y tokenizando el texto.

    Args:
        carpeta (str): Ruta de la carpeta que contiene los documentos.

    Returns:
        dict: Un diccionario donde las claves son los nombres de los archivos y los valores son listas de n-gramas.
    """
    documentos_tokenizados = {}
    
    for archivo in os.listdir(carpeta):
        if archivo.endswith('.txt'):
            with open(os.path.join(carpeta, archivo), 'r') as f:
                texto = f.read()
                # Limpiar texto: eliminar signos de puntuación y convertir a minúsculas
                texto_limpio = re.sub(r'[^\w\s]', '', texto.lower())
                # Tokenizar en n-gramas (bi-gramas en este caso)
                n_gramas = [texto_limpio[i:i+2] for i in range(len(texto_limpio)-1)]
                documentos_tokenizados[archivo] = n_gramas
    
    return documentos_tokenizados

if __name__ == "__main__":
    documentos_tokenizados = preprocesar_documentos('documentos')
    print("Documentos preprocesados y tokenizados.")