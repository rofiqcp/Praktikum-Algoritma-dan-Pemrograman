# Materi Pertemuan 05 — Scratch + Python Google Colab IV: List, Data, Pencarian, dan Statistik

> **Sumber utama:** *Buku Panduan Praktik: Pemrograman Dasar hingga Full Stack — 16 Pertemuan Terstruktur, Edisi Agustus 2026*.
>
> Pertemuan ini merupakan kelanjutan langsung dari loop, counter, dan accumulator. Fokus berubah dari mengolah **satu nilai** menjadi mengolah **sekumpulan data**. Sesuai buku panduan, mahasiswa tetap mengerjakan versi Scratch terlebih dahulu, kemudian menerjemahkan ide yang sama ke Python di Google Colab.

## Target Kompetensi

Setelah menyelesaikan pertemuan ini mahasiswa mampu:

- membuat list dan menjelaskan alasan list lebih baik daripada banyak variable terpisah;
- menambah, membaca, mengubah, dan menghapus data pada list;
- menjelaskan bahwa index Python dimulai dari `0`;
- melakukan loop pada seluruh isi list;
- melakukan pencarian data dengan `in` dan loop;
- menghitung `len`, `sum`, `min`, `max`, dan rata-rata;
- menghitung jumlah data yang memenuhi syarat tertentu;
- menggunakan dictionary sederhana sebagai pasangan **key–value**;
- membuat list of dictionaries untuk merepresentasikan beberapa objek sederhana;
- membedakan `IndexError`, `KeyError`, dan pembagian dengan list kosong;
- menguji kasus normal, boundary, data kosong, dan data tidak ditemukan.

## Output Pertemuan

1. Satu latihan Scratch menggunakan List.
2. Notebook Google Colab yang menjalankan seluruh contoh P05.
3. Minimal lima program Python runnable.
4. Mini aplikasi pengelolaan data dalam memori.
5. Tabel pengujian expected-vs-actual.
6. Catatan debugging minimal tiga kasus.

---

# 5.1 Mengapa Kita Membutuhkan List?

Pada pertemuan sebelumnya, lima nilai dapat disimpan sebagai:

```python
nilai1 = 80
nilai2 = 75
nilai3 = 90
nilai4 = 68
nilai5 = 88
```

Cara tersebut masih mungkin untuk lima data, tetapi menjadi sulit ketika jumlah data meningkat. Jika ada 100 nilai, membuat `nilai1` sampai `nilai100` tidak efisien. Program juga akan sulit diproses dengan loop.

List menyimpan beberapa nilai di bawah satu nama variable:

```python
nilai = [80, 75, 90, 68, 88]
```

Mental modelnya:

```text
LIST
+-------+-------+-------+-------+-------+
|  80   |  75   |  90   |  68   |  88   |
+-------+-------+-------+-------+-------+
 index 0  index 1  index 2  index 3  index 4
```

Perhatikan bahwa index Python dimulai dari **0**. Karena itu list yang memiliki panjang 5 mempunyai index valid `0` sampai `4`.

```python
nilai = [80, 75, 90, 68, 88]
print(nilai[0])   # 80
print(nilai[4])   # 88
```

Mengakses `nilai[5]` akan menghasilkan `IndexError` karena posisi tersebut tidak ada.

---

# 5.2 Operasi Dasar List

## Membuat list kosong

```python
data = []
```

## Menambah data

```python
data.append(80)
data.append(90)
print(data)
```

Hasil:

```text
[80, 90]
```

## Mengubah data berdasarkan index

```python
data[0] = 85
```

## Menghapus berdasarkan nilai

```python
data.remove(90)
```

## Menghapus berdasarkan index

```python
hapus = data.pop(0)
print("Data yang dihapus:", hapus)
```

## Menghitung jumlah data

```python
print(len(data))
```

### Hal yang harus dipahami

`append()` menambah satu elemen ke akhir list. `remove()` mencari nilai lalu menghapus kemunculan pertama. `pop()` menghapus berdasarkan posisi dan juga mengembalikan nilai yang dihapus. Mahasiswa tidak perlu menghafal semua method list; yang lebih penting adalah mengetahui **state list sebelum dan sesudah operasi**.

---

# 5.3 Loop pada List

List menjadi sangat berguna karena dapat diproses dengan loop.

```python
nilai = [80, 75, 90]

for n in nilai:
    print(n)
```

Tracing:

| Iterasi | `n` | Aksi |
|---:|---:|---|
| 1 | 80 | cetak 80 |
| 2 | 75 | cetak 75 |
| 3 | 90 | cetak 90 |

