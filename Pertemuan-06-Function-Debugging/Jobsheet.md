# Jobsheet Pertemuan 06 — Function, Dekomposisi, dan Debugging

## Environment
Scratch + Google Colab + Python.

## Percobaan Wajib
1. Kalkulator modular: fungsi hitung + formatting.
2. Sistem nilai modular: validation + grade.
3. Menu modular: beberapa fitur dipanggil dari main loop.
4. Bug hunt: tracing accumulator salah.
5. Function tests: test normal, boundary, invalid.

## Cara Menjalankan
Rakit My Blocks Scratch → jalankan `praktikum/python/*.py` → notebook Colab → test:

```bash
python -m unittest discover -s praktikum/tests -v
```

## Analisis
1. Apa beda parameter dan return?
2. Mengapa global state sebaiknya diminimalkan?
3. Kapan fungsi perlu dipecah lagi?
4. Mengapa regression test penting setelah refactor?

## Debug Log
Gunakan format `reproduce → read → locate → hypothesis → small test → one change → retest → document` minimal untuk dua bug.
