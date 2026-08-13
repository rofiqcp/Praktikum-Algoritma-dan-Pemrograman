# Materi Pertemuan 02 — Scratch + Python Colab I: Sequence, Input, Output, dan Variabel

> Disusun dari **Buku Panduan Praktik: Pemrograman Dasar hingga Full Stack, 16 Pertemuan Terstruktur (Edisi Agustus 2026)**.

## Target Kompetensi

- Membuat notebook Google Colab dan menjalankan cell secara benar.
- Menerjemahkan blok Scratch say/set/ask/operator menjadi print/variable/input/operator Python.
- Menggunakan string, integer, float, boolean, dan konversi tipe data.

## Filosofi Pertemuan

Materi dibuat dengan pola **mental model → contoh → praktik → challenge → debugging → refleksi**. Mahasiswa tidak cukup hanya membuat program “jalan”; mahasiswa harus dapat menjelaskan input, proses, keputusan, data, output, dan bukti pengujian.

## 1. Scratch ↔ Python

| Scratch | Python | Konsep |
|---|---|---|
| `say "Halo"` | `print("Halo")` | output |
| `set nama to "Ayu"` | `nama = "Ayu"` | variable |
| `ask "Nama?" and wait` | `nama = input("Nama? ")` | input |
| `(5) + (3)` | `5 + 3` | operator |
| `join "Halo " nama` | `f"Halo {nama}"` | string composition |

## 2. Tipe Data

- `str`: teks
- `int`: bilangan bulat
- `float`: bilangan desimal
- `bool`: `True`/`False`

`input()` selalu menghasilkan string sehingga data angka biasanya dikonversi dengan `int()` atau `float()`.

## 3. Program Paralel: Kalkulator Belanja

Algoritma:
1. baca nama barang;
2. baca harga;
3. baca jumlah;
4. hitung `total = harga * jumlah`;
5. tampilkan ringkasan.

## 4. Operator Penting

- aritmatika: `+ - * / // % **`
- assignment: `=`
- gabungan string: f-string
- `//` untuk pembagian bulat, `%` untuk sisa pembagian.

## 5. Debugging Colab

Jika output terasa “aneh”:
1. Restart/Reset runtime.
2. Run all dari atas.
3. Baca `NameError`, `ValueError`, dan `TypeError`.
4. Periksa tipe data dengan `type(variable)`.
