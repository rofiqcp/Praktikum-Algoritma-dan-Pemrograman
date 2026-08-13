# Praktikum Algoritma dan Pemrograman — Branch v1

Repository ini mengimplementasikan **16 pertemuan terstruktur** dari buku panduan *Scratch → Python → Web → API → Deployment → Node.js → Database → Full Stack*.

## Struktur Standar

Setiap pertemuan memiliki:
- `Materi.md`
- `Jobsheet.md`
- `TugasVideo.md`

Khusus **Pertemuan 08, 12, dan 16**, `TugasVideo.md` diganti dengan **`Project.md`** sesuai checkpoint/final project.

Setiap folder juga memiliki `praktikum/` yang berisi contoh program/instruksi yang wajib dijalankan.

## Peta Pertemuan

| No | Topik | Lingkungan utama | Output runnable |
|---:|---|---|---|
| 01 | [Scratch: Algoritma Visual dan Dasar Pemrograman](Pertemuan-01-Scratch-Algoritma-Visual/) | Scratch | `praktikum/` |
| 02 | [Scratch + Python Colab I: Sequence, Input, Output, dan Variabel](Pertemuan-02-Scratch-Python-Colab-Dasar/) | Scratch + Google Colab | `praktikum/` |
| 03 | [Scratch + Python Colab II: Percabangan, Operator Logika, dan Validasi](Pertemuan-03-Percabangan-Validasi/) | Scratch + Google Colab | `praktikum/` |
| 04 | [Scratch + Python Colab III: Loop, Counter, dan Akumulasi](Pertemuan-04-Loop-Counter-Akumulasi/) | Scratch + Google Colab | `praktikum/` |
| 05 | [Scratch + Python Colab IV: List, Data, Pencarian, dan Statistik](Pertemuan-05-List-Data-Statistik/) | Scratch + Google Colab | `praktikum/` |
| 06 | [Scratch + Python Colab V: Function, Dekomposisi, dan Debugging](Pertemuan-06-Function-Debugging/) | Scratch + Google Colab | `praktikum/` |
| 07 | [VS Code, Python Lokal, Git, dan GitHub](Pertemuan-07-VSCode-Git-GitHub/) | VS Code + Python + Git | `praktikum/` |
| 08 | [Project Checkpoint 1: Algoritma + Python Lokal + GitHub](Pertemuan-08-Project-Checkpoint-1/) | VS Code + Python + Git | `praktikum/` |
| 09 | [Python Web Programming dengan Flask](Pertemuan-09-Python-Web-Flask/) | Flask/Browser | `praktikum/` |
| 10 | [Python API: HTTP, JSON, REST, dan Integrasi](Pertemuan-10-Python-API-REST/) | Flask/Browser | `praktikum/` |
| 11 | [Deployment: GitHub ke Aplikasi Publik](Pertemuan-11-Deployment/) | Flask/Browser | `praktikum/` |
| 12 | [Project Checkpoint 2: Python Web + API + Deployment](Pertemuan-12-Project-Checkpoint-2/) | Flask/Browser | `praktikum/` |
| 13 | [Node.js, npm, Express, dan Web Lokal](Pertemuan-13-NodeJS-Express/) | Node.js/Express | `praktikum/` |
| 14 | [Integrasi Node.js + Python Backend + SQLite](Pertemuan-14-Node-Python-SQLite/) | Node.js + Python + SQLite | `praktikum/` |
| 15 | [Node + Python + Database Terstruktur](Pertemuan-15-Fullstack-Structured-Backend/) | Node.js + Python + SQLite | `praktikum/` |
| 16 | [Final Project: Full Stack Node.js + Python + Database](Pertemuan-16-Final-Project/) | Node.js + Python + SQLite | `praktikum/` |

## Jalur Belajar

1. **Pertemuan 1**: algoritma visual di Scratch.
2. **Pertemuan 2–6**: algoritma yang sama diterjemahkan ke Python/Google Colab.
3. **Pertemuan 7–8**: workflow developer lokal, VS Code, Git/GitHub, checkpoint CLI.
4. **Pertemuan 9–12**: Python web, REST API, deployment, checkpoint web/API.
5. **Pertemuan 13–16**: Node.js, integrasi multi-service, database relasional, final full stack.

## Aturan Menjalankan

Baca `Jobsheet.md` pada setiap pertemuan. Jangan lompat langsung ke project akhir. Setiap mahasiswa harus menyimpan bukti:
- command yang dijalankan;
- output/response;
- test case;
- error yang ditemukan;
- perubahan yang dilakukan;
- commit Git.

## Catatan Scratch

GitHub tidak dapat mengeksekusi project Scratch secara native. Untuk materi Scratch, folder `praktikum/` berisi **script blok yang presisi langkah demi langkah** yang harus direkonstruksi dan dijalankan di Scratch. Pertemuan 2–6 juga menyediakan program Python/Notebook setara untuk membandingkan algoritma yang sama.

## Keamanan

Jangan commit `.env`, password, token, API key, atau data sensitif. Gunakan placeholder dan environment variable.
