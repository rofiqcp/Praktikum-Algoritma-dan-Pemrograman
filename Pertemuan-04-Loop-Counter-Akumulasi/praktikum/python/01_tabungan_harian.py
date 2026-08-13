saldo = 0
hari = int(input("Berapa hari menabung? "))
setoran = float(input("Setoran per hari: "))

for i in range(1, hari + 1):
    saldo += setoran
    print(f"Hari {i}: saldo Rp{saldo:,.0f}")

print(f"Saldo akhir: Rp{saldo:,.0f}")
