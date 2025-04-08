import math

def calcular_similitud_jaccard(doc1, doc2):
    """
    Calcula la similitud de Jaccard entre dos documentos.
    
    :param doc1: Lista de palabras del primer documento.
    :param doc2: Lista de palabras del segundo documento.
    :return: Similitud de Jaccard como un valor entre 0 y 1.
    """
    conjunto1 = set(doc1)
    conjunto2 = set(doc2)
    interseccion = len(conjunto1.intersection(conjunto2))
    union = len(conjunto1.union(conjunto2))
    
    if union == 0:
        return 0.0  # Evitar división por cero
    return interseccion / union

def calcular_similitud_coseno(doc1, doc2):
    """
    Calcula la similitud coseno entre dos documentos.
    
    :param doc1: Lista de palabras del primer documento.
    :param doc2: Lista de palabras del segundo documento.
    :return: Similitud coseno como un valor entre 0 y 1.
    """
    # Crear un conjunto de todas las palabras
    palabras = set(doc1).union(set(doc2))
    
    # Crear vectores de frecuencia de palabras
    vector1 = [doc1.count(palabra) for palabra in palabras]
    vector2 = [doc2.count(palabra) for palabra in palabras]
    
    # Calcular el producto punto y las magnitudes
    producto_punto = sum(a * b for a, b in zip(vector1, vector2))
    magnitud1 = math.sqrt(sum(a ** 2 for a in vector1))
    magnitud2 = math.sqrt(sum(b ** 2 for b in vector2))
    
    if magnitud1 == 0 or magnitud2 == 0:
        return 0.0  # Evitar división por cero
    return producto_punto / (magnitud1 * magnitud2)

def calcular_similitud(doc1, doc2, metodo='jaccard'):
    """
    Calcula la similitud entre dos documentos utilizando el método especificado.
    
    :param doc1: Lista de palabras del primer documento.
    :param doc2: Lista de palabras del segundo documento.
    :param metodo: Método de similitud a utilizar ('jaccard' o 'coseno').
    :return: Valor de similitud entre 0 y 1.
    """
    if metodo == 'jaccard':
        return calcular_similitud_jaccard(doc1, doc2)
    elif metodo == 'coseno':
        return calcular_similitud_coseno(doc1, doc2)
    else:
        raise ValueError("Método de similitud no reconocido. Usa 'jaccard' o 'coseno'.")