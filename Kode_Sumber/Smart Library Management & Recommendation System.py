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
    def __init__(self):
        self.adj = {}

    def add_vertex(self, isbn):
        if isbn not in self.adj:
            self.adj[isbn] = []

    def add_copinjam(self, isbn_a, isbn_b):
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

def generate_koleksi(n=80):
    kata = ['Algoritma','Jaringan','Python','Data','Digital',
        'Sistem','Kontrol','Sinyal','Elektronika','Fisika']
    return [Buku(f'ISBN-{i:04d}', f'{random.choice(kata)} Vol.{i}',
        f'Penulis-{random.randint(1,20)}', random.choice(KATEGORI))
        for i in range(1, n+1)]
def shell_sort_durasi(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap].durasi_hari < temp.durasi_hari:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


# --- MERGE SORT (FREKUENSI) ---
def merge_sort_frekuensi(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_frekuensi(arr[:mid])
    right = merge_sort_frekuensi(arr[mid:])
    return merge(left, right)


def merge(left, right):
    res = []
    while left and right:
        if left[0].pinjam_count >= right[0].pinjam_count:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    return res + left + right


def generate_koleksi(n=80):
    kata = [
        "Algoritma",
        "Jaringan",
        "Python",
        "Data",
        "Digital",
        "Sistem",
        "Kontrol",
        "Sinyal",
        "Elektronika",
        "Fisika",
    ]
    return [
        Buku(
            f"ISBN-{i:04d}",
            f"{random.choice(kata)} Vol.{i}",
            f"Penulis-{random.randint(1,20)}",
            random.choice(KATEGORI),
        )
        for i in range(1, n + 1)
    ]


def main():
    bst = BSTKatalog()
    antrian_pesan = {}  # isbn -> Queue
    riwayat_global = Stack()
    graf_rek = GraphRekBuku()
    tx_counter = 0
    riwayat_user = {}
    peminjaman_aktif = {}
    for buku in generate_koleksi(80):
        bst.insert(buku)
    print("Smart Library System Ketik BANTUAN untuk daftar perintah")
    while True:
        cmd = input("\n>>> ").strip().split()
        if len(cmd) == 0:
            continue
        perintah = cmd[0].upper()
        if perintah == "BANTUAN":
            print("\nDAFTAR PERINTAH:")
            print("  CARI_BUKU <isbn>")
            print("  PINJAM <anggota_id> <isbn>")
            print("  KEMBALIKAN <isbn>")
            print("  PESAN <anggota_id> <isbn>")
            print("  BATALKAN_TERAKHIR")
            print("  REKOMENDASI <isbn>")
            print("  KATALOG")
            print("  ANTRIAN <isbn>")
            print("  BATALKAN_PESANAN <anggota_id> <isbn>")
            print("  HAPUS_RUSAK <isbn>")
            print("  LAPORAN_BULAN")
            print("  KELUAR")
        elif perintah == "CARI_BUKU":
            if len(cmd) != 2:
                print("Format: CARI_BUKU <isbn>")
                continue
            isbn = cmd[1]
            buku = bst.search(isbn)
            if buku:
                print(f"\nISBN       : {buku.isbn}")
                print(f"Judul      : {buku.judul}")
                print(f"Pengarang  : {buku.pengarang}")
                print(f"Kategori   : {buku.kategori}")
                print(f"Status     : {buku.status}")
                if isbn in peminjaman_aktif:
                    trx = peminjaman_aktif[isbn]
                    print(f"Peminjam   : {trx.anggota_id}")
                    waktu = time.strftime(
                        "%d-%m-%Y %H:%M:%S", time.localtime(trx.tgl_pinjam)
                    )
                    print(f"Tgl Pinjam : {waktu}")
                    print(f"Durasi     : {trx.durasi_hari} hari")
            else:
                print("Buku tidak ditemukan")
            print("[Big-O: O(log n)]")
        elif perintah == "PINJAM":
            if len(cmd) != 3:
                print("Format: PINJAM <anggota_id> <isbn>")
                continue
            anggota_id = cmd[1]
            isbn = cmd[2]
            buku = bst.search(isbn)
            if buku is None:
                print("Buku tidak ditemukan")
                continue
            if buku.status != STATUS["TERSEDIA"]:
                print("Buku tidak tersedia")
                continue
            tx_counter += 1
            buku.pinjam_count += 1
            transaksi = Peminjaman(tx_counter, anggota_id, isbn, time.time())
            riwayat_global.push(("PINJAM", transaksi))
            peminjaman_aktif[isbn] = transaksi
            if anggota_id not in riwayat_user:
                riwayat_user[anggota_id] = []
            for buku_lama in riwayat_user[anggota_id]:
                graf_rek.add_copinjam(buku_lama, isbn)
            riwayat_user[anggota_id].append(isbn)
            bst.update_status(isbn, STATUS["DIPINJAM"])
            print(f"Buku {isbn} berhasil dipinjam")
            print("[Big-O: O(log n)]")
        elif perintah == "KEMBALIKAN":
            if len(cmd) != 2:
                print("Format: KEMBALIKAN <isbn>")
                continue
            isbn = cmd[1]
            buku = bst.search(isbn)
            if buku is None:
                print("Buku tidak ditemukan")
                continue
            if isbn in peminjaman_aktif:
                del peminjaman_aktif[isbn]
            if isbn in antrian_pesan and not antrian_pesan[isbn].is_empty():
                next_anggota_id = antrian_pesan[isbn].dequeue()
                if antrian_pesan[isbn].is_empty():
                    bst.update_status(isbn, STATUS["TERSEDIA"])
                else:
                    bst.update_status(isbn, STATUS["DIPESAN"])
                print(f"Buku {isbn} dialihkan ke antrian {next_anggota_id}")
            else:
                bst.update_status(isbn, STATUS["TERSEDIA"])
                print(f"Buku {isbn} dikembalikan")
            print("[Big-O: O(log n)]")
        elif perintah == "PESAN":
            if len(cmd) != 3:
                print("Format: PESAN <anggota_id> <isbn>")
                continue
            anggota_id = cmd[1]
            isbn = cmd[2]
            buku = bst.search(isbn)
            if buku is None:
                print("Buku tidak ditemukan")
            elif buku.status == STATUS["TERSEDIA"]:
                print("Buku masih tersedia, gunakan PINJAM")
            else:
                if isbn not in antrian_pesan:
                    antrian_pesan[isbn] = Queue()
                antrian_pesan[isbn].enqueue(anggota_id)
                bst.update_status(isbn, STATUS["DIPESAN"])
                print(f"{anggota_id} masuk antrian buku {isbn}")
            print("[Big-O: O(log n)]")
        elif perintah == "ANTRIAN":
            if len(cmd) != 2:
                print("Format: ANTRIAN <isbn>")
                continue
            isbn = cmd[1]
            if isbn not in antrian_pesan or antrian_pesan[isbn].is_empty():
                print("Tidak ada antrian")
            else:
                current = antrian_pesan[isbn].head
                print(f"Antrian buku {isbn}:")
                while current:
                    print(f"  - {current.data}")
                    current = current.next
            print("[Big-O: O(n)]")
        elif perintah == "REKOMENDASI":
            if len(cmd) != 2:
                print("Format: REKOMENDASI <isbn>")
                continue
            isbn = cmd[1]
            hasil = graf_rek.rekomendasikan(isbn)
            if len(hasil) == 0:
                print("Tidak ada rekomendasi")
            else:
                print(f"Rekomendasi untuk {isbn}:")
                for rekom, freq in hasil:
                    print(f"  {rekom} | freq={freq}")
            print("[Big-O: O(V + E)]")
        elif perintah == "KATALOG":
            semua = bst.inorder()
            for buku in semua:
                print(f"{buku.isbn} | {buku.judul} | {buku.kategori}")
            print("[Big-O: O(n)]")
        elif perintah == "BATALKAN_TERAKHIR":
            if riwayat_global.is_empty():
                print("Tidak ada transaksi")
            else:
                label, data = riwayat_global.pop()
                if label == "HAPUS":
                    bst.insert(data)
                    print(f"Undo: Buku {data.isbn} dikembalikan ke katalog.")
                elif label == "PINJAM":
                    bst.update_status(data.isbn, STATUS["TERSEDIA"])
                    if data.isbn in peminjaman_aktif:
                        del peminjaman_aktif[data.isbn]
                    print(f"Undo: Transaksi {data.transaksi_id} dibatalkan")
            print("[Big-O: O(log n)]")
        elif perintah == "BATALKAN_PESANAN":
            if len(cmd) != 3:
                print("Format: BATALKAN_PESANAN <anggota_id> <isbn>")
                continue
            aid, isbn = cmd[1], cmd[2]
            if isbn in antrian_pesan and antrian_pesan[isbn].delete_by_value(aid):
                print(f"Pesanan {aid} untuk buku {isbn} berhasil dibatalkan.")
            else:
                print("Data pesanan tidak ditemukan.")
            print("[Big-O: O(n)]")
        elif perintah == "HAPUS_RUSAK":
            if len(cmd) != 2:
                print("Format: HAPUS_RUSAK <isbn>")
                continue
            isbn = cmd[1]
            buku_target = bst.search(isbn)
            if buku_target:
                riwayat_global.push(("HAPUS", buku_target))
                bst.delete(isbn)
                print(f"Buku {isbn} berhasil dihapus dari katalog (Rusak).")
            else:
                print("Buku tidak ditemukan.")
            print("[Big-O: O(log n)]")
        elif perintah == "LAPORAN_BULAN":
            # 1. Siapkan data dari Katalog (untuk Merge Sort)
            data_buku = bst.inorder()

            # 2. Siapkan data dari Riwayat (untuk Shell Sort)
            # Kita filter hanya yang labelnya "PINJAM"
            raw_riwayat = riwayat_global.to_list()
            data_peminjaman = [item[1] for item in raw_riwayat if item[0] == "PINJAM"]

            print(f"\n=== LAPORAN BULANAN (N Riwayat={len(data_peminjaman)}) ===")

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
