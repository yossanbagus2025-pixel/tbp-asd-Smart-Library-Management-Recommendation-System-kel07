import sys
import os
import time
import numpy as np
import random

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.models import STATUS, KATEGORI, Buku, Peminjaman, generate_koleksi
from modules.layanan_katalog import LayananKatalog
from modules.layanan_transaksi import shell_sort_durasi, merge_sort_frekuensi
from data_structures.queue_ll import Queue
from data_structures.stack import Stack
from data_structures.graph import GraphRekBuku

np.random.seed(13)
random.seed(13)


def main():
    layanan_kat = LayananKatalog()
    bst = layanan_kat.bst
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
            """Big-O: O(1)"""
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
            """
            Big-O Average: O(log n)
            Big-O Worst  : O(n)
            """
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
            """
            Big-O Average: O(log n + k)
            Big-O Worst  : O(n + k)
            """
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
            """
            Big-O Average: O(log n)
            Big-O Worst  : O(n)
            """
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
            """
            Big-O Average: O(log n)
            Big-O Worst  : O(n)
            """
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
            """Big-O: O(n)"""
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
            """Big-O: O(V + E)"""
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
            """Big-O: O(n)"""
            semua = bst.inorder()
            for buku in semua:
                print(f"{buku.isbn} | {buku.judul} | {buku.kategori}")
            print("[Big-O: O(n)]")
        elif perintah == "BATALKAN_TERAKHIR":
            """
            Big-O Average: O(log n)
            Big-O Worst  : O(n)
            """
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
            """Big-O: O(n)"""
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
            """
            Big-O Average: O(log n)
            Big-O Worst  : O(n)
            """
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
            """Big-O: O(n log n + n²)"""
            data_buku = bst.inorder()
            raw_riwayat = riwayat_global.to_list()
            data_peminjaman = [item[1] for item in raw_riwayat if item[0] == "PINJAM"]
            print(f"\n=== LAPORAN BULANAN (N Riwayat={len(data_peminjaman)}) ===")

            # --- Uji Shell Sort (Durasi) ---
            t_start = time.time()
            res_shell = shell_sort_durasi(data_peminjaman[:])
            t_shell = time.time() - t_start
            print(f"\n[Shell Sort - Durasi Descending] Runtime: {t_shell:.6f}s")
            for p in res_shell[:5]:
                print(f"ID: {p.transaksi_id} | Durasi: {p.durasi_hari} hari")

            # --- (b) Uji Merge Sort (Frekuensi) ---
            t_start = time.time()
            res_merge = merge_sort_frekuensi(data_buku[:])
            t_merge = time.time() - t_start
            print(f"\n[Merge Sort - Frekuensi Descending] Runtime: {t_merge:.6f}s")
            for b in res_merge[:5]:
                print(f"{b.judul} | Dipinjam: {b.pinjam_count}x")

            print(f"\nPerbandingan Runtime (N={len(data_buku)}):")
            print(f"Shell Sort: {t_shell:.6f}s vs Merge Sort: {t_merge:.6f}s")
            print("[Big-O: Shell ~O(n^1.5), Merge O(n log n)]")
        elif perintah == "KELUAR":
            """Big-O: O(1)"""
            print("Program selesai")
            break
        else:
            print("Perintah tidak dikenali")


if __name__ == "__main__":
    main()
