def validasi(nilai): return 0 <= nilai <= 100

def grade(nilai):
    if not validasi(nilai): raise ValueError("Nilai harus 0-100")
    if nilai >= 90: return "A"
    if nilai >= 80: return "B"
    if nilai >= 75: return "C / Lulus"
    return "Belum lulus"

def laporan(nama,nilai): return f"{nama}: {nilai:.1f} → {grade(nilai)}"

if __name__ == "__main__":
    try: print(laporan(input("Nama: ").strip(),float(input("Nilai: "))))
    except ValueError as e: print("Error:",e)
