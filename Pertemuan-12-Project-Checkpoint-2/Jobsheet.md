# Jobsheet Pertemuan 12 — Project Checkpoint 2: Web + API + Deployment

## Identitas Project
- Nama mahasiswa/tim:
- Kelas:
- Nomor project pilihan:
- Judul project:
- Repository GitHub:
- Branch kerja:
- Public URL:
- External/mock API yang digunakan:

## Tujuan
Menyelesaikan satu project dari `Project.md` dengan mengintegrasikan kompetensi Pertemuan 09–11: Flask web, UI/UX dasar, REST API internal, external/mock API, validation, testing, GitHub, dan deployment publik.

> Starter pada `praktikum/starter-web-api/` hanya contoh struktur teknis. Nama domain, field, halaman, endpoint, dan aturan project harus disesuaikan dengan soal pilihan.

---

# Tahap 1 — Pilih dan Pahami Soal

Pilih satu dari 30 project pada `Project.md`.

Tuliskan ulang masalah dengan bahasa sendiri:

```text
Masalah yang ingin diselesaikan:
Pengguna utama:
Tujuan pengguna:
Input utama:
Output utama:
Fitur internal:
Data external/mock:
Batasan:
```

Checklist:

- [ ] Tidak mengubah inti soal menjadi project lain.
- [ ] Dapat menjelaskan mana fitur utama dan mana fitur eksternal/pelengkap.
- [ ] Tidak menambahkan Node/database karena belum menjadi kebutuhan checkpoint.

---

# Tahap 2 — Requirement Table

| ID | Requirement | Input | Proses | Output | Error/Boundary |
|---|---|---|---|---|---|
| R01 | | | | | |
| R02 | | | | | |
| R03 | | | | | |
| R04 | | | | | |
| R05 | | | | | |

Tambahkan baris sesuai kebutuhan.

## Aturan Validasi
Tuliskan minimal lima aturan yang relevan:

```text
V01:
V02:
V03:
V04:
V05:
```

Contoh kategori: kosong, tipe salah, angka negatif, duplikat, ID tidak ditemukan, kapasitas, query terlalu pendek, dan sebagainya.

---

# Tahap 3 — User Flow

Gambarkan alur utama, termasuk failure path.

Template:

```text
HOME
 ↓
INPUT/SEARCH
 ↓
VALIDASI
 ├── salah → ERROR STATE → kembali edit
 └── benar
       ↓
EXTERNAL/MOCK REQUEST
 ├── sukses + data → RESULT
 ├── sukses kosong → EMPTY STATE
 ├── timeout → TIMEOUT STATE
 └── error → ERROR STATE
       ↓
SIMPAN/PILIH DATA INTERNAL
       ↓
LIST INTERNAL
       ↓
DETAIL/UPDATE/DELETE
```

Lampirkan flowchart/diagram pada README atau file dokumentasi.

---

# Tahap 4 — Page Map

Minimal tiga halaman fungsional.

| Halaman | Route | Tujuan | Data yang Dibutuhkan | State |
|---|---|---|---|---|
| Home/Dashboard | `/` | | | |
| List | | | | |
| Form/Detail | | | | |
| Opsional | | | | |

Pertanyaan review:

1. Apakah setiap halaman mempunyai tujuan berbeda?
2. Apakah tiga halaman tersebut dapat didemonstrasikan?
3. Apakah error/empty state ditempatkan pada halaman yang tepat?

---

# Tahap 5 — UI Component Plan

Minimal enam komponen UI berbeda.

| Komponen | Halaman | Fungsi | State yang Diuji |
|---|---|---|---|
| Navbar | | | |
| Form/Input | | | |
| Button | | | |
| Table/Card/List | | | |
| Alert/Feedback | | | |
| Empty/Loading state | | | |
| Tambahan | | | |

Audit juga label input, focus keyboard, responsive layout, dan feedback aksi.

---

# Tahap 6 — Internal Data Model

Tentukan struktur data internal.

Contoh format dokumentasi:

```text
Entity: SavedItem
- id        : integer, unik
- title     : string, wajib
- note      : string, opsional
- source_id : string, opsional
```

Berikan dua contoh object/data:

```json
{}
```

```json
{}
```

Jelaskan apakah data in-memory atau mekanisme sederhana lain yang diizinkan, serta konsekuensi ketika server restart.

---

# Tahap 7 — Internal REST API Contract

Isi **sebelum coding endpoint**.

