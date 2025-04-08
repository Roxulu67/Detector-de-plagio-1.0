import matplotlib.pyplot as plt
import networkx as nx

def graficar_similitudes(lista_similitudes):
    """
    Función para graficar las similitudes entre los N pares de documentos más similares.
    
    :param lista_similitudes: Lista de tuplas que contienen los pares de documentos y su similitud.
    """
    # Crear un grafo
    G = nx.Graph()

    # Agregar nodos y aristas solo para los N pares más similares
    for (doc1, doc2), similitud in lista_similitudes:
        G.add_edge(doc1, doc2, weight=similitud * 100)  # Convertir a porcentaje

    # Dibujar el grafo
    pos = nx.spring_layout(G)  # Posiciones para todos los nodos
    weights = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={k: f"{int(v)}%" for k, v in weights.items()})  # Mostrar como porcentaje

    # Guardar el gráfico
    plt.savefig('resultados/graficos/similitudes.png')
    plt.clf()  # Limpiar la figura para evitar superposiciones en futuros gráficos

def guardar_resultados(lista_similitudes):
    """
    Función para guardar los resultados de similitud en un archivo.
    
    :param lista_similitudes: Lista de tuplas que contienen los pares de documentos y su similitud.
    """
    # Guardar los resultados en un archivo de texto
    with open('resultados/similitudes.txt', 'w') as f:
        for (doc1, doc2), similitud in lista_similitudes:
            f.write(f"{doc1} y {doc2}: {int(similitud * 100)}%\n")  # Guardar como porcentaje