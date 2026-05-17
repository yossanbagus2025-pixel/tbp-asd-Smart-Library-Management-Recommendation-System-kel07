# tbp-asd-SmartLibraryManagementRecommendationSystemkel07

## Deskripsi Program

Smart Library System adalah program simulasi sistem perpustakaan berbasis terminal (CLI) Interaktif menggunakan bahasa pemrograman Python.

Program ini menerapkan beberapa struktur data dan algoritma, yaitu:

- Binary Search Tree (BST)
- Queue (Linked List)
- Stack (Linked List)
- Graph
- Shell Sort
- Merge Sort

Fitur utama program:

- Pencarian buku
- Peminjaman buku
- Pengembalian buku
- Pemesanan/antrian buku
- Undo transaksi
- Rekomendasi buku
- Laporan bulanan
- Penghapusan buku rusak

---

## Struktur Data dan Algoritma

| Struktur Data / Algoritma | Fungsi |
| --- | --- |
| BST | Menyimpan katalog buku |
| Queue | Menyimpan antrian pemesanan |
| Stack | Menyimpan riwayat transaksi |
| Graph | Sistem rekomendasi buku |
| Shell Sort | Mengurutkan durasi peminjaman |
| Merge Sort | Mengurutkan frekuensi peminjaman |

---

## Cara Menjalankan Program

### Install Python

Pastikan Python 3 sudah terinstall.

Cek versi Python:

```bash
python --version
```

### Install Dependency

Program menggunakan NumPy.

```bash
pip install numpy
```

### Jalankan Program

```bash
python main.py
```

---

## Daftar Perintah

| Perintah | Fungsi |
| --- | --- |
| BANTUAN | Menampilkan daftar command |
| CARI_BUKU | Mencari buku berdasarkan ISBN |
| PINJAM | Meminjam buku |
| KEMBALIKAN | Mengembalikan buku |
| PESAN | Memesan buku |
| ANTRIAN | Melihat antrian buku |
| REKOMENDASI | Menampilkan rekomendasi buku |
| KATALOG | Menampilkan katalog |
| BATALKAN_TERAKHIR | Undo transaksi terakhir |
| BATALKAN_PESANAN | Membatalkan antrian |
| HAPUS_RUSAK | Menghapus buku rusak |
| LAPORAN_BULAN | Menampilkan laporan sorting |
| KELUAR | Keluar program |

---

## Contoh Input dan Output

### Perintah BANTUAN

#### Input Perintah BANTUAN

```bash
BANTUAN
```

#### Output Perintah BANTUAN

```bash
DAFTAR PERINTAH:
  CARI_BUKU <isbn>
  PINJAM <anggota_id> <isbn>
  KEMBALIKAN <isbn>
  PESAN <anggota_id> <isbn>
  BATALKAN_TERAKHIR
  REKOMENDASI <isbn>
  KATALOG
  ANTRIAN <isbn>
  BATALKAN_PESANAN <anggota_id> <isbn>
  HAPUS_RUSAK <isbn>
  LAPORAN_BULAN
  KELUAR
```

---

### Perintah CARI_BUKU

#### Input Perintah CARI_BUKU

```bash
CARI_BUKU ISBN-0001
```

#### Output Perintah CARI_BUKU

```bash
ISBN       : ISBN-0001
Judul      : Python Vol.1
Pengarang  : Penulis-5
Kategori   : Teknik
Status     : 0

[Big-O: O(log n)]
```

---

### Perintah PINJAM

#### Input Perintah PINJAM

```bash
PINJAM A001 ISBN-0001
```

#### Output Perintah PINJAM

```bash
Buku ISBN-0001 berhasil dipinjam

[Big-O: O(log n)]
```

---

### Perintah KEMBALIKAN

#### Input Perintah KEMBALIKAN

```bash
KEMBALIKAN ISBN-0001
```

#### Output Perintah KEMBALIKAN

```bash
Buku ISBN-0001 dikembalikan

[Big-O: O(log n)]
```

---

### Perintah PESAN

#### Input Perintah PESAN

```bash
PESAN A002 ISBN-0001
```

