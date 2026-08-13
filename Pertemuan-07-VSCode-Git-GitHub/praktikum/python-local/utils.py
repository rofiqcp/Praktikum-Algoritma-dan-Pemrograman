def hitung_diskon(total, member):
    if total < 0:
        raise ValueError("total tidak boleh negatif")
    if member and total >= 100_000:
        return total * 0.10
    return 0.0

def hitung_bayar(total, member):
    return total - hitung_diskon(total, member)

def format_rupiah(nilai):
    return f"Rp{nilai:,.0f}"