Jika index juga dibutuhkan, pada tahap ini mahasiswa dapat memakai pola sederhana:

```python
nilai = [80, 75, 90]

for i in range(len(nilai)):
    print(i, nilai[i])
```

---

# 5.4 Statistik Sederhana

Sesuai buku panduan, statistik pada P05 bersifat sederhana: jumlah data, total, nilai tertinggi, nilai terendah, dan rata-rata.

```python
nilai = [80, 75, 90, 68, 88]

print("Jumlah data:", len(nilai))
print("Total       :", sum(nilai))
print("Tertinggi   :", max(nilai))
print("Terendah    :", min(nilai))
print("Rata-rata   :", sum(nilai) / len(nilai))
```

Secara matematis:

```text
rata-rata = jumlah seluruh data / banyak data
```

Jika list kosong, pembagian tersebut tidak boleh dilakukan karena `len(nilai) == 0`.

```python
if len(nilai) > 0:
    rata_rata = sum(nilai) / len(nilai)
else:
    print("Data masih kosong")
```

---

# 5.5 Praktik Paralel — Daftar Nilai

## Versi Scratch

Buat List bernama `Nilai`. Minta jumlah siswa, lalu gunakan `repeat` untuk meminta nilai dan `add (answer) to [Nilai]`. Setelah seluruh data masuk, lakukan loop untuk menjumlahkan isi list.

Mental model Scratch:

```text
hapus semua isi Nilai
set total = 0
ask jumlah siswa
repeat jumlah_siswa
    ask nilai
    add answer to Nilai
end
repeat length of Nilai
    baca item ke-i
    tambahkan ke total
end
rata = total / length of Nilai
```

## Versi Python

```python
nilai = []
jumlah_data = int(input("Jumlah siswa: "))

for i in range(jumlah_data):
    n = float(input(f"Nilai siswa ke-{i + 1}: "))
    nilai.append(n)

if len(nilai) > 0:
    print("Data      :", nilai)
    print("Rata-rata :", sum(nilai) / len(nilai))
    print("Tertinggi :", max(nilai))
    print("Terendah  :", min(nilai))
else:
    print("Tidak ada data yang dimasukkan.")
```

### Pertanyaan penting

- Kapan list dibuat?
- Kapan data ditambahkan?
- Mengapa list tidak boleh di-reset di dalam loop?
- Apa yang terjadi jika `jumlah_data = 0`?

---

# 5.6 Pencarian Data

## Menggunakan `in`

```python
barang = ["buku", "pensil", "penghapus"]
keyword = input("Cari barang: ").lower()

if keyword in barang:
    print("Barang ditemukan")
else:
    print("Barang tidak ditemukan")
```

## Menggunakan loop

```python
barang = ["buku", "pensil", "penghapus"]
keyword = input("Cari barang: ").lower()
ditemukan = False

for item in barang:
    if item == keyword:
        ditemukan = True

if ditemukan:
    print("Barang ditemukan")
else:
    print("Barang tidak ditemukan")
```

Versi kedua lebih panjang tetapi penting karena menunjukkan logika pencarian secara eksplisit.

### Test wajib

- data pertama ditemukan;
- data terakhir ditemukan;
- data tidak ditemukan;
- list kosong.

---

# 5.7 Menghitung Data yang Memenuhi Kondisi

Contoh menghitung siswa lulus dan belum lulus:

```python
nilai = [80, 65, 90, 74, 75]
lulus = 0
belum_lulus = 0

for n in nilai:
    if n >= 75:
        lulus += 1
    else:
        belum_lulus += 1

print("Lulus       :", lulus)
print("Belum lulus :", belum_lulus)
```

Perhatikan bahwa ini menggabungkan tiga kompetensi lama:

```text
LIST + LOOP + CONDITION + COUNTER
```

P05 bukan materi yang berdiri sendiri. Ia mengintegrasikan konsep P02–P04.

---

# 5.8 Dictionary sebagai Data Terstruktur

Dictionary adalah kumpulan pasangan **key–value**.

```python
produk = {
    "nama": "Keyboard",
    "harga": 250000,
    "stok": 10
}
```

Akses value:

```python
print(produk["nama"])
print(produk["stok"])
```

Mengubah value:

```python
produk["stok"] = 9
```

Dictionary pada pertemuan ini **bukan database**. Tujuannya hanya memperkenalkan bahwa satu objek dapat memiliki beberapa atribut.

```text
produk
├── nama  : Keyboard
├── harga : 250000
└── stok  : 10
```

## `.get()` untuk akses yang lebih aman

```python
print(produk.get("nama"))
print(produk.get("warna", "tidak tersedia"))
```

