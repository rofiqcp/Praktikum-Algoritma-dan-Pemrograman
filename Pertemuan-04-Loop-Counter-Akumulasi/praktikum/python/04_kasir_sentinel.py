total = 0
jumlah_data = 0

nilai = float(input("Masukkan nilai, 0 untuk selesai: "))
while nilai != 0:
    total += nilai
    jumlah_data += 1
    nilai = float(input("Masukkan nilai, 0 untuk selesai: "))

print("Jumlah data:", jumlah_data)
print("Total:", total)
