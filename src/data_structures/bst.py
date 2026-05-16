class BSTNode:
    def __init__(self, buku):
        """Big-O: O(1)"""
        self.buku = buku
        self.left = None
        self.right = None


class BSTKatalog:
    def __init__(self):
        """Big-O: O(1)"""
        self.root = None

    def insert(self, buku):
        """
        Big-O Average: O(log n)
        Big-O Worst  : O(n)
        """
        if self.root is None:
            self.root = BSTNode(buku)
        else:
            return self.insert_recursive(self.root, buku)

    def insert_recursive(self, node, buku):
        """
        Big-O Average: O(log n)
        Big-O Worst  : O(n)
        """
        if buku.isbn < node.buku.isbn:
            if node.left is None:
                node.left = BSTNode(buku)
            else:
                return self.insert_recursive(node.left, buku)
        elif buku.isbn > node.buku.isbn:
            if node.right is None:
                node.right = BSTNode(buku)
            else:
                return self.insert_recursive(node.right, buku)

    def search_node(self, isbn):
        """
        Big-O Average: O(log n)
        Big-O Worst  : O(n)
        """
        node = self.root
        while node:
            if isbn == node.buku.isbn:
                return node
            elif isbn < node.buku.isbn:
                node = node.left
            else:
                node = node.right
        return None

    def search(self, isbn):
        """
        Big-O Average: O(log n)
        Big-O Worst  : O(n)
        """
        node = self.search_node(isbn)
        return node.buku if node else None

    def update_status(self, isbn, status):
        """
        Big-O Average: O(log n)
        Big-O Worst  : O(n)
        """
        node = self.search_node(isbn)
        if node is None:
            return False
        node.buku.status = status
        return True

    def inorder(self):
        """Big-O: O(n)"""
        result = []
        self.inorder_recursive(self.root, result)
        return result

    def inorder_recursive(self, node, result):
        """Big-O: O(n)"""
        if node is None:
            return
        self.inorder_recursive(node.left, result)
        result.append(node.buku)
        self.inorder_recursive(node.right, result)

    def delete(self, key):
        """
        Big-O Average: O(log n)
        Big-O Worst  : O(n)
        """
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        """
        Big-O Average: O(log n)
        Big-O Worst  : O(n)
        """
        if node is None:
            return None
        if key < node.buku.isbn:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.buku.isbn:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._find_min(node.right)
                node.buku = successor.buku
                node.right = self._delete_recursive(node.right, successor.buku.isbn)
        return node

    def _find_min(self, node):
        """
        Big-O Average: O(log n)
        Big-O Worst  : O(n)
        """
        while node.left:
            node = node.left
        return node
