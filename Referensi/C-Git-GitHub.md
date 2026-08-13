> Diadaptasi langsung dari lampiran/panduan pada buku sumber Edisi Agustus 2026.

# Lampiran C — Git dan GitHub Cheat Sheet

```bash
git status
git add .
git commit -m "feat: tambah fitur"
git log --oneline
git diff
git pull
git push
git branch
git remote -v
```

| Situasi | Perintah/aksi |
|---|---|
| Lihat perubahan belum commit | `git status` + `git diff` |
| Simpan checkpoint | `git add ...` lalu `git commit` |
| Ambil perubahan remote | `git pull` |
| Kirim commit | `git push` |
| Salin repo baru | `git clone URL` |
| Cek remote | `git remote -v` |

> Jangan jalankan perintah Git destruktif yang tidak dipahami. Sebelum reset/clean/rebase atau menghapus branch, pastikan ada backup/commit dan pahami dampaknya.
