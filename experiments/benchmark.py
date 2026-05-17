from pathlib import Path
import sys
import os
import time
import random

current_file = Path(__file__).resolve()
src_dir = current_file.parent.parent / "src"
sys.path.append(str(src_dir))

from modules.models import generate_koleksi, Peminjaman
from modules.layanan_transaksi import shell_sort_durasi, merge_sort_frekuensi
from data_structures.bst import BSTKatalog
from data_structures.queue_ll import Queue
from data_structures.stack import Stack

# EXPERIMEN 1 — BST Search

print("\n=== Eksperimen 1: BST Search ===")
bst = BSTKatalog()
for buku in generate_koleksi(500):
    bst.insert(buku)
target = "ISBN-0500"
start = time.time()
hasil = bst.search(target)
end = time.time()
print("Hasil:", hasil.judul if hasil else "Tidak ditemukan")
print("Runtime:", end - start)

# EXPERIMEN 2 — Queue

print("\n=== Eksperimen 2: Queue ===")

queue = Queue()
start = time.time()
for i in range(1000):
    queue.enqueue(i)
for i in range(1000):
    queue.dequeue()
end = time.time()
print("Runtime:", end - start)

# EXPERIMEN 3 — Stack

print("\n=== Eksperimen 3: Stack ===")

stack = Stack()
start = time.time()
for i in range(1000):
    stack.push(i)
for i in range(1000):
    stack.pop()
end = time.time()
print("Runtime:", end - start)

# EXPERIMEN 4 — Shell Sort

print("\n=== Eksperimen 4: Shell Sort ===")

data = []
for i in range(1000):
    trx = Peminjaman(i, "A001", f"ISBN-{i}", time.time(), random.randint(1, 30))
    data.append(trx)
start = time.time()
shell_sort_durasi(data)
end = time.time()
print("Runtime:", end - start)

# EXPERIMEN 5 — Merge Sort

print("\n=== Eksperimen 5: Merge Sort ===")

buku_data = generate_koleksi(999)
for buku in buku_data:
    buku.pinjam_count = random.randint(1, 100)
start = time.time()
merge_sort_frekuensi(buku_data)
end = time.time()
print("Runtime:", end - start)
