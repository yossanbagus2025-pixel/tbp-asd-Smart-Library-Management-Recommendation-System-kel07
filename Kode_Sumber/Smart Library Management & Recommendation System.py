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
        pass # TODO: implementasikan
    def dequeue(self):
        """Big-O: O(1)."""
        pass # TODO: implementasikan
    def is_empty(self):
        return self._size == 0
    def __len__(self):
        return self._size
class Stack:
    def __init__(self):
        self.top = None
        self._size = 0
    def push(self, data):
        """Big-O: O(1)."""
        pass # TODO: implementasikan
    def pop(self):
        """Big-O: O(1)."""
        pass # TODO: implementasikan
    def peek(self):
        return self.top.data if self.top else None
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
        pass # TODO: implementasikan
    def search(self, isbn):
        """Big-O: O(log n) rata-rata."""
        pass # TODO: implementasikan
    def update_status(self, isbn, status):
        """Big-O: O(log n) rata-rata."""
        pass # TODO: cari node, update status
    def inorder(self):
        """Big-O: O(n). Kembalikan list Buku terurut ISBN."""
        pass # TODO: implementasikan
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
