def simulasi_tabungan(hari, setoran):
    if hari < 0 or setoran < 0:
        raise ValueError("hari dan setoran tidak boleh negatif")
    saldo = 0.0
    riwayat = []
    for i in range(1, hari + 1):
        saldo += setoran
        riwayat.append((i, saldo))
    return riwayat, saldo

if __name__ == "__main__":
    try:
        hari=int(input("Berapa hari menabung? ")); setoran=float(input("Setoran per hari: "))
        riwayat,saldo=simulasi_tabungan(hari,setoran)
        for i,nilai in riwayat: print(f"Hari {i}: Rp{nilai:,.0f}")
        print(f"Saldo akhir: Rp{saldo:,.0f}")
    except ValueError as e: print("Input tidak valid:",e)
