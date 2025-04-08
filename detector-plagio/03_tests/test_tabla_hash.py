import unittest
from src.tabla_hash import TablaHash

class TestTablaHash(unittest.TestCase):
    def test_agregar_y_obtener(self):
        tabla = TablaHash()
        tabla.agregar('n-grama1')
        tabla.agregar('n-grama1')
        tabla.agregar('n-grama2')

        # Verifica que la frecuencia del n-grama1 sea 2
        self.assertEqual(tabla.obtener('n-grama1'), 2)
        # Verifica que la frecuencia del n-grama2 sea 1
        self.assertEqual(tabla.obtener('n-grama2'), 1)
        # Verifica que un n-grama no existente retorne 0
        self.assertEqual(tabla.obtener('n-grama3'), 0)

if __name__ == '__main__':
    unittest.main()