# Materi Pertemuan 12 — Project Checkpoint 2: Python Web + API + Deployment

> Sumber utama: *Buku Panduan Praktik: Scratch → Python → Web → API → Node.js → Full Stack*, Edisi Agustus 2026. Pertemuan 12 adalah **checkpoint**, bukan sesi framework baru. Peserta memilih satu dari 30 project dan mengintegrasikan kompetensi Pertemuan 09–11: web Flask, UI sederhana, REST API, integrasi external/mock API, GitHub, dan deployment publik.

Checkpoint ini menguji kemampuan mengubah soal cerita menjadi aplikasi yang mempunyai **alur pengguna, halaman, endpoint, state UI, kontrak API, failure handling, test, Git history, deployment, dan dokumentasi**. Program yang hanya “bisa dibuka” belum cukup.

## Target Kompetensi
Setelah checkpoint, mahasiswa mampu:

1. Menentukan requirement project sebelum coding.
2. Merancang user flow dan page map minimal tiga halaman.
3. Menentukan minimal enam jenis komponen UI yang memang dibutuhkan.
4. Membuat website Flask dengan minimal tiga route halaman.
5. Menyediakan REST API JSON minimal GET dan POST serta satu operasi perubahan data; PATCH/DELETE digunakan bila sesuai kebutuhan project.
6. Mendokumentasikan method, path, request body, response body, dan status code endpoint.
7. Menggunakan minimal satu API publik atau mock API yang disediakan pengajar.
8. Memberikan timeout dan error handling pada integrasi external/mock API.
9. Menampilkan state normal, loading bila relevan, empty/no-result, error, dan success.
10. Memisahkan kegagalan fitur eksternal agar fitur utama tetap dapat digunakan bila requirement project memang menuntutnya.
11. Menggunakan environment variable untuk konfigurasi yang sesuai.
12. Menulis automated test dan manual test report.
13. Menggunakan Git commit bertahap selama pengerjaan.
14. Mendeploy aplikasi dari GitHub dan memverifikasi public URL.
15. Membaca build/runtime log bila deployment gagal.
16. Menyusun README, endpoint documentation, test report, dan demo yang dapat direproduksi.

## Output Pertemuan
- public URL;
- GitHub repository;
- source Flask yang dapat dijalankan lokal;
- minimal tiga halaman;
- REST API internal;
- satu integrasi external/mock API;
- dokumentasi endpoint;
- test report dan automated test;
- bukti deployment;
- README lengkap;
- demo project.

---

# 12.1 Requirement Setara untuk Semua Project

Sesuai buku panduan, semua pilihan project memiliki beban inti setara:

- Flask sebagai backend web utama dan template HTML.
- Minimal **3 halaman**: dashboard/home, list data, form/detail atau variasi setara.
- Minimal **6 komponen UI berbeda**, misalnya navbar, form, button, table/card, alert, badge, empty state, loading indicator, search/filter.
- REST API internal dengan response JSON dan status code yang sesuai.
- Minimal GET collection, GET detail atau POST, serta satu operasi perubahan state/data.
- Minimal satu request ke external/mock API.
- External/mock request mempunyai timeout dan error handling.
- Environment variable digunakan untuk konfigurasi yang perlu dipisahkan dari source.
- Deploy dari GitHub dan diuji melalui public URL.
- Minimal **10 test case**, termasuk API failure.
- Minimal satu kasus normal, satu boundary, satu invalid input, serta not-found/capacity bila relevan.

---

# 12.2 Rubrik Penilaian

| Aspek | Bobot |
|---|---:|
| UI & alur pengguna | 15 |
| Backend Flask | 20 |
| API sendiri | 20 |
| Integrasi API eksternal/mock | 10 |
| Validation & error state | 10 |
| Deployment & config | 15 |
| Dokumentasi/testing/demo | 10 |
| **Total** | **100** |

Rubrik menunjukkan bahwa aplikasi bukan hanya dinilai dari tampilan. Backend, API, validation, failure state, deployment, testing, dan dokumentasi mempunyai bobot besar.

---

# 12.3 Workflow Besar Checkpoint

```text
SOAL CERITA
   ↓
REQUIREMENT
   ↓
USER FLOW
   ↓
PAGE MAP + UI STATE
   ↓
DATA MODEL SEDERHANA
   ↓
INTERNAL API CONTRACT
   ↓
EXTERNAL/MOCK API CONTRACT
   ↓
PROJECT SKELETON
   ↓
FITUR UTAMA LOKAL
   ↓
VALIDATION + ERROR STATE
   ↓
AUTOMATED TEST
   ↓
GIT COMMIT
   ↓
EXTERNAL INTEGRATION
   ↓
FAILURE TEST
   ↓
DEPLOY
   ↓
PUBLIC REGRESSION TEST
   ↓
README + ENDPOINT DOCS + DEMO
```

