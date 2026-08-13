nama_barang = input("Nama barang: ")
harga_satuan = float(input("Harga satuan: "))
jumlah = int(input("Jumlah: "))
total = harga_satuan * jumlah

print(f"Barang : {nama_barang}")
print(f"Jumlah : {jumlah}")
print(f"Total  : Rp{total:,.0f}")
