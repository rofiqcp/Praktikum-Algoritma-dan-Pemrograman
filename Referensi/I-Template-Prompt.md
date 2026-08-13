> Diadaptasi langsung dari lampiran/panduan pada buku sumber Edisi Agustus 2026.

# Lampiran I — Template Prompt untuk Programming

## Penjelasan
```text
Jelaskan kode berikut untuk pemula. Pecah per blok, jelaskan input-output setiap fungsi, lalu berikan tiga pertanyaan cek pemahaman. Jangan mengubah kode dulu.
```

## Implementasi Kecil
```text
Context: [...]. Saya butuh fungsi untuk [...]. Input: [...]. Output: [...]. Edge cases: [...]. Constraint: jangan tambah dependency. Berikan fungsi, contoh pemanggilan, dan test case.
```

## Debugging
```text
Environment: [...]. Expected: [...]. Actual: [...]. Reproduction: [...]. Error log: [...]. Relevant code: [...]. Identifikasi root cause, berikan patch minimal, lalu test regresi.
```

## Code Review
```text
Review file berikut untuk correctness, readability, duplication, validation, error handling, dan security basics. Urutkan temuan berdasarkan severity. Jangan rewrite total.
```

## Refactor
```text
Perilaku program berikut sudah benar. Refactor hanya untuk mengurangi duplikasi dan memperjelas function. Pertahankan input/output. Berikan before/after behavior checklist.
```

## API Integration
```text
Dokumentasi endpoint menyatakan [...]. Request saya [...]. Response [...]. Tunjukkan cara request yang benar dengan timeout/error handling dan jelaskan status code.
```

## Deployment
```text
Local berjalan dengan perintah [...]. Platform [...]. Build/start log [...]. Struktur repo [...]. Pisahkan diagnosis build error vs runtime error dan usulkan perubahan minimal.
```

## Test Plan
```text
Buat test matrix untuk fitur [...]. Kelompokkan happy path, boundary, invalid input, not found, dependency failure, dan regression. Jangan buat kode implementasi.
```

## Database
```text
Schema saat ini [...]. Requirement [...]. Usulkan tabel/relationship minimal, constraint, dan query utama. Jelaskan tradeoff tanpa menambah tabel yang tidak perlu.
```

## Belajar Konsep
```text
Saya baru belajar [...]. Beri analogi, mental model, contoh kecil, lalu latihan bertingkat. Jangan langsung memberikan jawaban challenge terakhir.
```
