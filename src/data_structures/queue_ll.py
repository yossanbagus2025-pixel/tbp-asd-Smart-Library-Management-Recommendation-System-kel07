from data_structures.linked_list import LLNode


class Queue:
    """FIFO Queue untuk antrian pemesanan buku."""

    def __init__(self):
        """Big-O: O(1)"""
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, data):
        """Big-O: O(1)."""
        new = LLNode(data)
        if self.is_empty():
            self.head = new
        else:
            self.tail.next = new
        self.tail = new
        self._size += 1

    def dequeue(self):
        """Big-O: O(1)."""
        if self.is_empty():
            raise TypeError("Data Kosong")
        removed = self.head.data
        self.head = self.head.next
        self._size -= 1
        if self.is_empty():
            self.tail = None
        return removed

    def is_empty(self):
        """Big-O: O(1)"""
        return self._size == 0

    def __len__(self):
        """Big-O: O(1)"""
        return self._size

    def delete_by_value(self, x):
        """Big-O: O(n)"""
        if self.head is None:
            return False
        if self.head.data == x:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return True
        prev = self.head
        cur = self.head.next
        while cur:
            if cur.data == x:
                prev.next = cur.next
                if cur.next is None:
                    self.tail = prev
                self._size -= 1
                return True
            prev, cur = cur, cur.next
        return False
