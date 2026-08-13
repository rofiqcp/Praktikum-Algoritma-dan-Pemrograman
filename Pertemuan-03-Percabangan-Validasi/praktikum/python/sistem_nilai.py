def tentukan_grade(nilai):
    if nilai < 0 or nilai > 100:
        return None
    if nilai >= 90: return "A"
    if nilai >= 80: return "B"
    if nilai >= 75: return "C / Lulus"
    return "Belum lulus"

def main():
    nama = input("Nama siswa: ").strip()
    try:
        nilai = float(input("Nilai akhir: "))
    except ValueError:
        print("Nilai harus berupa angka."); return
    grade = tentukan_grade(nilai)
    print("Nilai tidak valid" if grade is None else f"{nama}: {grade}")

if __name__ == "__main__": main()
