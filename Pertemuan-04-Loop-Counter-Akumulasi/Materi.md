# Materi Pertemuan 04 — Scratch + Python Google Colab III: Loop, Counter, dan Akumulasi

> **Sumber utama:** *Buku Panduan Praktik: Pemrograman Dasar hingga Full Stack — 16 Pertemuan Terstruktur, Edisi Agustus 2026*.
>
> Pertemuan ini membahas pengulangan terkontrol: kapan memakai `repeat/for`, kapan memakai `forever/while`, bagaimana counter dan accumulator berubah tiap iterasi, serta bagaimana menemukan infinite loop dan off-by-one error. List belum diperlukan untuk latihan rata-rata lima nilai; pengolahan list dibahas pada Pertemuan 05.

## Target Kompetensi

Mahasiswa mampu:

- membedakan loop dengan jumlah iterasi diketahui dan tidak diketahui;
- menggunakan `for` bersama `range()`;
- menggunakan `while` berdasarkan condition;
- menggunakan counter dan accumulator;
- melakukan tracing nilai variable pada setiap iterasi;
- memahami sentinel sebagai penanda berhenti;
- menghindari infinite loop;
- membuat nested loop sederhana.

## Output Pertemuan

1. Simulasi loop di Scratch.
2. Program Python dengan `for` dan `while`.
3. Tabel tracing nilai variable setiap iterasi.
4. Minimal lima program latihan loop.
5. Catatan infinite-loop/off-by-one dan hasil perbaikan.

## Alur Pembelajaran 180 Menit

| Tahap | Durasi | Aktivitas |
|---|---:|---|
| Review | 15 menit | Condition dan test case dari Pertemuan 03 |
| Loop Scratch | 25 menit | `repeat`, `forever`, `repeat until` |
| Tracing | 20 menit | Counter dan perubahan variable |
| Python `for` | 30 menit | `range` dan iterasi diketahui |
| Python `while` | 25 menit | condition loop dan sentinel |
| Praktik | 45 menit | tabungan, nilai, tebak angka, kasir, pola |
| Debug | 20 menit | infinite loop dan off-by-one |

---

## 1. Mengapa Program Membutuhkan Loop?

Tanpa loop, instruksi berulang harus ditulis berkali-kali.

Tanpa loop:

```python
print("Latihan 1")
print("Latihan 2")
print("Latihan 3")
print("Latihan 4")
print("Latihan 5")
```

Dengan loop:

```python
for i in range(1, 6):
    print(f"Latihan {i}")
```

Loop mengurangi duplikasi dan membuat aturan pengulangan eksplisit.

---

## 2. Dua Pertanyaan sebelum Memilih Loop

### Pertanyaan A — Apakah jumlah pengulangan diketahui?

Jika diketahui, `for` biasanya lebih jelas.

```text
Ulangi 5 kali
Proses 10 hari
Minta tepat 5 nilai
```

### Pertanyaan B — Apakah pengulangan berhenti karena kondisi?

Jika jumlah iterasi belum diketahui, `while` biasanya lebih sesuai.

```text
Ulangi sampai jawaban benar
Terima data sampai sentinel 0
Ulangi selama saldo masih tersedia
```

Pemilihan loop harus berasal dari rule masalah, bukan dari kebiasaan.

---

## 3. Pemetaan Scratch ↔ Python

| Situasi | Scratch | Python |
|---|---|---|
| ulang tepat 10 kali | `repeat (10)` | `for i in range(10)` |
| berjalan terus | `forever` | `while True` |
| ulang sampai kondisi terpenuhi | `repeat until <kondisi>` | `while not kondisi` |
| tambah counter | `change counter by 1` | `counter += 1` |
| tambah accumulator | `change total by nilai` | `total += nilai` |

---

## 4. `for` dan `range()`

Bentuk umum:

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

Nilai stop **tidak ikut**. Ini sumber off-by-one error paling umum.

### Bentuk `range`

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

Contoh:

```python
for i in range(1, 6):
    print(i)
```

menghasilkan 1 sampai 5.

```python
for i in range(2, 11, 2):
    print(i)
```

