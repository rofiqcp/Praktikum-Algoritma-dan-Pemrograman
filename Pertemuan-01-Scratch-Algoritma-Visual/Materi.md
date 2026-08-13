# Materi Pertemuan 01 — Scratch: Belajar Berpikir seperti Programmer

> **Sumber utama:** *Buku Panduan Praktik: Pemrograman Dasar hingga Full Stack — 16 Pertemuan Terstruktur, Edisi Agustus 2026*. Isi materi di bawah mengikuti urutan, istilah, target kompetensi, praktik, dan troubleshooting dari buku panduan. Contoh executable yang sudah dirapikan berada di folder `praktikum/`.

Pertemuan ini hanya menggunakan Scratch melalui https://scratch.mit.edu/. Tidak ada Python pada sesi pertama.

## Target Kompetensi

- Menjelaskan konsep input–process–output dengan bahasa sendiri.
- Membedakan sequence, event, condition, dan loop.
- Menggunakan variable untuk menyimpan skor/nilai.
- Membuat satu program Scratch yang mempunyai tujuan dan aturan.
- Melakukan debugging sederhana dengan melihat urutan blok.

## Output Pertemuan

- Satu project Scratch yang dapat dimainkan/dijalankan.
- Flowchart sederhana dari program.
- Catatan tiga bug yang ditemukan dan cara memperbaikinya.

## Alur Pengajaran 180 Menit

| Tahap | Durasi | Aktivitas |
|---|---:|---|
| Pembukaan | 15 | Contoh algoritma sehari-hari: membuat mi, login, menyeberang jalan. |
| Kenali Scratch | 25 | Stage, sprite, block palette, code area, costumes, sounds. |
| Sequence & event | 25 | Gerak sprite berdasarkan green flag dan keyboard. |
| Variable & condition | 30 | Skor, nyawa, menang/kalah. |
| Loop & sensing | 30 | Repeat/forever, touching, ask/answer. |
| Praktik utama | 40 | Mini game tangkap benda atau maze sederhana. |
| Debug & refleksi | 15 | Ubah satu blok sengaja untuk membuat bug, lalu perbaiki. |

## 1.1 Mental Model Algoritma

Algoritma adalah urutan langkah yang cukup jelas sehingga manusia atau komputer dapat mengikutinya. Sebelum memilih blok Scratch, peserta harus mampu menjelaskan langkah program dalam kalimat biasa.

```text
INPUT → PROCESS → OUTPUT
```

Contoh: pengguna menekan tombol panah → program memeriksa tombol → sprite bergerak 10 langkah. Dalam game: sprite menyentuh koin → skor bertambah → koin pindah ke posisi acak.

## 1.2 Komponen Antarmuka Scratch

| Komponen | Fungsi | Pertanyaan pengajar |
|---|---|---|
| Stage | Tempat hasil program terlihat. | Apa yang berubah di layar ketika blok dijalankan? |
| Sprite | Objek/karakter yang memiliki script. | Objek mana yang bertanggung jawab atas aksi ini? |
| Block Palette | Kumpulan instruksi per kategori. | Blok ini termasuk gerak, kontrol, sensing, atau operator? |
| Code Area | Tempat menyusun blok menjadi program. | Blok mana yang dijalankan lebih dulu? |
| Costumes | Tampilan/pose sprite. | Bagaimana membuat animasi tanpa mengganti sprite? |
| Sounds | Suara yang dapat dipicu event. | Kapan suara harus dimainkan? |

## 1.3 Enam Pola Algoritma Dasar

| Pola | Contoh Scratch | Makna |
|---|---|---|
| Sequence | `when green flag → go to x/y → say` | Instruksi berurutan. |
| Event | `when key pressed` | Program bereaksi terhadap kejadian. |
| Condition | `if touching edge then ...` | Aksi hanya dilakukan jika kondisi benar. |
| Loop | `repeat 10 / forever` | Instruksi diulang. |
| State/Variable | `set score to 0` | Program menyimpan keadaan. |
| Input | `ask ... and wait` | Program menerima data pengguna. |

## 1.4 Praktik: Game Tangkap Koin

1. Buat sprite pemain dan sprite koin.
2. Saat green flag: set skor = 0, letakkan pemain di bawah, koin di posisi acak.
3. Gunakan event tombol kiri/kanan untuk menggerakkan pemain.
4. Pada sprite koin gunakan `forever` untuk memeriksa apakah menyentuh pemain.
5. Jika menyentuh pemain: ubah skor +1, mainkan suara singkat, pindahkan koin ke posisi acak.
6. Tambahkan target skor; jika skor mencapai target, tampilkan pesan menang dan hentikan permainan.

**Challenge:** tambahkan nyawa, timer, atau benda berbahaya. Peserta harus menjelaskan variable apa yang ditambah dan condition apa yang berubah.

## 1.5 Troubleshooting Scratch

| Gejala | Kemungkinan penyebab | Langkah pemeriksaan/perbaikan |
|---|---|---|
| Sprite tidak bergerak | Event tidak terhubung atau script ada pada sprite lain. | Klik sprite yang benar, cek event paling atas, uji dengan blok `say`. |
| Skor tidak bertambah | Condition tidak pernah true atau variable berbeda. | Tampilkan nilai score dan uji touching dengan indikator visual. |
| Program berhenti aneh | Blok `stop all/stop script` terpanggil terlalu cepat. | Telusuri blok control dan pindahkan stop ke kondisi akhir. |
| Sprite bergerak terlalu cepat | Forever tanpa wait atau step terlalu besar. | Tambahkan wait kecil atau kecilkan langkah gerak. |
| Koin tidak pindah | Blok random berada di script yang tidak terpanggil. | Klik blok secara manual lalu cek event/condition. |

## 1.6 Exit Ticket

- [ ] Saya dapat menunjukkan event utama program.
- [ ] Saya dapat menyebutkan minimal dua condition.
- [ ] Saya tahu variable apa yang menyimpan skor.
- [ ] Saya dapat menjelaskan mengapa loop diperlukan.
