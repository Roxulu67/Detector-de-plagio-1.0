import unittest
from src.preprocesar import preprocesar_documentos

class TestPreprocesar(unittest.TestCase):
    def test_preprocesar_documentos(self):
        # Crea un archivo de prueba
        with open('documentos/test.txt', 'w') as f:
            f.write("Este es un texto de prueba para verificar el preprocesamiento.")

        # Llama a la función de preprocesamiento
        resultado = preprocesar_documentos('documentos')

        # Verifica que el resultado contenga el archivo de prueba
        self.assertIn('test.txt', resultado)
        # Verifica que el n-grama esperado esté presente
        self.assertIn('es', resultado['test.txt'])
        self.assertIn('un', resultado['test.txt'])

if __name__ == '__main__':
    unittest.main()