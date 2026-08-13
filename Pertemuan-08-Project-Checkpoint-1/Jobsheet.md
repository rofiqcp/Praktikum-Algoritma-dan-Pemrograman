# Jobsheet Pertemuan 08 — Project Checkpoint 1

## Tahap 1 — Pilih dan Analisis Soal
1. Pilih satu project dari `Project.md`.
2. Tulis aktor/pengguna, input, proses, output, aturan, dan kondisi error.
3. Pecah menjadi minimal empat fitur operasi dan lima function.
4. Buat flowchart/pseudocode sebelum coding.

## Tahap 2 — Rancang Data
Tentukan list/dictionary yang menyimpan state. Tuliskan contoh data awal dan aturan validasinya.

## Tahap 3 — Implementasi Bertahap
Gunakan commit kecil, misalnya:
```text
chore: buat struktur project
feat: tambah data dan menu utama
feat: tambah operasi utama
fix: validasi boundary dan not-found
test: tambah delapan test case
docs: lengkapi README dan demo
```

## Tahap 4 — Pengujian Minimum
Buat minimal 8 test case yang mencakup:
- normal;
- nilai tepat di boundary;
- input kosong;
- tipe input salah;
- data tidak ditemukan;
- duplikat;
- kapasitas/stok tidak cukup bila relevan;
- regression setelah fitur baru.

## Tahap 5 — Review Kualitas
- Tidak ada satu fungsi raksasa untuk seluruh program.
- Nama variable/function menjelaskan maksud.
- Tidak ada logic duplikat berlebihan.
- Program tetap berjalan setelah input salah yang wajar.
- README memiliki setup, run, contoh penggunaan, test, struktur, dan batasan.

## Deliverable
- Source runnable.
- README.
- Flowchart/pseudocode.
- Tabel test case expected/actual.
- Minimal 5 commit progres.
- Demo 3–5 menit.

## Starter
```bash
cd praktikum/starter-cli
python main.py
python -m unittest discover -s tests -v
```
Starter dipakai hanya untuk memahami struktur menu/function/test.
