# Jobsheet Pertemuan 04 — Loop, Counter, dan Akumulasi

## Environment
Scratch + Google Colab + Python.

## Tujuan
Mahasiswa mampu memilih `for` atau `while`, menggunakan counter dan accumulator, melakukan tracing setiap iterasi, menjelaskan `range()`, menggunakan sentinel sebagai penanda berhenti, dan membuat nested loop sederhana.

## Aturan Kerja
Untuk setiap percobaan: tulis rule → prediksi jumlah iterasi → isi tracing → jalankan → bandingkan expected dan actual → perbaiki bila berbeda → retest.

## Percobaan Wajib

### P01 — Akumulasi Harian
Jalankan `praktikum/python/01_tabungan_harian.py`. Gunakan contoh 4 iterasi dengan tambahan 5000.

| Iterasi | Counter | Total sebelum | Tambahan | Total sesudah |
|---:|---:|---:|---:|---:|
| 1 | 1 | 0 | 5000 |  |
| 2 | 2 |  | 5000 |  |
| 3 | 3 |  | 5000 |  |
| 4 | 4 |  | 5000 |  |

Jelaskan mengapa accumulator harus diinisialisasi sebelum loop.

### P02 — Bilangan Genap
Jalankan `praktikum/python/02_bilangan_genap.py`.

| Awal | Akhir | Expected |
|---:|---:|---|
| 1 | 10 | 2, 4, 6, 8, 10 |
| 2 | 2 | 2 |
| 3 | 3 | tidak ada output genap |
| -2 | 2 | -2, 0, 2 |

Jelaskan sifat stop eksklusif pada `range()`.

### P03 — Lima Nilai dan Rata-rata Tanpa List
Jalankan `praktikum/python/06_rata_rata_lima_nilai.py`. Latihan ini sengaja tidak menggunakan list agar fokus tetap pada accumulator.

| Iterasi | Nilai | Total sebelum | Total sesudah |
|---:|---:|---:|---:|
| 1 | 80 |  |  |
| 2 | 75 |  |  |
| 3 | 90 |  |  |
| 4 | 85 |  |  |
| 5 | 70 |  |  |

Hitung total dan rata-rata secara manual sebelum Run.

### P04 — Pengulangan sampai Kondisi Terpenuhi
Jalankan `praktikum/python/03_tebak_angka.py`.

| Iterasi | Input | Condition | Output | Lanjut/Stop |
|---:|---:|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |

Jelaskan mengapa jumlah iterasi tidak selalu diketahui sebelum program berjalan.

### P05 — Sentinel
Jalankan contoh input berulang pada folder `praktikum/python/` yang memakai `0` sebagai tanda selesai.

| Urutan input | Expected jumlah data | Expected total |
|---|---:|---:|
| `0` | 0 | 0 |
| `10, 0` | 1 | 10 |
| `10, 5, 0` | 2 | 15 |

Jelaskan mengapa sentinel tidak ikut diakumulasi.

### P06 — Nested Loop
Jalankan `praktikum/python/05_pola_bintang.py` dan trace empat baris.

| Outer | Jumlah inner | Output |
|---:|---:|---|
| 1 |  |  |
| 2 |  |  |
| 3 |  |  |
| 4 |  |  |

### P07 — Scratch Loop
Buka `praktikum/scratch/README.md`, lalu buat minimal dua padanan visual.

| Scratch | Python |
|---|---|
| `repeat n` | `for ... range(...)` |
| `forever` | `while True` |
| `repeat until` | `while not kondisi` |
| `change total by nilai` | `total += nilai` |

## Debugging Wajib

1. **Loop tidak berhenti:** pada salinan program, hilangkan perubahan variable kondisi lalu jelaskan penyebabnya dan retest setelah diperbaiki.
2. **Off-by-one:** bandingkan `range(1,6)` dan `range(1,5)` dengan deret expected.
3. **Accumulator reset:** pindahkan inisialisasi total ke dalam loop pada salinan, trace tiga iterasi, lalu kembalikan ke tempat yang benar.

Format catatan:

```text
Gejala:
Input:
Expected:
Actual:
Iterasi terakhir yang benar:
Variable yang berubah:
Hipotesis:
Perbaikan:
Retest:
```

## Pertanyaan Analisis
1. Kapan `for` lebih tepat daripada `while`?
2. Apa arti stop eksklusif pada `range()`?
3. Apa beda counter dan accumulator?
4. Mengapa accumulator dibuat sebelum loop?
5. Apa yang harus berubah agar `while` berhenti?
6. Apa fungsi sentinel?
7. Apa beda outer dan inner loop?
8. Mengapa latihan rata-rata dibuat tanpa list?

## Deliverable
- output seluruh program;
- notebook Colab;
- minimal dua contoh Scratch;
- tracing table;
- expected-versus-actual;
- tiga catatan debugging;
- satu modifikasi mandiri;
- kesimpulan.

## Checklist
- [ ] P01 selesai dan ditrace.
- [ ] P02 diuji.
- [ ] P03 dibuat tanpa list.
- [ ] P04 dijalankan sampai condition selesai.
- [ ] P05 sentinel diuji.
- [ ] P06 nested loop ditrace.
- [ ] P07 Scratch dibandingkan dengan Python.
- [ ] Tiga debugging diperbaiki dan diretest.
