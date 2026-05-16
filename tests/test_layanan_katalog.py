import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from modules.layanan_katalog import LayananKatalog


class TestLayananKatalogModule(unittest.TestCase):
    def test_layanan_katalog_initialization(self):
        layanan = LayananKatalog()
        self.assertIsNone(layanan.bst.root)


if __name__ == "__main__":
    unittest.main()
