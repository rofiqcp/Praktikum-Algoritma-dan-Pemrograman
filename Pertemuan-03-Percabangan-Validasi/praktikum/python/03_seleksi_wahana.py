def boleh_naik(usia, tinggi_cm):
    return usia >= 10 and tinggi_cm >= 130

if __name__ == "__main__":
    usia=int(input("Usia: ")); tinggi=float(input("Tinggi badan (cm): "))
    print("Boleh naik wahana." if boleh_naik(usia,tinggi) else "Belum memenuhi syarat.")
