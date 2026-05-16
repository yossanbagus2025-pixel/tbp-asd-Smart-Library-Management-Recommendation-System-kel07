# Deskripsi Perubahan

Melakukan modularisasi kode program utama ke dalam struktur folder yang sesuai dengan panduan TBP (Team Based Project). Selain itu, memperbaiki bug `RecursionError` pada pengujian BST dengan membatasi sampel data dummy maksimal menjadi 500 item agar aman dari batasan limit rekursi Python.

## Modul yang Berubah

- [x] src/data_structures/linked_list.py
- [x] src/data_structures/stack.py
- [x] src/data_structures/queue_ll.py
- [x] src/data_structures/bst.py
- [x] src/data_structures/graph.py
- [x] src/modules/models.py
- [ ] src/modules/layanan_katalog.py
- [ ] src/modules/layanan_transaksi.py
- [x] src/main.py

## Checklist Sebelum Merge

- [x] Kode berjalan tanpa error (`python src/main.py`)
- [x] Unit test lulus (`python -m unittest discover -s tests` atau `pytest`)
- [x] Analisis Big-O ditulis sebagai docstring komentar
- [x] Tidak ada kode debug / print sementara tertinggal
- [ ] README diupdate jika ada perubahan cara menjalankan

## Hasil Uji Singkat

OK semua test lulus. Hasil running `python -m unittest discover -s tests` memunculkan pesan OK (7 tests passed). Skrip `benchmark.py` juga berjalan normal menghasilkan data runtime untuk kelima eksperimen.

## Anggota yang Mengerjakan

- Yossan Bagus Pramuditya (25051030013)            - Ketua
- Bimo Aqces Saefullah (25051030003)               - Anggota
- Muhammad Erji Alvinandra Pratama (25051030008)   - Anggota
- Daffa Rifqi Muafa (25051030019)                  - Anggota
