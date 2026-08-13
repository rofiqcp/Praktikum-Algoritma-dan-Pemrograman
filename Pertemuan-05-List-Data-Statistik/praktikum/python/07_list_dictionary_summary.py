produk = [
    {"nama": "Keyboard", "harga": 250000, "stok": 10},
    {"nama": "Mouse", "harga": 120000, "stok": 5},
    {"nama": "Headset", "harga": 300000, "stok": 4},
]

print("Jumlah produk:", len(produk))
print("Total stok:", sum(item["stok"] for item in produk))

for item in produk:
    status = "stok rendah" if item["stok"] < 5 else "stok cukup"
    print(f'{item["nama"]}: {item["stok"]} ({status})')
