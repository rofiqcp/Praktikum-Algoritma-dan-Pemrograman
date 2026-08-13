# Materi Pertemuan 11 — Deployment: Dari GitHub ke Aplikasi Publik

> Sumber utama: *Buku Panduan Praktik: Pemrograman Dasar hingga Full Stack — 16 Pertemuan Terstruktur, Edisi Agustus 2026*. Detail platform deployment, paket gratis, dan batas resource dapat berubah; periksa dokumentasi resmi terbaru sebelum praktik.

Tujuan sesi adalah memahami bagaimana source code lokal menjadi service yang dapat diakses melalui internet, serta bagaimana membaca build/runtime log ketika deployment gagal.

## Target Kompetensi
- Membedakan local development, build, deploy, runtime, domain, dan environment variable.
- Menyiapkan `requirements.txt`, `.gitignore`, dan entrypoint yang benar.
- Mendeploy dari GitHub ke minimal satu platform.
- Mengenal variasi Vercel, Render, Railway, PythonAnywhere, dan static hosting.
- Membaca build log dan runtime log.

## Output
- Aplikasi Python mempunyai public URL.
- Secret dipindahkan ke environment variable.
- README mempunyai bagian deployment dan troubleshooting.

## Mental Model Deployment
```text
LOCAL SOURCE → GIT COMMIT → GITHUB → BUILD → RUNTIME/SERVICE → PUBLIC URL
                          ↘ ENVIRONMENT VARIABLES / LOGS ↗
```

## Local vs Production
- Local: dependency dan config ada di komputer developer.
- Build: platform menyiapkan dependency/artifact.
- Runtime: proses aplikasi benar-benar hidup.
- Public URL/domain: alamat service yang dapat diakses client.
- Environment variable: konfigurasi diberikan di environment, bukan hard-code ke source.

## File Minimum
```text
app.py
requirements.txt
Procfile        # bila platform memakai start command model ini
.env.example    # hanya nama variable/contoh aman
.gitignore
README.md
```

## Environment Variable
```python
import os
port = int(os.getenv("PORT", "5000"))
secret = os.getenv("APP_SECRET", "dev-only")
```
Jangan commit `.env` atau token sungguhan. `.env.example` boleh berisi placeholder.

## Health Check
Endpoint seperti `/health` membantu membedakan “deploy berhasil” dari “service benar-benar siap menerima request”.

## Platform
Buku mengenalkan Vercel, Render, Railway, PythonAnywhere, dan static hosting sebagai variasi deployment. Gunakan dokumentasi resmi pada hari praktikum karena runtime, command, plan, dan batas resource dapat berubah.

## Troubleshooting Berdasarkan Layer
| Gejala | Fokus |
|---|---|
| Build gagal | dependency, version, syntax, build command |
| Deploy sukses tapi URL 5xx | runtime log, start command, import, env var |
| App bind port salah | gunakan port yang diberikan environment bila platform meminta |
| Secret tidak terbaca | nama env var/config platform |
| Works local, fail cloud | filesystem, path, case-sensitive filename, version/runtime |
| 404 publik | routing/base path/deployment target |

## Kebiasaan Wajib
1. Reproduce.
2. Baca build/runtime log.
3. Tentukan layer gagal.
4. Uji perubahan kecil.
5. Commit fix yang spesifik.
6. Redeploy dan regression test dari perangkat/browser lain.
