def hitung_diskon(total,member):
    if total<0: raise ValueError("total tidak boleh negatif")
    return total*0.10 if member and total>=100_000 else 0.0
