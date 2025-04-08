class TablaHash:
    """
    Clase que implementa una tabla hash para almacenar n-gramas.

    Attributes:
        tabla (dict): Diccionario que almacena los n-gramas y sus frecuencias.
    """
    def __init__(self):
        self.tabla = {}

    def agregar(self, n_grama):
        """
        Agrega un n-grama a la tabla hash.

        Args:
            n_grama (str): El n-grama a agregar.
        """
        if n_grama in self.tabla:
            self.tabla[n_grama] += 1
        else:
            self.tabla[n_grama] = 1

    def obtener(self, n_grama):
        """
        Obtiene la frecuencia de un n-grama en la tabla hash.

        Args:
            n_grama (str): El n-grama a buscar.

        Returns:
            int: Frecuencia del n-grama.
        """
        return self.tabla.get(n_grama, 0)

if __name__ == "__main__":
    from preprocesar import preprocesar_documentos
    documentos_tokenizados = preprocesar_documentos('documentos')
    
    tabla_hash = TablaHash()
    for n_gramas in documentos_tokenizados.values():
        for n_grama in n_gramas:
            tabla_hash.agregar(n_grama)

    print("Tabla hash creada y n-gramas almacenados.")