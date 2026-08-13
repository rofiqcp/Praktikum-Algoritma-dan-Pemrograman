def grade(nilai):
    if nilai < 0 or nilai > 100: return None
    if nilai >= 90: return "A"
    if nilai >= 80: return "B"
    if nilai >= 75: return "C / Lulus"
    return "Belum lulus"

def main():
    nama=input("Nama siswa: ").strip(); nilai=float(input("Nilai akhir: "))
    hasil=grade(nilai)
    print("Nilai tidak valid. Gunakan 0-100." if hasil is None else f"{nama}: {hasil}")

if __name__ == "__main__": main()
