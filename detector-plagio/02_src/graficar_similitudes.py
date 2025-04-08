import matplotlib.pyplot as plt
import networkx as nx

def graficar_similitudes(lista_similitudes):
    """
    Función para graficar las similitudes entre los N pares de documentos más similares.
    
    :param lista_similitudes: Lista de tuplas que contienen los pares de documentos y su similitud.
    """
    # Crear un grafo
    G = nx.Graph()

    # Agregar nodos y aristas para cada par de documentos
    for (doc1, doc2), similitud in lista_similitudes:
        G.add_node(doc1)
        G.add_node(doc2)
        G.add_edge(doc1, doc2, weight=similitud * 100)  # Conectar los nodos del mismo par

    # Configurar el tamaño de la figura
    plt.figure(figsize=(14, 10))  # Tamaño de la figura

    # Dibujar el grafo
    pos = nx.spring_layout(G, k=1.5, iterations=50)  # Posiciones para todos los nodos
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=2000, alpha=0.7)

    # Dibujar aristas
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='gray')

    # Dibujar etiquetas de nodos
    nx.draw_networkx_labels(G, pos, font_size=12, font_color='black')

    # Dibujar etiquetas de aristas (similitud)
    edge_labels = {(doc1, doc2): f"{int(similitud * 100)}%" for (doc1, doc2), similitud in lista_similitudes}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10)

    # Configurar el fondo
    plt.title("Similitudes entre Documentos", fontsize=16)
    plt.axis('off')  # Ocultar ejes
    plt.grid(False)  # Desactivar la cuadrícula

    # Guardar el gráfico
    plt.savefig('resultados/graficos/similitudes.png', format='png', bbox_inches='tight')
    plt.clf()  # Limpiar la figura para evitar superposiciones en futuros gráficos