# Materi Pertemuan 01 — Scratch: Algoritma Visual dan Dasar Pemrograman

> Disusun dari **Buku Panduan Praktik: Pemrograman Dasar hingga Full Stack, 16 Pertemuan Terstruktur (Edisi Agustus 2026)**.

## Target Kompetensi

- Menjelaskan input–process–output, sequence, event, condition, loop, dan variable.
- Membuat project Scratch yang mempunyai tujuan, aturan, skor, dan kondisi selesai.
- Melakukan debugging sederhana dengan menelusuri urutan blok.

## Filosofi Pertemuan

Materi dibuat dengan pola **mental model → contoh → praktik → challenge → debugging → refleksi**. Mahasiswa tidak cukup hanya membuat program “jalan”; mahasiswa harus dapat menjelaskan input, proses, keputusan, data, output, dan bukti pengujian.

## 1. Input – Process – Output

Algoritma adalah urutan langkah yang cukup jelas sehingga manusia atau komputer dapat mengikutinya.

```text
INPUT → PROCESS → OUTPUT
```

Contoh game:
1. pengguna menekan tombol panah;
2. program memeriksa event;
3. sprite bergerak;
4. jika sprite menyentuh koin, skor bertambah;
5. koin berpindah ke posisi acak.

## 2. Enam Pola Algoritma Dasar di Scratch

| Pola | Blok/Pola Scratch | Makna |
|---|---|---|
| Sequence | `when green flag` → beberapa blok | Instruksi berurutan |
| Event | `when [key] pressed` | Program bereaksi terhadap kejadian |
| Condition | `if <...> then` | Aksi hanya jika syarat benar |
| Loop | `repeat`, `forever` | Mengulang instruksi |
| State | `set [score] to 0` | Menyimpan keadaan program |
| Input | `ask ... and wait` | Menerima data pengguna |

## 3. Program Utama: Game Tangkap Koin

Komponen:
- Sprite `Pemain`
- Sprite `Koin`
- Variable `skor`
- Variable `target`

Alur:
- Green Flag: skor = 0, pemain di bawah, koin acak.
- Panah kiri/kanan menggerakkan pemain.
- Koin selalu memeriksa collision dengan pemain.
- Collision → skor +1 → suara → posisi acak.
- Jika skor mencapai target → tampilkan “MENANG” → stop all.

## 4. Debugging Scratch

Gunakan indikator visual (`say`, variable monitor, perubahan costume) untuk membuktikan apakah event/condition benar-benar terpanggil. Hindari langsung mengganti banyak blok sekaligus.

Gejala yang wajib dapat didiagnosis:
- sprite tidak bergerak;
- skor tidak bertambah;
- program berhenti terlalu cepat;
- loop terlalu cepat;
- koin tidak pernah berpindah.

## 5. Challenge

Tambahkan salah satu:
- nyawa;
- timer;
- benda berbahaya;
- level kesulitan;
- kecepatan koin bertambah setelah skor tertentu.
