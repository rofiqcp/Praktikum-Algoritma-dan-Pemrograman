# Materi Pertemuan 04 — Scratch + Python Google Colab III: Loop, Counter, dan Akumulasi

> Sumber utama: *Buku Panduan Praktik: Pemrograman Dasar hingga Full Stack — 16 Pertemuan Terstruktur, Edisi Agustus 2026*. Contoh runnable ada di `praktikum/`.

Peserta belajar mengulang proses secara terkontrol dan memahami kapan menggunakan `repeat/for` atau `forever/while`.

## Target Kompetensi
- Membedakan loop dengan jumlah iterasi diketahui dan tidak diketahui.
- Menggunakan counter dan accumulator.
- Menghindari infinite loop.
- Membuat nested loop sederhana.

## Output Pertemuan
- Simulasi loop di Scratch.
- Program Python dengan `for` dan `while`.
- Tabel tracing nilai variable tiap iterasi.

## Alur Pengajaran 180 Menit
| Tahap | Durasi | Aktivitas |
|---|---:|---|
| Review | 15 | Condition dan test case. |
| Loop Scratch | 25 | `repeat`, `forever`, `repeat until`. |
| Tracing | 20 | Counter dan perubahan variable. |
| Python `for` | 30 | `range` dan iterasi. |
| Python `while` | 25 | Condition loop dan sentinel. |
| Praktik | 45 | Tabungan/skor/transaksi berulang. |
| Debug | 20 | Infinite loop dan off-by-one. |

## 4.1 Pola Loop
| Situasi | Scratch | Python |
|---|---|---|
| Ulang tepat 10 kali | `repeat 10` | `for i in range(10)` |
| Berjalan terus sampai dihentikan | `forever` | `while True` |
| Ulang sampai kondisi terpenuhi | `repeat until` | `while not kondisi` |
| Menghitung total | `change total by nilai` | `total += nilai` |

## 4.2 Counter dan Accumulator
- **Counter** menyimpan jumlah kejadian/iterasi.
- **Accumulator** menyimpan hasil penjumlahan bertahap.
- Inisialisasi dilakukan **sebelum loop**, bukan di dalam loop.

## 4.3 Praktik Paralel: Tabungan Harian
```python
saldo = 0
hari = int(input("Berapa hari menabung? "))
setoran = float(input("Setoran per hari: "))
for i in range(1, hari + 1):
    saldo += setoran
    print(f"Hari {i}: saldo Rp{saldo:,.0f}")
print(f"Saldo akhir: Rp{saldo:,.0f}")
```

### Tracing contoh
| Iterasi | i | setoran | saldo sebelum | saldo sesudah |
|---:|---:|---:|---:|---:|
| 1 | 1 | 10.000 | 0 | 10.000 |
| 2 | 2 | 10.000 | 10.000 | 20.000 |
| 3 | 3 | 10.000 | 20.000 | 30.000 |

## 4.4 Tantangan
- Cetak bilangan genap pada rentang pengguna.
- Minta lima nilai dan hitung rata-rata tanpa list.
- Game tebak angka sampai benar.
- Kasir menerima harga sampai sentinel `0`.
- Pola bintang dengan nested loop.

## Troubleshooting
| Gejala | Kemungkinan penyebab | Perbaikan |
|---|---|---|
| Loop tidak berhenti | Kondisi `while` tidak pernah false | Pastikan variable kondisi berubah di loop |
| Iterasi kurang/lebih satu | Stop `range` tidak termasuk | Tulis deret yang diharapkan lalu cocokkan `range` |
| Total selalu nol | Accumulator di-reset di loop | Inisialisasi sebelum loop |
| Input tak selesai | Sentinel beda tipe | Cek input string atau angka |
