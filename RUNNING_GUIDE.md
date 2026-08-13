# Panduan Menjalankan Seluruh Praktikum

Gunakan Python 3.x dan Node.js sesuai kebutuhan lokal/institusi. Untuk environment yang cepat berubah seperti deployment/runtime, verifikasi dokumentasi resmi pada saat praktikum.

| P | Folder Runnable | Cara Menjalankan |
|---:|---|---|
| 01 | `praktikum/*.md` | Rakit di Scratch → Green Flag |
| 02 | `praktikum/python/`, `colab/` | jalankan semua `.py`; buka notebook di Colab |
| 03 | `praktikum/python/`, `colab/` | sama + boundary test |
| 04 | `praktikum/python/`, `colab/` | sama + tracing loop |
| 05 | `praktikum/python/`, `colab/` | sama + list empty/not-found test |
| 06 | `praktikum/python/`, `tests/` | `.py` + `python -m unittest discover -s tests -v` |
| 07 | `praktikum/python-local/` | `python main.py`; unit test; Git workflow |
| 08 | `praktikum/starter-cli/` | `python main.py`; unit test; starter checkpoint |
| 09 | `praktikum/flask-web/` | install requirements → test → `python app.py` |
| 10 | `praktikum/rest-api/` | test → `python app.py`; terminal lain `python client.py` |
| 11 | `praktikum/deploy-flask/` | test lokal → `python app.py` → deploy dari GitHub |
| 12 | `praktikum/starter-web-api/` | install → test → `python app.py` |
| 13 | `praktikum/node-express/` | `npm install`; `npm test`; `npm start` |
| 14 | `praktikum/integrated-app/` | backend Python `:5001` + frontend Node `:3000` |
| 15 | `praktikum/structured-app/` | `cd backend && python main.py`; frontend `npm start` |
| 16 | `praktikum/final-starter/` | `cd backend && python app.py`; frontend `npm start` |

## Python Virtual Environment
Windows PowerShell:
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```
macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Node.js
```bash
npm install
npm start
```
Jika project menyediakan test:
```bash
npm test
```

## Multi-service P14–P16
Gunakan dua terminal. Pastikan port backend dan frontend berbeda. Buka DevTools → Network/Console untuk membedakan error UI, CORS, network, API, dan database.

## Checklist Saat Program Tidak Jalan
```text
1. Working directory benar?
2. Runtime/interpreter benar?
3. Dependency terpasang pada environment yang benar?
4. Port sudah dipakai process lain?
5. File/path/template/static benar?
6. HTTP method/URL/status code benar?
7. Backend log/traceback mengatakan apa?
8. Database/schema sudah di-init?
9. Environment variable tersedia?
10. Setelah fix, regression test masih lulus?
```

## Bukti Minimum
Simpan command, versi runtime, output, test case, screenshot/browser response, error/log, perubahan, retest, dan Git commit.
