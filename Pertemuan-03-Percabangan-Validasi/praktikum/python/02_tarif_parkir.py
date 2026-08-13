def hitung_tarif(jam, tarif_awal=5000, tarif_tambahan=3000):
    if jam <= 0: raise ValueError("Jam parkir harus > 0")
    return tarif_awal if jam <= 2 else tarif_awal + (jam-2)*tarif_tambahan

if __name__ == "__main__":
    try: print(f"Tarif: Rp{hitung_tarif(int(input('Lama parkir (jam): '))):,.0f}")
    except ValueError as e: print("Input tidak valid:",e)
