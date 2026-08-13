# Materi Pertemuan 02 — Scratch + Python Google Colab I: Sequence, Input, Output, dan Variabel

> **Sumber utama:** *Buku Panduan Praktik: Pemrograman Dasar hingga Full Stack — 16 Pertemuan Terstruktur, Edisi Agustus 2026*. Contoh executable yang dirapikan berada di folder `praktikum/`.

Setiap algoritma dibuat dua kali: pertama visual di Scratch, lalu ditulis sebagai Python di Google Colab.

## Target Kompetensi

- Membuat notebook Google Colab dan menjalankan cell.
- Menerjemahkan blok `say/set/ask/operator` ke `print/variable/input/operator` Python.
- Mengenal string, integer, float, dan boolean.
- Memprediksi output program sebelum menekan Run.

## Output Pertemuan

- Notebook Colab dengan minimal empat latihan.
- Project Scratch dan Python dengan input-output yang setara.

## Alur Pengajaran 180 Menit

| Tahap | Durasi | Aktivitas |
|---|---:|---|
| Review | 15 | Ulang input–process–output dan variable dari Scratch. |
| Colab | 20 | Notebook, code cell, text cell, Run, reset runtime. |
| Scratch pair | 25 | Program biodata/kalkulator sederhana. |
| Python dasar | 35 | `print`, variable, `input`, type conversion, operator. |
| Terjemahkan algoritma | 40 | Scratch → pseudocode → Python. |
| Challenge | 30 | Kalkulator biaya atau konversi. |
| Debug | 15 | NameError, ValueError, salah tipe data. |

## 2.1 Mengenal Google Colab

Google Colab adalah lingkungan notebook berbasis browser. Satu notebook berisi cell teks dan cell kode. Cell dapat dijalankan tidak selalu dari atas ke bawah; biasakan menjalankan semua cell berurutan. Jika hasil terasa aneh, gunakan Restart/Reset runtime lalu Run all.

## 2.2 Pemetaan Scratch ↔ Python

| Scratch | Python | Konsep |
|---|---|---|
| `say "Halo"` | `print("Halo")` | Output |
| `set nama to "Ayu"` | `nama = "Ayu"` | Variable |
| `ask "Nama?" and wait` | `nama = input("Nama? ")` | Input |
| `(5) + (3)` | `5 + 3` | Operator |
| `join "Halo " nama` | f-string / concatenation | String composition |
| `answer` | hasil `input()` | Nilai pengguna |

## 2.3 Praktik Paralel: Kalkulator Belanja

Soal cerita: program meminta nama barang, harga satuan, dan jumlah pembelian, lalu menghitung total.

```python
nama_barang = input("Nama barang: ")
harga = float(input("Harga satuan: "))
jumlah = int(input("Jumlah: "))
total = harga * jumlah
print(f"Barang : {nama_barang}")
print(f"Jumlah : {jumlah}")
print(f"Total  : Rp{total:,.0f}")
```

## 2.4 Latihan Bertingkat

| Level | Soal | Konsep |
|---|---|---|
| A | Hitung luas persegi panjang | variable, float, operator |
| A | Konversi menit menjadi jam dan sisa menit | `//` dan `%` |
| B | Hitung total pembelian 3 jenis barang | multiple input |
| B | Konversi Celsius ke Fahrenheit dan Kelvin | formula |
| C | Estimasi biaya perjalanan | pemodelan sederhana |

## 2.5 Error yang Wajib Dipahami

| Gejala | Penyebab umum | Perbaikan |
|---|---|---|
| `NameError` | Nama variable salah | Cocokkan ejaan dari traceback |
| `ValueError` saat `int()` | Input bukan angka valid | Uji input dan pahami konversi tipe |
| `TypeError` string + int | Tipe dicampur tanpa konversi | Gunakan `str/int/float` atau f-string |
| Output lama di Colab | Cell tidak berurutan | Restart runtime + Run all |
