import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from modules.layanan_transaksi import shell_sort_durasi, merge_sort_frekuensi
from modules.models import Buku, Peminjaman


class TestLayananTransaksiModule(unittest.TestCase):
    def test_sorting_algorithms(self):
        p1 = Peminjaman(1, "MHS1", "ISBN-1", 100.0, 5)
        p2 = Peminjaman(2, "MHS2", "ISBN-2", 200.0, 10)
        sorted_p = shell_sort_durasi([p1, p2])
        self.assertEqual(sorted_p[0].durasi_hari, 10)


if __name__ == "__main__":
    unittest.main()
