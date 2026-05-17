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
