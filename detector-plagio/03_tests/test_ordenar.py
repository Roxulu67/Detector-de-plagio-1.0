import unittest
from src.ordenar import merge_sort

class TestOrdenar(unittest.TestCase):
    def test_merge_sort(self):
        similitudes = [(('doc1.txt', 'doc2.txt'), 0.5), (('doc3.txt', 'doc4.txt'), 0.8), (('doc5.txt', 'doc6.txt'), 0.3)]
        merge_sort(similitudes)

        # Verifica que el primer elemento sea el de mayor similitud
        self.assertEqual(similitudes[0], (('doc3.txt', 'doc4.txt'), 0.8))
        # Verifica que el último elemento sea el de menor similitud
        self.assertEqual(similitudes[2], (('doc5.txt', 'doc6.txt'), 0.3))

if __name__ == '__main__':
    unittest.main()