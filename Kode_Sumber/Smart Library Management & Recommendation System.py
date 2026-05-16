import numpy as np, time, random
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Tuple

np.random.seed(13)
random.seed(13)
KATEGORI = ['Fiksi', 'Sains', 'Teknik', 'Sejarah', 'Seni']
STATUS = {'TERSEDIA': 0, 'DIPINJAM': 1, 'DIPESAN': 2}

@dataclass
class Buku:
    isbn: str # kunci BST
    judul: str
    pengarang: str
    kategori: str
    status: int = 0 # 0=TERSEDIA, 1=DIPINJAM, 2=DIPESAN
    pinjam_count: int = 0

@dataclass
class Peminjaman:
    transaksi_id: int
    anggota_id: str
    isbn: str
    tgl_pinjam: float # time.time()
    durasi_hari: int = 14

class LLNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    """FIFO Queue untuk antrian pemesanan buku."""
    def __init__(self):
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
        return self._size == 0

    def __len__(self):
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
class Stack:
    def __init__(self):
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
        return self.top.data if self.top else None

    def is_empty(self):
        return self._size == 0

    def to_list(self):
        res = []
        curr = self.top
        while curr:
            res.append(curr.data)
            curr = curr.next
        return res

class BSTNode:
    def __init__(self, buku):
        self.buku = buku
        self.left = None
        self.right = None

class BSTKatalog:
    def __init__(self):
        self.root = None

    def insert(self, buku):
        """Big-O: O(log n) rata-rata. Kunci = buku.isbn."""
        if self.root is None:
            self.root = BSTNode(buku)
        else:
            return self.insert_recursive(self.root, buku)

    def insert_recursive(self, node, buku):
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
        node = self.search_node(isbn)
        return node.buku if node else None

    def update_status(self, isbn, status):
        node = self.search_node(isbn)
        if node is None:
            return False
        node.buku.status = status
        return True

    def inorder(self):
        result = []
        self.inorder_recursive(self.root, result)
        return result

    def inorder_recursive(self, node, result):
        if node is None:
            return
        self.inorder_recursive(node.left, result)
        result.append(node.buku)
        self.inorder_recursive(node.right, result)

    def delete(self, key):
        """Hapus buku dari BST berdasarkan ISBN"""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
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
        while node.left:
            node = node.left
        return node


class GraphRekBuku:
    """Graf tak-berarah berbobot: edge (A,B,w) = ko-pinjam frekuensi w."""
    def __init__(self):
        self.adj = {} # isbn -> [(isbn, freq)]

    def add_copinjam(self, isbn_a, isbn_b):
        """Tambah atau naikkan bobot edge. Big-O: O(deg)."""
        pass # TODO: implementasikan

    def rekomendasikan(self, isbn, max_hop=2):
        """BFS hingga max_hop. Big-O: O(V+E)."""
        pass # TODO: gunakan Queue Linked List sendiri

def generate_koleksi(n=80):
    kata = ['Algoritma','Jaringan','Python','Data','Digital',
        'Sistem','Kontrol','Sinyal','Elektronika','Fisika']
    return [Buku(f'ISBN-{i:04d}', f'{random.choice(kata)} Vol.{i}',
        f'Penulis-{random.randint(1,20)}', random.choice(KATEGORI))
        for i in range(1, n+1)]

def main():
    bst = BSTKatalog()
    antrian_pesan = {} # isbn -> Queue
    riwayat_global = Stack()
    graf_rek = GraphRekBuku()
    tx_counter = 0
    for buku in generate_koleksi(80):
        bst.insert(buku)
    antrian_pesan[buku.isbn] = Queue()
    print('Smart Library System Ketik BANTUAN untuk daftar perintah')
# TODO: implementasikan loop CLI
# Perintah: CARI_BUKU <isbn>, PINJAM <nim> <isbn>, KEMBALIKAN <isbn>
# PESAN <nim> <isbn>, BATALKAN_TERAKHIR, REKOMENDASI <isbn>
# KATALOG, ANTRIAN <isbn>, LAPORAN_BULAN, KELUAR
if __name__ == '__main__':
    main()
