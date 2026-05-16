from data_structures.linked_list import LLNode


class Stack:
    def __init__(self):
        """Big-O: O(1)"""
        self.top = None
        self._size = 0

    def push(self, data):
        """Big-O: O(1)."""
        new = LLNode(data)
        new.next = self.top
        self.top = new
        self._size += 1

    def pop(self):
        """Big-O: O(1)."""
        if self.is_empty():
            raise TypeError("Data Kosong")
        removed = self.top.data
        self.top = self.top.next
        self._size -= 1
        return removed

    def peek(self):
        """Big-O: O(1)"""
        return self.top.data if self.top else None

    def is_empty(self):
        """Big-O: O(1)"""
        return self._size == 0

    def to_list(self):
        """Big-O: O(n)."""
        res = []
        curr = self.top
        while curr:
            res.append(curr.data)
            curr = curr.next
        return res
