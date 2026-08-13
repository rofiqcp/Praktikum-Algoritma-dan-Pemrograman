# Materi Pertemuan 01 — Scratch: Belajar Berpikir seperti Programmer

> **Sumber utama:** *Buku Panduan Praktik: Pemrograman Dasar hingga Full Stack — 16 Pertemuan Terstruktur, Edisi Agustus 2026*.
>
> Pertemuan ini **hanya menggunakan Scratch** melalui `https://scratch.mit.edu/`. Tidak ada Python pada sesi pertama. Bagian **Pengayaan implementasi repository** menambahkan contoh pengujian dan dokumentasi agar praktikum siap dipakai tanpa mengubah urutan kompetensi buku.

## Daftar Isi

1. Target kompetensi dan output
2. Alur pembelajaran 180 menit
3. Mental model algoritma
4. Input–Process–Output
5. Antarmuka Scratch
6. Sequence
7. Event
8. Variable dan state
9. Condition
10. Loop
11. Sensing dan operator
12. Praktik utama: Game Tangkap Koin
13. Flowchart dan pseudocode
14. Pengujian
15. Debugging
16. Challenge
17. Rangkuman dan exit ticket

---

## 1. Target Kompetensi

Setelah menyelesaikan pertemuan ini, mahasiswa diharapkan mampu:

- menjelaskan konsep **input–process–output** dengan bahasa sendiri;
- membedakan **sequence**, **event**, **condition**, dan **loop**;
- menggunakan **variable** untuk menyimpan skor atau nilai program;
- membuat satu program Scratch yang memiliki tujuan dan aturan yang jelas;
- melakukan debugging sederhana dengan melihat urutan blok dan perubahan state.

## 2. Output Pertemuan

Mahasiswa menghasilkan:

1. satu project Scratch yang dapat dimainkan atau dijalankan;
2. flowchart sederhana dari program;
3. catatan minimal tiga bug yang ditemukan beserta cara memperbaikinya;
4. tabel pengujian expected-versus-actual;
5. satu modifikasi mandiri terhadap program utama.

## 3. Alur Pembelajaran 180 Menit

| Tahap | Durasi | Aktivitas utama | Bukti belajar |
|---|---:|---|---|
| Pembukaan | 15 menit | Contoh algoritma sehari-hari: membuat mi, login, menyeberang jalan | Mahasiswa dapat menyebut input, proses, output |
| Mengenal Scratch | 25 menit | Stage, sprite, block palette, code area, costumes, sounds | Mahasiswa dapat menunjukkan fungsi tiap area |
| Sequence & event | 25 menit | Gerak sprite dari Green Flag dan keyboard | Sprite bereaksi sesuai event |
| Variable & condition | 30 menit | Skor, target, aturan menang/kalah | Nilai state terlihat berubah |
| Loop & sensing | 30 menit | `repeat`, `forever`, `touching`, `ask/answer` | Program memeriksa kondisi berulang |
| Praktik utama | 40 menit | Mini game tangkap benda | Game dapat dimainkan |
| Debug & refleksi | 15 menit | Membuat bug sengaja, mengamati, memperbaiki | Minimal tiga catatan debugging |

---

## 4. Mental Model Algoritma

Algoritma adalah urutan langkah yang cukup jelas sehingga manusia atau komputer dapat mengikutinya. Sebelum memilih blok Scratch, tuliskan dahulu program dalam kalimat biasa.

Contoh algoritma gerak:

```text
1. Program menunggu tombol panah.
2. Pengguna menekan panah kanan.
3. Event panah kanan dijalankan.
4. Nilai posisi x pemain ditambah 10.
5. Stage menampilkan pemain pada posisi baru.
```

Contoh algoritma tangkap koin:

```text
1. Program memulai skor dari 0.
2. Koin ditempatkan pada posisi acak.
3. Program terus memeriksa apakah koin menyentuh pemain.
4. Jika menyentuh pemain, skor bertambah 1.
5. Koin dipindahkan ke posisi acak baru.
6. Jika skor mencapai target, game selesai.
```

