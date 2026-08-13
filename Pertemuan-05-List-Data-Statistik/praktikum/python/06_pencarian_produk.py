produk = [
    {"nama": "Keyboard", "harga": 250000, "stok": 10},
    {"nama": "Mouse", "harga": 120000, "stok": 5},
    {"nama": "Headset", "harga": 300000, "stok": 4},
]

keyword = input("Cari nama produk: ").strip().lower()
ditemukan = False

for item in produk:
    if item["nama"].lower() == keyword:
        print("Nama :", item["nama"])
        print("Harga:", item["harga"])
        print("Stok :", item["stok"])
        ditemukan = True

if not ditemukan:
    print("Produk tidak ditemukan.")
