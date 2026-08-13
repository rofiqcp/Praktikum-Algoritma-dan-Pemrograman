# Git Workflow Lab — Pertemuan 07

## Tahap 1 — Repository Lokal

```bash
git init
git status
```

## Tahap 2 — Staging dan Commit

```bash
git add .
git status
git commit -m "chore: siapkan project Python lokal"
```

Lakukan minimal dua perubahan stabil berikutnya dan commit secara terpisah.

## Tahap 3 — History

```bash
git log --oneline
```

Target latihan P07: minimal tiga commit bermakna.

## Tahap 4 — Remote GitHub

```bash
git remote add origin <URL_REPOSITORY>
git branch -M main
git push -u origin main
```

Verifikasi:

```bash
git remote -v
git status
```

## Tahap 5 — Sinkronisasi

```bash
git pull
git clone <URL_REPOSITORY>
```

Clone repository ke folder berbeda dan jalankan kembali program berdasarkan README.

## Bukti
Simpan `git status`, `git log --oneline`, remote, repository GitHub, dan hasil project dari folder clone.