Jangan memulai dari CSS atau deployment sebelum requirement dan kontrak dasar jelas.

---

# 12.4 Requirement Extraction

Gunakan format berikut terhadap project yang dipilih.

```text
Aktor/Pengguna:
Tujuan utama:
Input utama:
Data internal:
Data external/mock:
Proses utama:
Output utama:
Aturan validasi:
Kondisi kosong:
Kondisi tidak ditemukan:
Kondisi external failure:
Batasan project:
```

Contoh untuk “Pencari Buku dan Reading List”:

```text
Pengguna     : siswa/pembaca
Input        : kata kunci buku
External     : API katalog/mock
Internal     : reading list
Output       : card hasil pencarian dan daftar tersimpan
Invalid      : query kosong
No-result    : API sukses tetapi hasil kosong
Failure      : API timeout/error
Internal API : list/tambah/hapus reading list
```

---

# 12.5 User Flow Sebelum Page Map

Contoh:

```text
HOME
  ↓
SEARCH FORM
  ↓
LOADING
  ↓
┌───────────────┬─────────────────┬────────────────┐
│ RESULT FOUND  │ NO RESULT       │ REQUEST ERROR  │
│      ↓        │      ↓          │      ↓         │
│ SAVE ITEM     │ TRY AGAIN       │ RETRY/FALLBACK │
└───────────────┴─────────────────┴────────────────┘
       ↓
SAVED LIST
       ↓
DETAIL / DELETE
```

User flow memaksa mahasiswa memikirkan kondisi selain happy path.

---

# 12.6 Page Map Minimal

Contoh umum:

| Halaman | Route contoh | Tujuan |
|---|---|---|
| Home/Dashboard | `/` | orientasi, form/search, ringkasan |
| List internal | `/saved` | data yang disimpan pengguna |
| Form/Detail | `/saved/new` atau `/saved/<id>` | tambah/detail data |
| API Docs/About | `/about` | bonus/opsional bila 3 halaman inti sudah terpenuhi |

Tiga halaman harus memiliki fungsi nyata; jangan membuat tiga halaman yang hanya membagi teks statis.

---

# 12.7 UI Component Plan

Sebelum coding, tulis minimal enam komponen dan alasan penggunaannya.

| Komponen | Halaman | Tujuan | State penting |
|---|---|---|---|
| Navbar | semua | navigasi | normal/focus |
| Search form | home | input query | normal/error |
| Button | form | submit | normal/disabled bila dipakai |
| Card/table | hasil/list | tampil data | normal/empty |
| Alert | home/form | feedback | error/success |
| Badge | list | status | variasi status |
| Loading state | search | menunggu external API | loading |

Jangan menambah komponen hanya untuk memenuhi jumlah. Setiap komponen harus mendukung user flow.

---

# 12.8 Internal Data Model

Pada checkpoint ini penyimpanan dapat menggunakan mekanisme sederhana yang diizinkan pengajar. Jika starter memakai in-memory list, jelaskan keterbatasannya: data hilang saat process restart.

Contoh:

```python
plans = [
    {
        "id": 1,
        "title": "Kegiatan Lapangan",
        "query": "Bandung",
        "note": "Persiapan alternatif lokasi",
    }
]
```

Pilih field berdasarkan kebutuhan project, bukan menyalin contoh tanpa alasan.

---

# 12.9 Internal REST API Contract

Sebelum route dibuat, isi tabel:

| Method | Path | Tujuan | Request | Success | Error |
|---|---|---|---|---|---|
| GET | `/api/items` | list | - | 200 | - |
| GET | `/api/items/<id>` | detail | - | 200 | 404 |
| POST | `/api/items` | tambah | JSON | 201 | 400/409 |
| PATCH | `/api/items/<id>` | update | JSON | 200 | 400/404 |
| DELETE | `/api/items/<id>` | hapus | - | 204/200 | 404 |

Endpoint aktual disesuaikan dengan domain project: `/api/watchlist`, `/api/plans`, `/api/notes`, dan seterusnya.

---

# 12.10 Response Contract

Contoh collection:

```json
{
  "data": [
    {"id": 1, "title": "Contoh"}
  ],
  "count": 1
}
```

Contoh validation error:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Input tidak valid",
    "details": {
      "title": "wajib diisi"
    }
  }
}
```

Contoh not found:

```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "Data tidak ditemukan"
  }
}
```

Gunakan pola konsisten pada endpoint internal.

---

# 12.11 External/Mock API Contract

Sebelum integrasi, dokumentasikan:

```text
Nama/sumber API:
Base URL atau mock source:
Method:
Path:
Query parameter:
Response field yang dipakai:
Timeout:
Success condition:
No-result condition:
HTTP failure:
Network failure:
Invalid JSON:
Fallback/UX response:
```

Tujuannya agar integrasi tidak menjadi potongan `requests.get()` yang tidak dipahami.

---

# 12.12 Wrapper untuk External API

Disarankan membungkus komunikasi external dalam function terpisah:

```python
import requests


