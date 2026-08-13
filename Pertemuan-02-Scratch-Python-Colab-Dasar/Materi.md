# Materi Pertemuan 02 — Scratch + Python Google Colab I: Sequence, Input, Output, dan Variabel

> **Sumber utama:** *Buku Panduan Praktik: Pemrograman Dasar hingga Full Stack — 16 Pertemuan Terstruktur, Edisi Agustus 2026*.
>
> Pada pertemuan ini setiap algoritma dibuat dua kali: pertama secara visual di Scratch, kemudian ditulis sebagai Python di Google Colab. **Percabangan belum menjadi fokus pertemuan 2**; validasi dengan `if` dibahas pada Pertemuan 03, sedangkan function dibahas lebih lanjut pada Pertemuan 06.

## Target Kompetensi

Mahasiswa mampu:

- membuat notebook Google Colab dan menjalankan cell;
- menerjemahkan `say`, `set`, `ask`, dan operator Scratch ke `print`, variable, `input`, dan operator Python;
- mengenal tipe data `string`, `integer`, `float`, dan `boolean`;
- menggunakan konversi tipe sederhana `int()` dan `float()`;
- menggunakan operator aritmetika `+`, `-`, `*`, `/`, `//`, `%`, `**`;
- memprediksi output program sebelum menekan Run.

## Output Pertemuan

1. Notebook Colab berisi minimal empat latihan.
2. Project Scratch dan Python dengan alur input–process–output yang setara.
3. Catatan expected-versus-actual untuk setiap latihan utama.
4. Catatan error dasar seperti `NameError`, `ValueError`, dan `TypeError`.

## Alur Pembelajaran 180 Menit

| Tahap | Durasi | Aktivitas |
|---|---:|---|
| Review | 15 menit | Ulang input–process–output dan variable dari Scratch |
| Google Colab | 20 menit | Notebook, code cell, text cell, Run, reset runtime |
| Scratch pair | 25 menit | Biodata/kalkulator sederhana |
| Python dasar | 35 menit | `print`, variable, `input`, type conversion, operator |
| Terjemahkan algoritma | 40 menit | Scratch → pseudocode → Python |
| Challenge | 30 menit | Kalkulator biaya atau konversi |
| Debug | 15 menit | `NameError`, `ValueError`, salah tipe data |

---

## 1. Google Colab

Google Colab adalah lingkungan notebook berbasis browser. Notebook terdiri dari **text cell** dan **code cell**. Berbeda dari file Python biasa, cell dapat dijalankan tidak berurutan. Karena itu mahasiswa harus memahami bahwa nilai variable yang tersimpan di memory runtime tergantung cell mana yang sudah dijalankan.

### Kebiasaan yang benar

1. Beri judul notebook.
2. Gunakan text cell untuk tujuan dan catatan.
3. Jalankan code cell dari atas ke bawah.
4. Setelah mengubah banyak cell, gunakan **Restart/Reset runtime** lalu **Run all**.
5. Jangan menyimpulkan program benar hanya karena cell terakhir menghasilkan output.

### Contoh state notebook

Cell 1:

```python
harga = 12000
```

Cell 2:

```python
jumlah = 3
```

Cell 3:

```python
print(harga * jumlah)
```

Cell 3 hanya dapat berjalan jika variable `harga` dan `jumlah` sudah ada pada runtime.

---

## 2. Pemetaan Scratch ↔ Python

| Scratch | Python | Konsep |
|---|---|---|
| `say [Halo]` | `print("Halo")` | output |
| `set [nama] to [Ayu]` | `nama = "Ayu"` | assignment |
| `ask [Nama?] and wait` | `nama = input("Nama? ")` | input |
| `answer` | nilai hasil `input()` | data pengguna |
| `(5) + (3)` | `5 + 3` | operator |
| `join [Halo ] (nama)` | `f"Halo {nama}"` | komposisi string |

Tujuan penerjemahan bukan menghafal bentuk blok dan syntax, tetapi menyadari bahwa algoritmanya tetap sama.

---

## 3. Variable dan Assignment

Variable adalah nama yang menunjuk suatu nilai.

```python
nama = "Ayu"
umur = 19
ipk = 3.75
aktif = True
```

Tanda `=` pada assignment dibaca **“simpan nilai di kanan ke variable di kiri”**, bukan sebagai pernyataan matematika “sama dengan”.

### Aturan nama variable

Gunakan nama yang menjelaskan data:

```python
harga_satuan = 15000
jumlah_barang = 3
```

Hindari nama seperti `a`, `x1`, `temp2` bila tidak ada alasan jelas.

---

## 4. Tipe Data Dasar

| Tipe | Contoh | Kegunaan |
|---|---|---|
| `str` | `"Bandung"` | teks |
| `int` | `25` | bilangan bulat |
| `float` | `12.5` | bilangan desimal |
| `bool` | `True`, `False` | nilai logika |

`input()` menghasilkan string. Bila input akan dihitung, lakukan konversi.

```python
umur = int(input("Umur: "))
harga = float(input("Harga: "))
```

### Mengapa konversi penting?

Tanpa konversi:

```python
jumlah = input("Jumlah: ")
print(jumlah + jumlah)
```

Jika pengguna memasukkan `3`, hasilnya menjadi string `33`, bukan angka `6`.

---

## 5. Output dengan `print()` dan f-string

```python
nama = input("Nama: ")
umur = int(input("Umur: "))
print(f"Halo {nama}, umur kamu {umur} tahun.")
```

f-string membuat output lebih mudah dibaca daripada banyak operasi penggabungan string.

Format angka:

```python
total = 37500
print(f"Rp{total:,.0f}")
```

---

## 6. Operator Aritmetika

