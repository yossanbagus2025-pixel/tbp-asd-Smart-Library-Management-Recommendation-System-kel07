import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from data_structures.stack import Stack


class TestStack(unittest.TestCase):
    def test_push_pop(self):
        s = Stack()
        s.push("Tx1")
        s.push("Tx2")
        self.assertEqual(s.peek(), "Tx2")
        self.assertEqual(s.pop(), "Tx2")
        self.assertEqual(s.pop(), "Tx1")
        self.assertTrue(s.is_empty())


if __name__ == "__main__":
    unittest.main()