Sebelum program dibuat, jawab tiga pertanyaan: **apa input-nya, apa prosesnya, dan apa output-nya?**

## 5. Input–Process–Output

```text
INPUT → PROCESS → OUTPUT
```

| Contoh | Input | Process | Output |
|---|---|---|---|
| Gerak pemain | Tombol panah | Ubah koordinat x/y | Sprite berpindah |
| Biodata | Jawaban pengguna | Simpan ke variable | Sapaan muncul |
| Tangkap koin | Collision pemain-koin | Tambah skor, pindah koin | Skor dan posisi baru |
| Menang | Skor saat ini | Bandingkan dengan target | Pesan MENANG, game berhenti |

Kesalahan yang sering terjadi pada pemula adalah langsung menyusun blok tanpa mengetahui proses yang ingin dibangun. Akibatnya blok dapat terlihat banyak, tetapi alur program sulit dijelaskan dan sulit di-debug.

---

## 6. Mengenal Antarmuka Scratch

| Komponen | Fungsi | Hal yang harus diamati |
|---|---|---|
| **Stage** | Tempat hasil program terlihat | posisi, gerak, pesan, backdrop |
| **Sprite** | Objek/karakter yang memiliki script | sprite aktif menentukan script yang diedit |
| **Block Palette** | Kumpulan blok per kategori | Motion, Looks, Sound, Events, Control, Sensing, Operators, Variables |
| **Code Area** | Tempat menyusun blok | urutan dan hubungan antarblok |
| **Costumes** | Tampilan/pose sprite | dapat dipakai membuat animasi |
| **Sounds** | Audio yang dapat dipicu | dipakai sebagai feedback event |

### 6.1 Kategori blok yang dipakai

- **Events:** `when green flag clicked`, `when [key] pressed`, `broadcast`.
- **Motion:** `go to x:y`, `change x by`, `change y by`.
- **Looks:** `say ... for ... seconds`.
- **Sound:** `start sound`.
- **Control:** `if`, `if else`, `repeat`, `forever`, `wait`, `stop all`.
- **Sensing:** `touching`, `ask ... and wait`, `answer`.
- **Operators:** perbandingan, `join`, angka acak.
- **Variables:** `set ... to`, `change ... by`.

---

## 7. Sequence — Urutan Instruksi

Sequence berarti instruksi dijalankan berurutan dari atas ke bawah setelah event pemicu aktif.

```text
when green flag clicked
set [skor] to (0)
go to x: (0) y: (-120)
say [Siap!] for (1) seconds
```

Urutan tersebut berarti skor di-reset, posisi pemain diinisialisasi, lalu pesan tampil. Bila urutan diubah, perilaku awal program dapat berubah.

### Prediksi sebelum menjalankan

Sebelum klik Green Flag, jawab:

1. Berapa nilai `skor` setelah blok pertama?
2. Di koordinat mana sprite berada?
3. Pesan apa yang terlihat terakhir?

Kebiasaan **prediksi → run → bandingkan** menjadi dasar debugging pada pertemuan berikutnya.

---

## 8. Event — Program Bereaksi terhadap Kejadian

Event adalah pemicu. Pada Scratch, beberapa script dapat menunggu event yang berbeda secara bersamaan.

```text
when [right arrow] key pressed
change x by (10)

when [left arrow] key pressed
change x by (-10)
```

Script tombol kanan dan kiri tidak harus berada di bawah Green Flag. Keduanya adalah handler event yang berdiri sendiri.

Event utama game:

- Green Flag → reset game;
- panah kiri/kanan → gerakkan pemain;
- broadcast `MENANG` → jalankan respons akhir.

---

## 9. Variable dan State

Variable menyimpan nilai yang dapat berubah selama program berjalan. Nilai tersebut membentuk **state** atau keadaan program saat ini.

Pada Game Tangkap Koin gunakan:

