# Materi Pertemuan 05 — Scratch + Python Google Colab IV: List, Data, Pencarian, dan Statistik

> Sumber utama: buku panduan 16 pertemuan, Edisi Agustus 2026. Contoh runnable ada di `praktikum/`.

Pada sesi ini peserta mulai memproses sekumpulan data, bukan hanya satu nilai.

## Target Kompetensi
- Membuat dan mengubah list.
- Melakukan loop pada list.
- Mencari nilai dan menghitung statistik sederhana.
- Menggunakan dictionary sebagai pengantar data terstruktur.

## Output
- Daftar data di Scratch dan list/dictionary di Python.
- Mini aplikasi pengelolaan data dalam memori.

## Alur 180 Menit
| Tahap | Durasi | Aktivitas |
|---|---:|---|
| Review | 15 | Loop dan accumulator |
| List Scratch | 25 | add/delete/item/length |
| List Python | 35 | append, remove, len, indexing |
| Search & aggregate | 30 | `in`, `min`, `max`, `sum`, average |
| Dictionary intro | 25 | key-value |
| Praktik | 35 | Data nilai/barang |
| Debug | 15 | IndexError dan KeyError |

## 5.1 Dari Banyak Variable ke List
Tanpa list, data `nilai1`, `nilai2`, ... tidak skalabel. List memungkinkan jumlah data bertambah dan diproses dengan loop.

```python
nilai = [80, 75, 90, 68, 88]
print("Jumlah data:", len(nilai))
print("Tertinggi:", max(nilai))
print("Terendah:", min(nilai))
print("Rata-rata:", sum(nilai) / len(nilai))
```

## 5.2 Dictionary
```python
produk = {
    "nama": "Keyboard",
    "harga": 250000,
    "stok": 10
}
print(produk["nama"])
print(produk["stok"])
```
Dictionary adalah pasangan **key–value**. Pada tahap ini dictionary belum dipakai sebagai database; tujuannya memahami satu objek dengan beberapa atribut.

## 5.3 Praktik Paralel: Daftar Nilai
Scratch menggunakan List `Nilai`. Python menggunakan list, iterasi, dan fungsi agregasi.

```python
nilai=[]
jumlah_data=int(input("Jumlah siswa: "))
for i in range(jumlah_data):
    nilai.append(float(input(f"Nilai siswa ke-{i+1}: ")))
if nilai:
    print("Rata-rata:",sum(nilai)/len(nilai))
    print("Tertinggi:",max(nilai))
```

## 5.4 Latihan
- Daftar belanja: tambah, tampilkan, cari.
- Nilai siswa: jumlah lulus/tidak lulus.
- Stok barang: list of dictionaries + pencarian nama.
- Suhu harian: max/min/rata-rata.
- Voting sederhana: hitung frekuensi.

## Troubleshooting
| Gejala | Penyebab | Perbaikan |
|---|---|---|
| `IndexError` | Mengakses posisi yang tidak ada | Ingat index mulai 0; cek `len` |
| `KeyError` | Key dictionary tidak tersedia | Cek ejaan atau gunakan `.get()` |
| Data tidak bertambah | `append` tidak terpanggil/list di-reset | Buat list sebelum loop |
| Rata-rata error | List kosong | Validasi `len(list)>0` |