menghasilkan 2, 4, 6, 8, 10.

### Cara mencegah off-by-one

Sebelum Run, tulis deret yang diinginkan secara manual, lalu cocokkan dengan `start`, `stop`, dan `step`.

---

## 5. Counter

Counter menyimpan jumlah kejadian atau iterasi.

```python
counter = 0

for i in range(5):
    counter += 1
    print(f"Iterasi ke-{counter}")
```

Counter biasanya:

1. diinisialisasi sebelum loop;
2. diperbarui di dalam loop;
3. dibaca selama atau setelah loop.

Jika counter di-reset di dalam loop, nilainya tidak akan terakumulasi.

---

## 6. Accumulator

Accumulator menyimpan hasil penjumlahan bertahap.

```python
total = 0

for i in range(1, 6):
    total += i
    print(i, total)
```

Perubahan nilai:

| Iterasi | i | total sebelum | Operasi | total sesudah |
|---:|---:|---:|---|---:|
| 1 | 1 | 0 | `0 + 1` | 1 |
| 2 | 2 | 1 | `1 + 2` | 3 |
| 3 | 3 | 3 | `3 + 3` | 6 |
| 4 | 4 | 6 | `6 + 4` | 10 |
| 5 | 5 | 10 | `10 + 5` | 15 |

Tracing seperti ini adalah alat utama untuk memahami loop.

---

## 7. Praktik Utama — Tabungan Harian

Program inti dari panduan:

```python
saldo = 0
hari = int(input("Berapa hari menabung? "))
setoran = float(input("Setoran per hari: "))

for i in range(1, hari + 1):
    saldo += setoran
    print(f"Hari {i}: saldo Rp{saldo:,.0f}")

print(f"Saldo akhir: Rp{saldo:,.0f}")
```

### IPO dan loop rule

```text
INPUT  : hari, setoran
PROCESS: ulangi hari kali; saldo = saldo + setoran
OUTPUT : saldo setiap hari dan saldo akhir
```

### Tracing contoh

Untuk 3 hari dan setoran 10.000:

| Iterasi | i | setoran | saldo sebelum | saldo sesudah |
|---:|---:|---:|---:|---:|
| 1 | 1 | 10.000 | 0 | 10.000 |
| 2 | 2 | 10.000 | 10.000 | 20.000 |
| 3 | 3 | 10.000 | 20.000 | 30.000 |

### Bug yang harus dipahami

Salah:

```python
for i in range(1, hari + 1):
    saldo = 0
    saldo += setoran
```

Karena `saldo` di-reset setiap iterasi, nilai tidak pernah mengakumulasi seluruh setoran.

---

## 8. Latihan — Bilangan Genap dalam Rentang

Cara sederhana tanpa list:

```python
awal = int(input("Awal: "))
akhir = int(input("Akhir: "))

for angka in range(awal, akhir + 1):
    if angka % 2 == 0:
        print(angka)
```

Condition dari Pertemuan 03 boleh dipakai di dalam loop. Fokus baru pada sesi ini adalah **pengulangannya**.

---

## 9. Latihan — Lima Nilai dan Rata-rata tanpa List

Panduan secara eksplisit meminta rata-rata lima nilai **tanpa list**.

```python
total = 0

for i in range(1, 6):
    nilai = float(input(f"Nilai ke-{i}: "))
    total += nilai

rata_rata = total / 5
print(f"Rata-rata = {rata_rata:.2f}")
```

Mengapa tanpa list? Agar mahasiswa fokus pada loop dan accumulator. List baru menjadi topik utama Pertemuan 05.

---

## 10. `while`

Bentuk umum:

```python
while kondisi:
    # aksi
    # perubahan state agar kondisi dapat berubah
```

Contoh counter:

```python
angka = 1
while angka <= 5:
    print(angka)
    angka += 1
```

Jika `angka += 1` dihapus, kondisi `angka <= 5` selalu true dan loop tidak berhenti.

---

## 11. Infinite Loop

Infinite loop terjadi ketika kondisi loop tidak pernah menjadi false atau tidak ada mekanisme berhenti.

```python
angka = 1
while angka <= 5:
    print(angka)
```