def fetch_external(url, params=None, timeout=5):
    try:
        response = requests.get(url, params=params, timeout=timeout)
        response.raise_for_status()
        return {"ok": True, "data": response.json(), "error": None}
    except requests.Timeout:
        return {"ok": False, "data": None, "error": "timeout"}
    except requests.RequestException:
        return {"ok": False, "data": None, "error": "request_failed"}
    except ValueError:
        return {"ok": False, "data": None, "error": "invalid_json"}
```

Nama function dan bentuk result dapat berbeda. Tujuannya adalah **memisahkan integrasi network dari route/template** agar lebih mudah diuji.

---

# 12.13 Mock First

External API dapat berubah, membutuhkan key, mengalami rate limit, atau tidak tersedia pada saat penilaian. Buku mengizinkan mock API yang disediakan pengajar.

Workflow yang stabil:

```text
DEFINE CONTRACT
→ USE MOCK RESPONSE
→ BUILD UI + INTERNAL FEATURE
→ TEST SUCCESS/FAILURE
→ SWITCH TO PUBLIC API bila dipilih/tersedia
→ RETEST
```

Mock bukan berarti tidak belajar API. Mahasiswa tetap harus memahami request, response, status, field, timeout, dan failure path.

---

# 12.14 External Failure Tidak Boleh Membuat Seluruh App Tidak Terkendali

Contoh project tertentu dalam buku secara eksplisit meminta fitur utama tetap berjalan walaupun fitur tambahan eksternal gagal, misalnya Todo + Quote dan Catatan + Trivia.

Mental model:

```text
INTERNAL FEATURE ──────────────→ tetap tersedia

EXTERNAL FEATURE
   ├── success → tampilkan data
   ├── no result → empty state
   └── error/timeout → error state lokal
```

Jangan menangkap exception lalu menyembunyikan semua informasi. Aplikasi harus memberi feedback yang dapat dipahami.

---

# 12.15 State yang Harus Dirancang

Untuk halaman yang bergantung pada external API:

1. **Initial** — belum ada pencarian.
2. **Loading** — jika request dilakukan asynchronous/frontend; jika server-side form synchronous, pengguna tetap harus memperoleh feedback yang jelas setelah submit.
3. **Success** — data ditemukan.
4. **Empty/No Result** — request sukses tetapi data kosong.
5. **Validation Error** — input pengguna salah.
6. **External Error** — upstream/API gagal.
7. **Timeout** — request melewati batas.

Untuk internal API:

- collection kosong;
- detail not found;
- create success;
- validation error;
- conflict/duplicate bila relevan;
- update/delete success.

---

# 12.16 Environment Configuration

Gunakan environment variable untuk konfigurasi yang perlu dipisahkan dari source.

```python
import os

EXTERNAL_API_URL = os.getenv("EXTERNAL_API_URL", "")
```

Repository dapat memiliki `.env.example` dengan placeholder aman.

Pastikan aplikasi memberi error yang bisa dipahami jika konfigurasi wajib tidak tersedia.

---

# 12.17 Struktur Project yang Disarankan

```text
project-name/
├── app.py
├── requirements.txt
├── .gitignore
├── .env.example
├── README.md
├── API.md
├── TEST_PLAN.md
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── list.html
│   └── detail_or_form.html
├── static/
│   ├── style.css
│   └── app.js
├── services/
│   └── external_api.py        # pengayaan yang disarankan
└── tests/
    └── test_app.py
