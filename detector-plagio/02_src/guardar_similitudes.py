def guardar_similitudes(similitudes, n, ruta='resultados/top_n.txt'):
    """
    Guarda las similitudes en un archivo de texto en formato tabular.

    :param similitudes: Lista de tuplas con los pares de documentos y su similitud.
    :param n: Número de pares a guardar.
    :param ruta: Ruta del archivo donde se guardarán las similitudes.
    """
    with open(ruta, 'w') as f:
        # Escribir encabezados
        f.write("Documento 1\t\t| Documento 2\t\t| Similitud (%)\n")
        f.write("-" * 60 + "\n")  # Línea de separación
        for i in range(min(n, len(similitudes))):  # Asegúrate de que solo se guarden los primeros N
            doc1, doc2 = similitudes[i][0]
            similitud = similitudes[i][1] * 100  # Convertir a porcentaje
            # Escribir cada fila con formato alineado
            f.write(f"{doc1.ljust(20)} | {doc2.ljust(20)} | {int(similitud)}\n")  # Escribir cada fila