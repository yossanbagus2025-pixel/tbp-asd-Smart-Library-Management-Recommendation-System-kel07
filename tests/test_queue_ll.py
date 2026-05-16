import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from data_structures.queue_ll import Queue


class TestQueueLL(unittest.TestCase):
    def test_enqueue_dequeue(self):
        q = Queue()
        q.enqueue("UserA")
        q.enqueue("UserB")
        self.assertEqual(len(q), 2)
        self.assertEqual(q.dequeue(), "UserA")
        self.assertEqual(q.dequeue(), "UserB")
        self.assertTrue(q.is_empty())


if __name__ == "__main__":
    unittest.main()
