import unittest
from src.similitud import calcular_similitud_jaccard

class TestSimilitud(unittest.TestCase):
    def test_calcular_similitud_jaccard(self):
        doc1 = ['a', 'b', 'c']
        doc2 = ['b', 'c', 'd']
        doc3 = ['e', 'f', 'g']

        # Verifica que la similitud entre doc1 y doc2 sea 0.5
        self.assertEqual(calcular_similitud_jaccard(doc1, doc2), 0.5)
        # Verifica que la similitud entre doc1 y doc3 sea 0
        self.assertEqual(calcular_similitud_jaccard(doc1, doc3), 0)

if __name__ == '__main__':
    unittest.main()