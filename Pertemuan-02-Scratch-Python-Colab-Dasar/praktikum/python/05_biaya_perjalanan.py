def estimasi_biaya(jarak_km, km_per_liter, harga_per_liter):
    liter = jarak_km / km_per_liter
    return liter, liter * harga_per_liter

def main():
    jarak = float(input("Jarak perjalanan (km): "))
    efisiensi = float(input("Konsumsi kendaraan (km/l): "))
    harga = float(input("Harga BBM per liter: "))
    if efisiensi <= 0:
        print("Konsumsi km/l harus > 0.")
        return
    liter, biaya = estimasi_biaya(jarak, efisiensi, harga)
    print(f"Estimasi BBM : {liter:.2f} liter")
    print(f"Estimasi biaya: Rp{biaya:,.0f}")

if __name__ == "__main__":
    main()