Pada contoh salah tersebut, `angka` tidak berubah.

### Checklist saat `while` tidak berhenti

1. Variable apa yang menentukan condition?
2. Apakah variable itu diperbarui di dalam loop?
3. Apakah arah perubahannya mendekati kondisi berhenti?
4. Apakah tipe datanya sesuai?
5. Apakah condition yang ditulis sama dengan rule?

---

## 12. Latihan — Tebak Angka sampai Benar

Pola utama:

```python
rahasia = 7
tebakan = int(input("Tebak angka: "))

while tebakan != rahasia:
    if tebakan < rahasia:
        print("Terlalu kecil")
    else:
        print("Terlalu besar")
    tebakan = int(input("Tebak lagi: "))

print("Benar")
```

Jumlah tebakan tidak diketahui sebelum program berjalan, sehingga `while` sesuai.

---

## 13. Sentinel

Sentinel adalah nilai khusus yang menandai akhir input. Pada contoh kasir latihan, sentinel `0` berarti selesai memasukkan data.

```python
total = 0
harga = float(input("Harga, 0 untuk selesai: "))

while harga != 0:
    total += harga
    harga = float(input("Harga, 0 untuk selesai: "))

print(f"Total = {total}")
```

Sentinel harus dipilih sehingga maknanya jelas dan tipenya konsisten dengan input.

---

## 14. Nested Loop

Nested loop adalah loop di dalam loop.

```python
for baris in range(1, 5):
    for kolom in range(baris):
        print("*", end="")
    print()
```

Output:

```text
*
**
***
****
```

**Outer loop** menentukan jumlah baris. **Inner loop** menentukan berapa simbol yang dicetak pada baris tersebut.

### Tracing nested loop

| baris | jumlah inner iteration | output baris |
|---:|---:|---|
| 1 | 1 | `*` |
| 2 | 2 | `**` |
| 3 | 3 | `***` |
| 4 | 4 | `****` |

---

## 15. `break` dan `continue` — Pengayaan Implementasi

Konsep inti panduan dapat diselesaikan tanpa `break/continue`, tetapi repository boleh menunjukkan penggunaannya sebagai pengayaan setelah mahasiswa memahami condition loop.

- `break` menghentikan loop saat ini.
- `continue` melewati sisa iterasi dan lanjut ke iterasi berikutnya.

Untuk penilaian inti, mahasiswa tetap harus dapat menjelaskan condition berhenti tanpa bergantung pada `break`.

---

## 16. Debugging Loop

| Gejala | Kemungkinan penyebab | Pemeriksaan/perbaikan |
|---|---|---|
| Loop tidak berhenti | condition selalu true | cek perubahan variable condition |
| Iterasi kurang satu | stop `range` tidak ikut | tulis deret expected |
| Iterasi lebih satu | start/stop salah | tracing indeks |
| Total selalu kecil/nol | accumulator di-reset di loop | inisialisasi sebelum loop |
| Sentinel tidak bekerja | nilai/type berbeda | print nilai dan tipe yang dibandingkan |
| Nested loop output aneh | inner loop salah range | tracing per baris |

## 17. Rangkuman

- `for` cocok saat jumlah iterasi diketahui.
- `while` cocok saat berhenti berdasarkan condition.
- `range` memiliki stop eksklusif.
- counter menghitung kejadian/iterasi.
- accumulator menyimpan hasil bertahap.
- sentinel adalah nilai penanda berhenti.
- accumulator diinisialisasi sebelum loop.
- nested loop mempunyai outer dan inner iteration.
- tracing adalah cara paling efektif memahami perubahan state.

## Exit Ticket

- [ ] Saya dapat memilih `for` atau `while` berdasarkan rule.
- [ ] Saya dapat menjelaskan `range(1, 6)`.
- [ ] Saya dapat membedakan counter dan accumulator.
- [ ] Saya dapat membuat tracing minimal tiga iterasi.
- [ ] Saya dapat menjelaskan infinite loop.
- [ ] Saya dapat menjelaskan sentinel.
- [ ] Saya dapat menjelaskan outer dan inner loop.
