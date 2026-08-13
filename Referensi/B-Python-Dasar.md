> Diadaptasi langsung dari lampiran/panduan pada buku sumber Edisi Agustus 2026.

# Lampiran B — Python Dasar Cheat Sheet

```python
nama = "Ayu"
umur = 16
nilai = 87.5
aktif = True

nama = input("Nama: ")
umur = int(input("Umur: "))

if umur >= 17:
    print("Kategori A")
else:
    print("Kategori B")

for i in range(5):
    print(i)

items=[]
items.append("Buku")
for item in items:
    print(item)

produk={"name":"Buku","stock":5}
print(produk["name"])

def tambah(a,b):
    return a+b
```

## Kesalahan Umum Python
| Gejala | Kemungkinan penyebab | Pemeriksaan/perbaikan |
|---|---|---|
| SyntaxError | kurung/colon/quote salah | baca caret `^` dan baris error |
| IndentationError | indentasi blok salah | 4 spasi konsisten |
| NameError | variable belum dibuat/typo | cek nama dan urutan eksekusi |
| TypeError | tipe tidak kompatibel | cek `type()` dan konversi |
| ValueError | isi tak dapat dikonversi | validasi input |
| IndexError | index di luar list | cek `len` dan batas |
| KeyError | key dict tidak ada | cek key/`.get()` |
| ModuleNotFoundError | package/environment salah | aktifkan venv dan install package |
