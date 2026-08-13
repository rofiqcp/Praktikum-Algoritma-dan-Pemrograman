awal = int(input("Awal: "))
akhir = int(input("Akhir: "))

print("Bilangan genap:")
for angka in range(awal, akhir + 1):
    if angka % 2 == 0:
        print(angka)
