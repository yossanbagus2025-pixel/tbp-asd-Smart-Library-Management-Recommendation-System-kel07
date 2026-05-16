import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from data_structures.graph import GraphRekBuku


class TestGraphRekBuku(unittest.TestCase):
    def test_add_copinjam_and_recommend(self):
        graph = GraphRekBuku()
        graph.add_copinjam("ISBN-0001", "ISBN-0002")
        rekomendasi = graph.rekomendasikan("ISBN-0001")
        self.assertTrue(len(rekomendasi) > 0)
        self.assertEqual(rekomendasi[0][0], "ISBN-0002")


if __name__ == "__main__":
    unittest.main()