| Method | Path | Tujuan | Request Body | Success | Error |
|---|---|---|---|---|---|
| GET | | collection | - | 200 | |
| GET | | detail | - | 200 | 404 |
| POST | | create | JSON | 201 | 400/409 |
| PATCH/PUT | | update | JSON | 200 | 400/404 |
| DELETE | | delete | - | 204/200 | 404 |

## Contoh Success Response

```json
{
  "data": [],
  "count": 0
}
```

## Contoh Error Response

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Input tidak valid"
  }
}
```

Gunakan bentuk error yang konsisten.

---

# Tahap 8 — External/Mock API Contract

Isi:

```text
Nama/sumber:
Public atau mock:
Base URL/source:
Method:
Path:
Query parameter:
Field response yang digunakan:
Timeout:
Success condition:
No-result condition:
Network failure:
HTTP failure:
Invalid JSON:
Respons UI saat gagal:
```

Jika menggunakan API dengan konfigurasi khusus, dokumentasikan **nama variable konfigurasi** di `.env.example`, bukan nilai privatnya.

---

# Tahap 9 — Buat Skeleton Project

Struktur minimal:

```text
project/
├── app.py
├── requirements.txt
├── .gitignore
├── .env.example
├── README.md
├── API.md
├── TEST_PLAN.md
├── templates/
└── static/
```

Commit pertama yang disarankan:

```bash
git add .
git commit -m "chore: create checkpoint project skeleton"
```

---

# Tahap 10 — Implementasi Halaman Dulu

Bangun:

1. base template/navigation;
2. Home/Dashboard;
3. List internal;
4. Form/detail;
5. static CSS;
6. basic responsive layout.

Test setiap route:

| Route | Expected | Actual | Pass? |
|---|---:|---:|:---:|
| `/` | 200 | | |
| halaman 2 | 200 | | |
| halaman 3 | 200 | | |
| route salah | 404 | | |

Commit milestone.

---

# Tahap 11 — Implementasi Internal REST API

Kerjakan bertahap:

```text
GET collection
→ GET detail
→ POST + validation
→ PATCH/DELETE bila relevan
→ error contract
→ automated test
```

Jangan mengintegrasikan API eksternal sebelum API internal utama stabil.

## Test Internal API

| TC | Method | Skenario | Expected | Actual | Pass? |
|---|---|---|---|---|:---:|
| I01 | GET | collection | 200 | | |
| I02 | GET | detail ada | 200 | | |
| I03 | GET | detail hilang | 404 | | |
| I04 | POST | valid | 201 | | |
| I05 | POST | invalid | 400 | | |
| I06 | POST | boundary | sesuai rule | | |
| I07 | POST | duplikat | conflict bila relevan | | |
| I08 | PATCH/DELETE | ID salah | 404 | | |

---

# Tahap 12 — Integrasi External/Mock API

Buat function/service khusus jika memungkinkan.

Checklist:

- [ ] URL/config terpisah dari template.
- [ ] Ada timeout.
- [ ] HTTP failure ditangani.
- [ ] Network failure ditangani.
- [ ] No-result dibedakan dari error.
- [ ] Parsing response tidak diasumsikan selalu berhasil.
- [ ] UI memiliki feedback yang sesuai.

## Failure Drill Wajib

Uji minimal:

1. response sukses;
2. hasil kosong;
3. timeout atau failure yang disimulasikan;
4. external service tidak tersedia.

Catat:

| Kasus | Expected UI/Behavior | Actual | Pass? |
|---|---|---|:---:|
| Success | data tampil | | |
| Empty | no-result state | | |
| Timeout | error state | | |
| Failure | app tidak crash | | |

---

# Tahap 13 — UI State Review

Periksa:

- [ ] normal;
- [ ] focus;
- [ ] validation error;
- [ ] success;
- [ ] empty/no result;
- [ ] external failure;
- [ ] loading bila arsitektur memerlukannya;
- [ ] responsive mobile;
- [ ] data panjang tidak merusak layout.

Buat satu screenshot untuk minimal tiga state berbeda.

---

# Tahap 14 — Automated Test

Jalankan test starter/project Anda, misalnya:

```bash
python -m unittest -v test_app.py
```

Automated test harus independen dari urutan test. Reset data in-memory pada `setUp()` bila diperlukan.

Target pengayaan repository: **10+ automated assertions/test scenarios** yang mencakup halaman, API internal, dan external integration mock.

Catat:

```text
Jumlah test:
Pass:
Fail/Error:
```

---

# Tahap 15 — Test Plan dan Regression

Minimal 10 test case adalah requirement buku. Gunakan 12 atau lebih bila project mempunyai banyak failure path.

| ID | Layer | Skenario | Input | Expected | Actual | Status |
|---|---|---|---|---|---|---|
| TC01 | Page | Home | | 200 | | |
| TC02 | Page | List | | 200 | | |
| TC03 | Page | 404 | | 404 | | |
| TC04 | API | Collection | | 200 | | |
| TC05 | API | POST valid | | 201 | | |
| TC06 | API | POST invalid | | 400 | | |
| TC07 | API | Not found | | 404 | | |
| TC08 | External | Success | | data | | |
| TC09 | External | Empty | | empty state | | |
| TC10 | External | Failure/timeout | | handled | | |
| TC11 | UI | Mobile | | usable | | |
| TC12 | Regression | setelah fitur baru | | fitur lama tetap benar | | |

---

# Tahap 16 — Git History Review

Minimum history harus menunjukkan progres nyata.

Contoh:

```text
chore: create project skeleton
docs: add page and endpoint plan
feat: add web pages
feat: add internal API
feat: add external mock integration
fix: handle timeout and empty response
test: cover page and API scenarios
docs: add API documentation
chore: prepare deployment
fix: resolve deployment issue
docs: add public verification
```

Jangan membuat commit palsu hanya untuk jumlah. Commit harus sesuai perubahan yang benar-benar dilakukan.

---

# Tahap 17 — Clean Environment Gate

Sebelum deploy:

```bash
python -m venv .venv-clean
```

Aktifkan lalu:

```bash
python -m pip install -r requirements.txt
python -m unittest -v test_app.py
```

Pastikan app dapat dijalankan dari dependency yang terdokumentasi.

---

# Tahap 18 — Deployment

Gunakan workflow Pertemuan 11:

```text
local PASS
→ commit
→ push GitHub
→ pilih repo/branch pada platform
→ build
→ start
→ public URL
→ verify
```

Bukti yang dicatat:

```text
Platform:
Repository:
Branch:
Commit:
Build result:
Start result:
Public URL:
```

---

# Tahap 19 — Public Regression Test

Setelah deploy, ulangi kasus penting dari URL publik.

Minimal:

- home;
- list page;
- internal API GET;
- create/update bila aman dilakukan;
- invalid input;
- external/mock success;
- external/mock failure state bila dapat disimulasikan;
- 404.

Uji dari browser/perangkat lain bila memungkinkan.

---

# Tahap 20 — README dan Dokumentasi

README harus menjawab:

1. Project ini menyelesaikan masalah apa?
2. Apa fitur utamanya?
3. Bagaimana arsitekturnya?
4. Bagaimana setup lokal?
5. Bagaimana menjalankan?
6. Bagaimana menjalankan test?
7. Environment variable apa yang dibutuhkan?
8. Endpoint apa saja?
9. Bagaimana deployment dilakukan?
10. Apa known limitations?

Pisahkan `API.md` bila endpoint cukup banyak.

---

# Tahap 21 — Review Penilaian Sendiri

Nilai project sebelum dikumpulkan.

| Aspek | Bobot | Nilai sendiri | Bukti |
|---|---:|---:|---|
| UI & alur pengguna | 15 | | |
| Backend Flask | 20 | | |
| API sendiri | 20 | | |
| External/mock integration | 10 | | |
| Validation & error state | 10 | | |
| Deployment & config | 15 | | |
| Docs/testing/demo | 10 | | |

Jika tidak ada bukti, jangan memberi nilai penuh pada diri sendiri.

---

# Deliverable Wajib
- [ ] source runnable;
- [ ] GitHub repository;
- [ ] public URL;
- [ ] minimal tiga halaman;
- [ ] minimal enam komponen UI;
- [ ] internal REST API;
- [ ] external/mock integration;
- [ ] timeout/failure handling;
- [ ] README;
- [ ] endpoint documentation;
- [ ] user flow/page map;
- [ ] test report minimal 10 kasus;
- [ ] automated test result;
- [ ] screenshot/log deployment;
- [ ] bukti test public URL;
- [ ] Git history progres;
- [ ] demo.

## Starter

```bash
cd praktikum/starter-web-api
python -m pip install -r requirements.txt
python app.py
```

Terminal lain/test:

```bash
python -m unittest -v test_app.py
```

Starter harus dimodifikasi sesuai project pilihan dan **bukan jawaban final**.