| Operator | Arti | Contoh | Hasil |
|---|---|---|---:|
| `+` | tambah | `7 + 3` | 10 |
| `-` | kurang | `7 - 3` | 4 |
| `*` | kali | `7 * 3` | 21 |
| `/` | bagi | `7 / 2` | 3.5 |
| `//` | pembagian bulat | `7 // 2` | 3 |
| `%` | sisa bagi | `7 % 2` | 1 |
| `**` | pangkat | `2 ** 3` | 8 |

### Prioritas operasi

Python mengikuti prioritas operator matematika. Bila formula panjang, gunakan tanda kurung untuk memperjelas maksud.

```python
rata_rata = (nilai1 + nilai2 + nilai3) / 3
```

---

## 7. Praktik Utama — Kalkulator Belanja

Soal: program meminta nama barang, harga satuan, dan jumlah pembelian, kemudian menghitung total.

```python
nama_barang = input("Nama barang: ")
harga = float(input("Harga satuan: "))
jumlah = int(input("Jumlah: "))
total = harga * jumlah

print(f"Barang : {nama_barang}")
print(f"Jumlah : {jumlah}")
print(f"Total  : Rp{total:,.0f}")
```

### IPO

```text
INPUT  : nama_barang, harga, jumlah
PROCESS: total = harga × jumlah
OUTPUT : nama barang, jumlah, total
```

Perhatikan bahwa program inti ini **belum menggunakan `if`**. Jika pengguna memasukkan teks ketika diminta angka, Python dapat menghasilkan `ValueError`. Pada pertemuan ini error tersebut diamati dan dibaca; strategi validasi input akan dibahas pada Pertemuan 03.

---

## 8. Latihan Bertingkat

### Level A — Luas Persegi Panjang

```python
panjang = float(input("Panjang: "))
lebar = float(input("Lebar: "))
luas = panjang * lebar
print(f"Luas = {luas}")
```

Fokus: variable, float, operator.

### Level A — Konversi Menit

```python
total_menit = int(input("Total menit: "))
jam = total_menit // 60
sisa_menit = total_menit % 60
print(f"{jam} jam {sisa_menit} menit")
```

Fokus: `//` dan `%`.

### Level B — Total Tiga Jenis Barang

Gunakan tiga pasang harga dan jumlah, hitung subtotal tiap jenis, lalu total akhir. Fokusnya tetap sequence, variable, input, dan operator.

### Level B — Konversi Suhu

```python
celsius = float(input("Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15
print(f"Fahrenheit = {fahrenheit:.2f}")
print(f"Kelvin = {kelvin:.2f}")
```

### Level C — Estimasi Biaya Perjalanan

Model sederhana:

```text
liter_dibutuhkan = jarak_km / km_per_liter
biaya = liter_dibutuhkan × harga_per_liter
```

Pada versi inti mahasiswa memasukkan data yang valid. Pemeriksaan syarat seperti `km_per_liter > 0` menjadi bahan transisi ke Pertemuan 03.

---

## 9. Prediksi Sebelum Run

Sebelum menjalankan kode, isi tabel:

| Input | Formula | Prediksi output | Actual | Sesuai? |
|---|---|---|---|:---:|
| harga=10000, jumlah=3 | 10000×3 | 30000 |  | ☐ |
| menit=125 | `//60`, `%60` | 2 jam 5 menit |  | ☐ |
| C=0 | C×9/5+32 | 32 F |  | ☐ |

Prediksi membuat mahasiswa membandingkan perilaku program dengan algoritma, bukan hanya menerima output komputer.

---

## 10. Error Dasar yang Wajib Dipahami

| Error/gejala | Contoh penyebab | Cara membaca |
|---|---|---|
| `NameError` | nama variable salah | lihat nama yang disebut traceback dan barisnya |
| `ValueError` | `int("abc")` | konversi tipe gagal karena isi tidak sesuai |
| `TypeError` | operasi tipe yang tidak cocok | periksa tipe operand |
| Output lama di Colab | cell tidak berurutan | Restart runtime lalu Run all |

### Latihan membaca error

Buat salinan kode, ubah satu nama variable, jalankan, lalu catat:

```text
Jenis error:
Baris:
Nama variable yang bermasalah:
Expected:
Actual:
Perbaikan:
Hasil run ulang:
```

---

## 11. Pengayaan Implementasi Repository

Folder `praktikum/` menyediakan:

- versi Scratch untuk algoritma utama;
- file `.py` yang dapat dijalankan lokal;
- notebook `.ipynb` untuk Colab;
- test otomatis untuk fungsi perhitungan murni **hanya sebagai alat verifikasi repository**. Test otomatis bukan materi function untuk mahasiswa pada sesi ini; program pembelajaran utama tetap ditulis secara berurutan sesuai scope Pertemuan 02.

## 12. Rangkuman

- Scratch dan Python dapat mewakili algoritma yang sama.
- `input()` menerima data, assignment menyimpan data, operator memproses data, `print()` menampilkan hasil.
- `input()` menghasilkan string sehingga data numerik perlu dikonversi.
- `//` menghasilkan pembagian bulat, `%` menghasilkan sisa bagi.
- Colab menyimpan state runtime; Restart + Run all membantu memastikan urutan yang benar.
- Error dibaca dari bukti yang ditampilkan, bukan ditebak.

## Exit Ticket

- [ ] Saya dapat menjelaskan padanan `ask` dan `say` di Python.
- [ ] Saya tahu hasil `input()` adalah string.
- [ ] Saya dapat memilih `int` atau `float` sesuai data.
- [ ] Saya dapat menjelaskan `/`, `//`, dan `%`.
- [ ] Saya dapat memprediksi output sebelum Run.
- [ ] Saya dapat membaca `NameError` atau `ValueError` sederhana.