| Variable | Nilai awal | Makna |
|---|---:|---|
| `skor` | 0 | jumlah koin yang berhasil ditangkap |
| `target` | 10 | skor minimum untuk menang |
| `gameAktif` | 1 | 1 = game berjalan, 0 = selesai |

### Prinsip inisialisasi

State yang harus kembali ke kondisi awal ditempatkan pada Green Flag.

```text
when green flag clicked
set [skor] to (0)
set [target] to (10)
set [gameAktif] to (1)
```

Jika `skor` tidak di-reset, run kedua dapat mewarisi nilai dari run sebelumnya. Ini contoh bug state yang penting dipahami.

---

## 10. Condition — Keputusan Berdasarkan Kondisi

Condition membuat program memilih apakah sebuah aksi perlu dilakukan.

```text
if <touching [Pemain] ?> then
    change [skor] by (1)
end
```

Condition mempunyai hasil true atau false. Perubahan skor hanya terjadi jika koin sedang menyentuh pemain.

Condition menang:

```text
if <(skor) >= (target)> then
    broadcast [MENANG]
end
```

Menggunakan `>=` membuat kondisi tetap benar bila skor tepat pada target atau melewatinya.

---

## 11. Loop — Pengulangan

Loop digunakan ketika pemeriksaan atau aksi harus dilakukan berulang.

| Blok | Kapan digunakan | Contoh |
|---|---|---|
| `repeat (10)` | jumlah pengulangan diketahui | animasi 10 langkah |
| `forever` | terus berjalan selama program aktif | memeriksa collision |
| `repeat until` | berhenti saat kondisi tercapai | variasi permainan |

Collision tidak cukup diperiksa satu kali karena pemain dapat menyentuh koin kapan saja:

```text
forever
    if <touching [Pemain] ?> then
        ...
    end
end
```

### Mengapa ada `wait` kecil setelah collision?

Jika sprite masih saling menyentuh selama beberapa frame, loop dapat menambah skor berkali-kali. Memindahkan koin segera dan memberi jeda kecil membuat satu collision lebih mudah diamati sebagai satu kejadian.

---

## 12. Sensing dan Operator

### 12.1 `ask` dan `answer`

```text
ask [Siapa nama kamu?] and wait
set [nama] to (answer)
say (join [Halo ] (nama)) for (2) seconds
```

`ask` adalah input, `answer` adalah nilai input terbaru, dan `say` adalah output.

### 12.2 `touching`

Blok `touching [sprite]?` menghasilkan true/false sehingga dapat dipakai sebagai syarat `if`.

### 12.3 `pick random`

```text
go to x: (pick random (-200) to (200)) y: (pick random (-80) to (150))
```

Koin dipindah ke posisi acak agar permainan tidak selalu sama.

---

## 13. Praktik Utama — Game Tangkap Koin

Spesifikasi blok lengkap berada pada folder `praktikum/`.

### 13.1 Komponen minimum

- Sprite `Pemain` dan `Koin`;
- variable `skor`, `target`, `gameAktif`;
- event Green Flag;
- event panah kiri/kanan;
- loop collision;
- condition menang;
- feedback suara/pesan.

### 13.2 Urutan pembangunan

1. Pastikan pemain dapat bergerak.
2. Tambahkan variable dan reset state.
3. Tambahkan koin serta posisi acak.
4. Uji collision dengan indikator `say` sebelum skor.
5. Setelah collision terbukti, tambahkan skor.
6. Tambahkan target menang.
7. Uji target kecil (`target = 1`).
8. Baru tambahkan sound, costume, atau challenge.

Dengan membangun bertahap, area masalah lebih mudah diketahui ketika sesuatu gagal.

---

## 14. Flowchart dan Pseudocode

Pseudocode ringkas:

```text
START
skor ← 0
target ← 10
gameAktif ← 1
letakkan pemain di posisi awal
letakkan koin di posisi acak

SELAMA gameAktif = 1
    layani event gerak pemain
    jika koin menyentuh pemain
        skor ← skor + 1
        bunyikan feedback
        pindahkan koin
    jika skor >= target
        gameAktif ← 0
        tampilkan MENANG
        hentikan program
END
```

