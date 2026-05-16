import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from data_structures.linked_list import LLNode


class TestLinkedListNode(unittest.TestCase):
    def test_node_initialization(self):
        node = LLNode("Data_Test")
        self.assertEqual(node.data, "Data_Test")
        self.assertIsNone(node.next)


if __name__ == "__main__":
    unittest.main()
