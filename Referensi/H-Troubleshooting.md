> Diadaptasi langsung dari lampiran/panduan pada buku sumber Edisi Agustus 2026.

# Lampiran H — Decision Tree Troubleshooting

| Pertanyaan | Jika YA | Jika TIDAK |
|---|---|---|
| Program bisa start? | lanjut tes fitur | baca syntax/import/startup log |
| URL dapat dihubungi? | cek status code | cek server, host, port, firewall |
| Status 2xx? | periksa data/UI | kelompokkan 4xx vs 5xx |
| 4xx? | cek request/auth/route/validation | jika 5xx baca traceback backend |
| Backend 2xx tapi UI salah? | cek JS/render/state | cek response/network |
| Data tidak tersimpan? | cek query/commit/database | cek layer sebelum DB |
| Hanya gagal deploy? | bandingkan env/path/port/filesystem/version | reproduksi lokal |

## Checklist Bukti Sebelum Bertanya
- [ ] Langkah reproduksi jelas.
- [ ] Expected vs actual ditulis.
- [ ] Error log relevan lengkap.
- [ ] Version/environment disebutkan.
- [ ] Struktur file relevan disebutkan.
- [ ] Perubahan terakhir diketahui.
- [ ] Sudah mencoba small test.
- [ ] Tidak menyertakan secret/private data.