Scratch bersifat event-driven, sehingga event tombol dan loop collision dapat berada pada script berbeda. Flowchart menyederhanakan beberapa script menjadi gambaran logika.

---

## 15. Pengujian Program

Program tidak dinyatakan benar hanya karena “kelihatan jalan”. Gunakan expected dan actual.

| No | Kasus | Expected |
|---:|---|---|
| 1 | Green Flag setelah skor pernah berubah | skor kembali 0 |
| 2 | Panah kanan sekali | x bertambah sesuai step |
| 3 | Panah kiri sekali | x berkurang sesuai step |
| 4 | Koin tidak menyentuh pemain | skor tetap |
| 5 | Koin menyentuh pemain sekali | skor bertambah tepat 1 |
| 6 | Skor mencapai target | pesan MENANG dan game berhenti |
| 7 | Run ulang setelah menang | state kembali ke awal |

### Pengayaan implementasi repository

Mahasiswa membuat minimal dua test case sendiri, misalnya target=1, koordinat batas Stage, atau test fitur challenge.

---

## 16. Debugging Berbasis Bukti

Gunakan urutan:

```text
REPRODUCE → AMATI → LOKALISASI → HIPOTESIS → UBAH SATU HAL → RETEST
```

| Gejala | Kemungkinan penyebab | Bukti yang dapat dipasang | Perbaikan |
|---|---|---|---|
| Sprite tidak bergerak | event/sprite salah | `say [RIGHT]` pada handler | cek sprite dan event |
| Skor tidak bertambah | touching tidak true/variable salah | monitor skor dan `say [HIT]` | cek condition dan variable |
| Skor naik terlalu cepat | collision dihitung berulang | monitor skor saat overlap | pindahkan koin, beri jeda kecil |
| Game langsung selesai | target/state salah | monitor `skor`, `target`, `gameAktif` | reset nilai pada Green Flag |
| Koin tidak pindah | random tidak terpanggil | klik blok random manual | letakkan pada branch collision |
| Program berhenti aneh | `stop all` terlalu awal | telusuri control | pindahkan stop ke kondisi akhir |

Format catatan bug:

```text
Bug / gejala:
Langkah reproduce:
Expected:
Actual:
Bukti yang diamati:
Hipotesis penyebab:
Perubahan yang dilakukan:
Hasil retest:
```

Minimal tiga bug dicatat dalam laporan.

---

## 17. Challenge Mandiri

Pilih satu:

- **Nyawa:** tambah variable `nyawa`, tentukan kapan berkurang dan kapan kalah.
- **Timer:** batasi permainan dengan waktu tertentu.
- **Benda berbahaya:** collision mengurangi skor/nyawa.
- **Level:** setelah skor tertentu, ubah kecepatan atau aturan.

Mahasiswa harus menjelaskan **variable baru**, **condition baru**, dan **test case baru**. Challenge bukan sekadar mengganti costume atau warna.

---

## 18. Rangkuman

- Sequence menentukan urutan instruksi.
- Event menentukan kapan script merespons.
- Variable menyimpan state.
- Condition membuat keputusan.
- Loop mengulang aksi/pemeriksaan.
- Sensing memberi data kondisi lingkungan program.
- Debugging dilakukan berdasarkan bukti.

## 19. Exit Ticket

- [ ] Saya dapat menunjukkan input, process, dan output program.
- [ ] Saya dapat menunjukkan event utama.
- [ ] Saya dapat menjelaskan sequence awal game.
- [ ] Saya dapat menyebutkan minimal dua condition.
- [ ] Saya tahu variable apa yang menyimpan state.
- [ ] Saya dapat menjelaskan mengapa loop collision diperlukan.
- [ ] Saya dapat menunjukkan satu bug dan bukti perbaikannya.
