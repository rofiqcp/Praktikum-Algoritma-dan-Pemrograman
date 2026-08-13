jarak_km = float(input("Jarak (km): "))
km_per_liter = float(input("Efisiensi kendaraan (km/liter): "))
nilai_per_liter = float(input("Nilai per liter: "))

liter_dibutuhkan = jarak_km / km_per_liter
total_nilai = liter_dibutuhkan * nilai_per_liter

print(f"Kebutuhan cairan : {liter_dibutuhkan:.2f} liter")
print(f"Estimasi total   : {total_nilai:,.0f}")
