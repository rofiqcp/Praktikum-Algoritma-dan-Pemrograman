# Materi Pertemuan 06 — Function, Dekomposisi, dan Debugging

## Target
Memecah masalah menjadi submasalah, menggunakan My Blocks Scratch dan `def` Python, memahami parameter/return, dan debugging sistematis.

Alur: **masalah besar → fitur → fungsi kecil → test per fungsi → integrasi**.

```python
def hitung_total(harga,jumlah):
    return harga*jumlah
```

Debugging: reproduce → read error → locate → hypothesize → test small → change one thing → retest → document. Hindari global state jika data bisa dikirim lewat parameter.
