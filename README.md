# Praktikum Algoritma dan Pemrograman — v1

Repository praktikum **16 pertemuan terstruktur** berdasarkan *Buku Panduan Praktik: Pemrograman Dasar hingga Full Stack (Edisi Agustus 2026)*.

```text
Scratch
  ↓
Scratch + Python / Google Colab
  ↓
Python lokal + VS Code + Git/GitHub
  ↓
Python Web (Flask)
  ↓
REST API
  ↓
Deployment
  ↓
Node.js + Express
  ↓
Node + Python + SQLite
  ↓
Backend terstruktur + relasi database
  ↓
Final Full Stack
```

## Struktur Setiap Pertemuan
Pertemuan reguler:
```text
Pertemuan-XX-.../
├── Materi.md
├── Jobsheet.md
├── TugasVideo.md
└── praktikum/
    ├── README.md
    └── program runnable / instruksi Scratch
```

Khusus **Pertemuan 08, 12, dan 16**, `TugasVideo.md` diganti `Project.md`:
```text
Pertemuan-XX-.../
├── Materi.md
├── Jobsheet.md
├── Project.md
└── praktikum/
    └── starter runnable
```

## Peta 16 Pertemuan
| No | Materi | Environment | Output Utama |
|---:|---|---|---|
| 01 | [Scratch: algoritma visual](Pertemuan-01-Scratch-Algoritma-Visual/) | Scratch | Mini game/animasi |
| 02 | [Sequence, input/output, variable](Pertemuan-02-Scratch-Python-Colab-Dasar/) | Scratch + Colab + Python | Program interaktif dua versi |
| 03 | [Percabangan & validasi](Pertemuan-03-Percabangan-Validasi/) | Scratch + Colab + Python | Program keputusan |
| 04 | [Loop, counter, akumulasi](Pertemuan-04-Loop-Counter-Akumulasi/) | Scratch + Colab + Python | Simulasi berulang |
| 05 | [List, pencarian, statistik](Pertemuan-05-List-Data-Statistik/) | Scratch + Colab + Python | Pengolahan kumpulan data |
| 06 | [Function, dekomposisi, debugging](Pertemuan-06-Function-Debugging/) | Scratch + Colab + Python | Program modular |
| 07 | [VS Code, Python lokal, Git/GitHub](Pertemuan-07-VSCode-Git-GitHub/) | VS Code + terminal + Git | Repo Python pertama |
| 08 | [Checkpoint 1](Pertemuan-08-Project-Checkpoint-1/) | Python CLI + GitHub | 1 dari 30 project |
| 09 | [Python web Flask](Pertemuan-09-Python-Web-Flask/) | Flask + HTML/CSS/JS | Web lokal |
| 10 | [Python REST API](Pertemuan-10-Python-API-REST/) | Flask + HTTP/JSON | API + client |
| 11 | [Deployment](Pertemuan-11-Deployment/) | GitHub + cloud platform | Public URL |
| 12 | [Checkpoint 2](Pertemuan-12-Project-Checkpoint-2/) | Flask + API + deploy | 1 dari 30 project |
| 13 | [Node.js + Express](Pertemuan-13-NodeJS-Express/) | Node + npm + Express | Node web lokal |
| 14 | [Node + Python + SQLite](Pertemuan-14-Node-Python-SQLite/) | Multi-service | Mini integrated app |
| 15 | [Structured backend](Pertemuan-15-Fullstack-Structured-Backend/) | Node + Python + relational DB | Full stack preparation |
| 16 | [Final Project](Pertemuan-16-Final-Project/) | Node + Python + DB | 1 dari 30 final project |

## Yang Harus Dijalankan
Lihat **[RUNNING_GUIDE.md](RUNNING_GUIDE.md)**. Semua pertemuan memiliki program/instruksi yang harus benar-benar dijalankan.

- P01: Scratch.
- P02–P06: Scratch + Python + notebook Google Colab.
- P07–P08: Python lokal di VS Code/terminal + Git.
- P09–P12: Flask/web/API/deployment.
- P13: Node.js + Express.
- P14–P16: Node + Python + SQLite/relational database.

## Prinsip Praktikum
Mahasiswa tidak dinilai hanya dari “program jalan”. Setiap praktikum harus menunjukkan:
1. mental model/algoritma;
2. program benar-benar dijalankan;
3. expected vs actual;
4. boundary/invalid/failure test;
5. debugging berbasis bukti;
6. modifikasi mandiri;
7. mulai pertemuan 7: Git history yang menunjukkan progres;
8. dokumentasi setup/run/test.

## Dokumen Pendukung
- [Panduan menjalankan](RUNNING_GUIDE.md)
- [Panduan pengajar](PANDUAN_PENGAJAR.md)
- [Checklist audit repository](AUDIT_CHECKLIST.md)
- [Referensi/lampiran](Referensi/)

## Audit Otomatis
```bash
python scripts/audit_repo.py
```
Audit memeriksa struktur 16 pertemuan, file assignment yang benar, Python syntax, notebook/JSON, dan JavaScript syntax bila Node tersedia. Workflow GitHub Actions juga menjalankan audit pada branch `v1`.

## Security Minimum
Jangan commit `.env`, password, token, API key, credential database, `node_modules/`, `.venv/`, atau database runtime latihan. Gunakan environment variable dan placeholder seperti `<API_KEY>`.

## Catatan Scratch
GitHub tidak mengeksekusi Scratch secara native. Folder praktikum Scratch berisi **spesifikasi blok langkah demi langkah** yang harus dirakit dan dijalankan di Scratch. Pertemuan 2–6 juga menyediakan implementasi Python/Colab setara.

## Branch
Materi versi ini dikembangkan pada branch **`v1`**.
