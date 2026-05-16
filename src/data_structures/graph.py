from data_structures.queue_ll import Queue


class GraphRekBuku:
    def __init__(self):
        """Big-O: O(1)"""
        self.adj = {}

    def add_vertex(self, isbn):
        """Big-O: O(1)"""
        if isbn not in self.adj:
            self.adj[isbn] = []

    def add_copinjam(self, isbn_a, isbn_b):
        """
        Big-O: O(deg(v))
        deg(v) = jumlah tetangga vertex
        """
        self.add_vertex(isbn_a)
        self.add_vertex(isbn_b)
        found = False
        for i, (isbn, freq) in enumerate(self.adj[isbn_a]):
            if isbn == isbn_b:
                self.adj[isbn_a][i] = (isbn, freq + 1)
                found = True
                break
        if not found:
            self.adj[isbn_a].append((isbn_b, 1))
        found = False
        for i, (isbn, freq) in enumerate(self.adj[isbn_b]):
            if isbn == isbn_a:
                self.adj[isbn_b][i] = (isbn, freq + 1)
                found = True
                break
        if not found:
            self.adj[isbn_b].append((isbn_a, 1))

    def rekomendasikan(self, isbn, max_hop=2):
        """Big-O: O(V + E)"""
        if isbn not in self.adj:
            return []
        visited = set([isbn])
        result = []
        queue = Queue()
        queue.enqueue((isbn, 0))
        while not queue.is_empty():
            current, hop = queue.dequeue()
            if hop >= max_hop:
                continue
            for tetangga, freq in self.adj[current]:
                if tetangga not in visited:
                    visited.add(tetangga)
                    result.append((tetangga, freq))
                    queue.enqueue((tetangga, hop + 1))
        return result
