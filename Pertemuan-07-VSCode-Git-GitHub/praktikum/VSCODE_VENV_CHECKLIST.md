# VS Code dan Virtual Environment Checklist

## Cek Environment

```bash
python --version
python -m pip --version
git --version
```

## Buat Virtual Environment

```bash
python -m venv .venv
```

Aktifkan sesuai OS, lalu pilih `.venv` melalui **Python: Select Interpreter** di VS Code.

## Verifikasi

- [ ] Terminal berada pada folder project.
- [ ] `.venv` aktif.
- [ ] Interpreter VS Code berasal dari `.venv`.
- [ ] `python main.py` berjalan.
- [ ] Unit test berjalan.
- [ ] `.venv/` tidak muncul sebagai file yang akan di-commit.
- [ ] `requirements.txt` tersedia bila project menggunakan package tambahan.

## Saat Package Tidak Ditemukan
Bandingkan interpreter yang menjalankan program dengan lokasi pip. Gunakan `python -m pip` agar instalasi package diarahkan ke interpreter Python yang sedang digunakan.