```

Starter repository boleh lebih sederhana. Struktur dipisahkan hanya jika membantu keterbacaan, bukan untuk membuat folder sebanyak mungkin.

---

# 12.18 Testing Pyramid Sederhana untuk Checkpoint

## A. Logic/validation tests
Uji function yang tidak membutuhkan network bila ada.

## B. Flask route/API tests
Gunakan test client untuk halaman dan internal REST API.

## C. External integration tests dengan mock
Jangan membuat automated test utama bergantung penuh pada internet yang berubah.

## D. Public smoke test
Setelah deploy, uji public URL.

---

# 12.19 Minimum Test Matrix

| ID | Layer | Skenario | Expected |
|---|---|---|---|
| TC01 | page | home | 200 |
| TC02 | page | list | 200 |
| TC03 | page | route tidak ada | 404 |
| TC04 | internal API | GET collection | 200 |
| TC05 | internal API | POST valid | 201 |
| TC06 | internal API | POST invalid | 400 |
| TC07 | internal API | not found | 404 |
| TC08 | external | success | data tampil |
| TC09 | external | no result | empty state |
| TC10 | external | timeout/failure | error state, app tidak crash |
| TC11 | deployment | public health/home | 200 |
| TC12 | regression | fitur lama setelah perubahan | tetap benar |

Buku mewajibkan minimal 10; repository mendorong 12 atau lebih agar failure path benar-benar diuji.

---

# 12.20 Git Workflow Project

Contoh milestone commit:

```text
chore: create flask project skeleton
docs: add user flow and endpoint plan
feat: add three page routes
feat: add internal REST API
feat: integrate mock external service
fix: handle empty and timeout state
test: add API and page tests
docs: add endpoint documentation
chore: add deployment config
fix: resolve deployment runtime issue
docs: add public verification report
```

Commit message aktual boleh berbeda, tetapi history harus menunjukkan proses, bukan satu commit raksasa di akhir.

---

# 12.21 Deployment Gate

Sebelum deploy:

```text
[ ] clean environment install berhasil
[ ] local page berjalan
[ ] internal API berjalan
[ ] external mock/success path berjalan
[ ] external failure path diuji
[ ] automated test PASS
[ ] requirements benar
[ ] config/environment terdokumentasi
[ ] GitHub branch terbaru
```

Setelah itu baru deploy.

---

# 12.22 Public Verification

Setelah deploy:

```text
GET homepage
GET list page
GET internal API collection
POST internal API valid/invalid bila aman dilakukan
external success/mock path
external failure state bila dapat disimulasikan
404
```

Jika project memiliki `/health`, uji juga endpoint tersebut.

Bukti publik minimal:

- public URL;
- screenshot/log deployment berhasil;
- test dari perangkat/browser lain;
- tabel expected-vs-actual.

---

# 12.23 Troubleshooting per Layer

```text
Browser/UI
  ↓
HTML Form / JavaScript
  ↓
HTTP Request
  ↓
Flask Page Route
  ↓
Internal API Route
  ↓
External API Client
  ↓
External/Mock Service
  ↓
Deployment Runtime
```

Contoh diagnosis:

- UI kosong tetapi internal API 200 → periksa template/rendering.
- internal API 500 → baca Flask traceback.
- external API timeout tetapi internal CRUD sehat → periksa external wrapper/config, jangan ubah seluruh app.
- lokal sukses, public build gagal → periksa dependency/build log.
- build sukses, public service tidak start → periksa entrypoint/start log.

---

# 12.24 Definition of Done

Project baru dianggap selesai jika:

- [ ] requirement sesuai pilihan project;
- [ ] minimal tiga halaman fungsional;
- [ ] minimal enam komponen UI yang relevan;
- [ ] internal REST API berjalan;
- [ ] status code benar;
- [ ] external/mock API terintegrasi;
- [ ] timeout/failure ditangani;
- [ ] normal/boundary/invalid/not-found diuji;
- [ ] minimal 10 test case terdokumentasi;
- [ ] automated test lulus;
- [ ] Git history menunjukkan progres;
- [ ] README dan API docs lengkap;
- [ ] public deploy berhasil;
- [ ] public URL diuji;
- [ ] mahasiswa dapat menjelaskan arsitektur dan failure path.

---

# 12.25 Hal yang Tidak Perlu Ditambahkan

Checkpoint ini **tidak mensyaratkan** Node.js, Express, SQLite, atau database relational karena materi tersebut baru masuk pada Pertemuan 13–15. Jangan memperumit project dengan teknologi yang belum diperlukan hanya untuk terlihat lebih besar.

---

# 12.26 Exit Ticket

1. Mengapa page map dan endpoint contract dibuat sebelum coding?
2. Apa beda internal API dan external API pada project?
3. Mengapa automated test external integration sebaiknya bisa memakai mock?
4. Apa beda validation error, no-result, dan external failure?
5. Mengapa public URL saja belum membuktikan seluruh project benar?
6. Jika API eksternal gagal tetapi fitur internal sehat, layer apa yang harus diperiksa?
7. Mengapa Git history dinilai dalam checkpoint?
8. Sebutkan minimal tiga bukti bahwa project benar-benar siap dinilai.

## Referensi Internal
- `Jobsheet.md` — workflow pelaksanaan checkpoint.
- `Project.md` — 30 pilihan project dari buku + blueprint implementasi repository.
- `praktikum/starter-web-api/` — starter teknis, bukan jawaban project.
- `Referensi/D-HTTP-API.md` — ringkasan HTTP/API.
- `Referensi/E-Flask-FastAPI.md` — ringkasan framework.
- `Referensi/H-Troubleshooting.md` — pola troubleshooting.