Akses `produk["warna"]` ketika key tidak ada akan menghasilkan `KeyError`, sedangkan `.get()` dapat menyediakan nilai default.

---

# 5.9 List of Dictionaries

Untuk beberapa produk:

```python
produk = [
    {"nama": "Keyboard", "harga": 250000, "stok": 10},
    {"nama": "Mouse", "harga": 120000, "stok": 5},
    {"nama": "Headset", "harga": 300000, "stok": 4}
]
```

Pencarian sederhana:

```python
keyword = input("Nama produk: ").lower()
ditemukan = False

for item in produk:
    if item["nama"].lower() == keyword:
        print("Harga:", item["harga"])
        print("Stok :", item["stok"])
        ditemukan = True

if not ditemukan:
    print("Produk tidak ditemukan")
```

Struktur ini menjadi jembatan penting menuju project P08, karena banyak project CLI akan membutuhkan sekumpulan record sederhana.

---

# 5.10 Latihan Wajib

| No | Latihan | Konsep utama |
|---:|---|---|
| 1 | Statistik nilai | list, append, sum, min, max, average |
| 2 | Daftar belanja | tambah, tampilkan, cari, hapus |
| 3 | Stok barang | dictionary / list of dictionaries |
| 4 | Suhu harian | agregasi statistik |
| 5 | Voting sederhana | frekuensi/counter |
| 6 | Pencarian produk | search + dictionary |
| 7 | Debug index/key | IndexError + KeyError |

---

# 5.11 Boundary dan Failure Cases

Mahasiswa wajib membedakan:

### Normal case
Data tersedia dan valid.

### Boundary case
Contoh nilai `0`, `75`, `100`, list dengan satu elemen.

### Empty case
List belum memiliki data.

### Not-found case
Keyword yang dicari tidak ada.

### Invalid case
Nilai di luar aturan, misalnya nilai siswa `-1` atau `101`.

Contoh validasi:

```python
nilai_baru = float(input("Nilai: "))

if 0 <= nilai_baru <= 100:
    nilai.append(nilai_baru)
else:
    print("Nilai harus 0 sampai 100")
```

---

# 5.12 Troubleshooting

| Gejala | Kemungkinan penyebab | Pemeriksaan/perbaikan |
|---|---|---|
| `IndexError` | Index di luar panjang list | cek `len(list)` dan ingat index mulai 0 |
| `KeyError` | Key dictionary tidak tersedia | cek ejaan key atau gunakan `.get()` |
| Data tidak bertambah | `append()` tidak terpanggil | print list setelah penambahan |
| Data hilang setiap iterasi | list dibuat ulang di dalam loop | pindahkan inisialisasi list sebelum loop |
| `ZeroDivisionError` | menghitung rata-rata list kosong | validasi `len(data) > 0` |
| Pencarian selalu gagal | beda huruf besar/kecil/spasi | normalisasi dengan `.strip().lower()` |
| Jumlah lulus salah | counter di-reset di loop | buat counter sebelum loop |
| Data salah berubah | index yang diubah keliru | tampilkan index dan isi sebelum update |

---

# 5.13 Pola Debugging P05

Gunakan prosedur:

```text
REPRODUCE
→ LIHAT ISI LIST/DICTIONARY
→ CEK INDEX/KEY
→ CEK LOOP
→ CEK CONDITION
→ UBAH SATU HAL
→ RETEST
```

Untuk data structure, `print(data)` merupakan alat debugging sederhana yang sangat berguna.

---

# 5.14 Challenge Mandiri

Pilih satu:

1. Tambahkan fitur hapus data pada daftar belanja.
2. Tambahkan pencarian sebagian nama produk.
3. Tambahkan hitung jumlah nilai di atas rata-rata.
4. Tambahkan kategori `stok rendah` jika stok kurang dari 5.
5. Tambahkan rekap voting dan tampilkan kandidat dengan suara terbanyak tanpa library eksternal.

Setiap challenge harus memiliki minimal tiga test case.

---

# 5.15 Exit Ticket

- [ ] Saya dapat menjelaskan mengapa list diperlukan.
- [ ] Saya tahu index Python dimulai dari 0.
- [ ] Saya dapat melakukan loop pada list.
- [ ] Saya dapat menghitung statistik sederhana.
- [ ] Saya dapat mencari data dan menangani kondisi tidak ditemukan.
- [ ] Saya dapat menjelaskan dictionary sebagai key–value.
- [ ] Saya tahu penyebab umum `IndexError` dan `KeyError`.
- [ ] Saya dapat menjelaskan bagaimana P02–P04 digunakan kembali pada P05.
