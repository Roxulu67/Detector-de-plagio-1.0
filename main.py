import os
import random
import pandas as pd  # Importar pandas
from src.generar_documentos import generar_texto_aleatorio
from src.preprocesar import preprocesar_documentos
from src.tabla_hash import TablaHash
from src.similitud import calcular_similitud  # Cambiado a calcular_similitud
from src.ordenar import merge_sort
from src.mostrar_resultados import guardar_resultados
from src.graficar_similitudes import graficar_similitudes  
from src.bloom_filter import BloomFilter  # Importar la nueva función
from src.guardar_similitudes import guardar_similitudes  # Importar la nueva función

def main():
    # Paso 1: Generar documentos
    carpeta_documentos = 'documentos'
    os.makedirs(carpeta_documentos, exist_ok=True)

    for i in range(1, 101):
        nombre_archivo = f'documento_{i}.txt'
        ruta_archivo = os.path.join(carpeta_documentos, nombre_archivo)
        contenido = generar_texto_aleatorio(longitud=random.randint(50, 200))
        with open(ruta_archivo, 'w') as archivo:
            archivo.write(contenido)

    print("Se han generado 100 documentos en la carpeta 'documentos'.")

    # Paso 2: Preprocesar documentos
    documentos_tokenizados = preprocesar_documentos(carpeta_documentos)

    # Paso 3: Crear tabla hash y Bloom Filter
    tabla_hash = TablaHash()
    bloom_filter = BloomFilter(size=1000, hash_count=5)

    similitudes = {}
    documentos = list(documentos_tokenizados.keys())
    for i in range(len(documentos)):
        for j in range(i + 1, len(documentos)):
            # Cambiar a calcular_similitud
            sim = calcular_similitud(documentos_tokenizados[documentos[i]], documentos_tokenizados[documentos[j]], metodo='jaccard')
            similitudes[(documentos[i], documentos[j])] = sim

    # Paso 4: Ordenar y mostrar resultados
    lista_similitudes = list(similitudes.items())
    merge_sort(lista_similitudes)

    # Mostrar los N documentos más similares en una tabla
    N = 5  # Cambia este valor según sea necesario
    print(f"Los {N} pares de documentos más similares son:")

    # Crear un DataFrame de pandas para mostrar los resultados
    resultados = []
    for i in range(min(N, len(lista_similitudes))):
        doc1, doc2 = lista_similitudes[i][0]
        similitud = lista_similitudes[i][1] * 100  # Convertir a porcentaje
        resultados.append({"Documento 1": doc1, "Documento 2": doc2, "Similitud (%)": f"{int(similitud)}"})  # Sin decimales

    df_resultados = pd.DataFrame(resultados)
    print(df_resultados)

    # Crear la carpeta 'resultados/graficos/' si no existe
    os.makedirs('resultados/graficos', exist_ok=True)

    # Crear la carpeta 'resultados/' si no existe
    os.makedirs('resultados', exist_ok=True)

    # Guardar resultados en un archivo de texto en formato tabla
    guardar_resultados(lista_similitudes)
    graficar_similitudes(lista_similitudes[:N])  # Pasar solo los N pares más similares

    # Guardar similitudes en un archivo de texto en la carpeta 'resultados'
    print("Guardando similitudes en 'resultados/top_n.txt'...")  # Verificación
    guardar_similitudes(lista_similitudes, N)  # Llamar a la nueva función

    print("Resultados guardados y gráfico generado.")
    print("Similitudes guardadas en 'resultados/top_n.txt'.")

if __name__ == "__main__":
    main()
