def merge_sort(similitudes):
    """
    Ordena una lista de similitudes utilizando el algoritmo Merge Sort.

    Args:
        similitudes (list): Lista de tuplas que contienen pares de documentos y sus similitudes.
    """
    if len(similitudes) > 1:
        mid = len(similitudes) // 2
        izquierda = similitudes[:mid]
        derecha = similitudes[mid:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i][1] > derecha[j][1]:
                similitudes[k] = izquierda[i]
                i += 1
            else:
                similitudes[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            similitudes[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            similitudes[k] = derecha[j]
            j += 1
            k += 1

if __name__ == "__main__":
    from similitud import calcular_similitud_jaccard
    from preprocesar import preprocesar_documentos
    documentos_tokenizados = preprocesar_documentos('documentos')
    
    similitudes = {}
    documentos = list(documentos_tokenizados.keys())
    for i in range(len(documentos)):
        for j in range(i + 1, len(documentos)):
            sim = calcular_similitud_jaccard(documentos_tokenizados[documentos[i]], documentos_tokenizados[documentos[j]])
            similitudes[(documentos[i], documentos[j])] = sim

    lista_similitudes = list(similitudes.items())
    merge_sort(lista_similitudes)
    print("Similitudes ordenadas.")