#### Output Perintah PESAN

```bash
A002 masuk antrian buku ISBN-0001

[Big-O: O(log n)]
```

---

### Perintah ANTRIAN

#### Input Perintah ANTRIAN

```bash
ANTRIAN ISBN-0001
```

#### Output Perintah ANTRIAN

```bash
Antrian buku ISBN-0001:
  - A002
  - A003

[Big-O: O(n)]
```

---

### Perintah REKOMENDASI

#### Input Perintah REKOMENDASI

```bash
REKOMENDASI ISBN-0001
```

#### Output Perintah REKOMENDASI

```bash
Rekomendasi untuk ISBN-0001:
  ISBN-0005 | freq=3
  ISBN-0010 | freq=1

[Big-O: O(V + E)]
```

---

### Perintah KATALOG

#### Input Perintah KATALOG

```bash
KATALOG
```

#### Output Perintah KATALOG

```bash
ISBN-0001 | Python Vol.1 | Teknik
ISBN-0002 | Data Vol.2 | Sains
ISBN-0003 | Sistem Vol.3 | Teknik

[Big-O: O(n)]
```

---

### Perintah BATALKAN_TERAKHIR

#### Input Perintah BATALKAN_TERAKHIR

```bash
BATALKAN_TERAKHIR
```

#### Output Perintah BATALKAN_TERAKHIR

```bash
Undo: Transaksi 1 dibatalkan

[Big-O: O(log n)]
```

---

### Perintah BATALKAN_PESANAN

#### Input Perintah BATALKAN_PESANAN

```bash
BATALKAN_PESANAN A002 ISBN-0001
```

#### Output Perintah BATALKAN_PESANAN

```bash
Pesanan A002 untuk buku ISBN-0001 berhasil dibatalkan.

[Big-O: O(n)]
```

---

### Perintah HAPUS_RUSAK

#### Input Perintah HAPUS_RUSAK

```bash
HAPUS_RUSAK ISBN-0001
```

#### Output Perintah HAPUS_RUSAK

```bash
Buku ISBN-0001 berhasil dihapus dari katalog (Rusak).

[Big-O: O(log n)]
```

---

### Perintah LAPORAN_BULAN

#### Input Perintah LAPORAN_BULAN

```bash
LAPORAN_BULAN
```

#### Output Perintah LAPORAN_BULAN

```bash
=== LAPORAN BULANAN ===

[Shell Sort - Durasi Descending]
ID: 1 | Durasi: 14 hari

[Merge Sort - Frekuensi Descending]
Python Vol.1 | Dipinjam: 5x

Perbandingan Runtime:
Shell Sort: 0.000010s
Merge Sort: 0.000005s

[Big-O: Shell ~O(n^1.5), Merge O(n log n)]
```

---

### Perintah KELUAR

#### Input Perintah KELUAR

```bash
KELUAR
```

#### Output Perintah KELUAR

```bash
Program selesai
```

---

## Analisis Kompleksitas Big-O

| Operasi | Kompleksitas |
| --- | --- |
| BST Search | O(log n) |
| BST Insert | O(log n) |
| BST Delete | O(log n) |
| Queue Enqueue | O(1) |
| Queue Dequeue | O(1) |
| Queue Delete | O(n) |
| Stack Push | O(1) |
| Stack Pop | O(1) |
| Inorder Traversal | O(n) |
| Shell Sort | O(n^1.5) |
| Merge Sort | O(n log n) |
| BFS Graph | O(V + E) |

---

## Penulis

Nama:

- Yossan Bagus Pramuditya (25051030013)            - Ketua
- Bimo Aqces Saefullah (25051030003)               - Anggota
- Muhammad Erji Alvinandra Pratama (25051030008)   - Anggota
- Daffa Rifqi Muafa (25051030019)                  - Anggota

Kelompok: 7

Kelas: G

Mata Kuliah: Algoritma dan Struktur Data

Teknik Elektro(S1)_Departemen Pendidikan Teknik Elektro_Fakultas Teknik_Universitas Negeri Yogyakarta

tesbranch
