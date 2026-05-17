import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from data_structures.bst import BSTKatalog
from modules.layanan_models import Buku

class TestBSTKatalog(unittest.TestCase):
    def test_insert_and_search_tree(self):
        bst = BSTKatalog()
        b_test = Buku("ISBN-7777", "Test BST Book", "Author X", "Teknik")
        bst.insert(b_test)
        found = bst.search("ISBN-7777")
        self.assertIsNotNone(found)
        self.assertEqual(found.judul, "Test BST Book")


if __name__ == "__main__":
    unittest.main()
