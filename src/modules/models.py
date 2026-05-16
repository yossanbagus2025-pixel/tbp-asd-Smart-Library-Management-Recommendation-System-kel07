import random
from dataclasses import dataclass

KATEGORI = ["Fiksi", "Sains", "Teknik", "Sejarah", "Seni"]
STATUS = {"TERSEDIA": 0, "DIPINJAM": 1, "DIPESAN": 2}


@dataclass
class Buku:
    isbn: str  # kunci BST
    judul: str
    pengarang: str
    kategori: str
    status: int = 0  # 0=TERSEDIA, 1=DIPINJAM, 2=DIPESAN
    pinjam_count: int = 0


@dataclass
class Peminjaman:
    transaksi_id: int
    anggota_id: str
    isbn: str
    tgl_pinjam: float  # time.time()
    durasi_hari: int = 14


def generate_koleksi(n=80):
    """Big-O: O(n)"""
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
