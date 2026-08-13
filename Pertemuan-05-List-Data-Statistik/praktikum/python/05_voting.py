from collections import Counter

def hitung(suara,kandidat):
    valid=[s for s in suara if s in kandidat]
    return Counter(valid)

if __name__ == "__main__":
    kandidat=["Ayu","Bima","Citra"]; suara=[]
    print("Kandidat:",", ".join(kandidat),"; ketik selesai untuk berhenti")
    while True:
        s=input("Suara: ").strip()
        if s.lower()=="selesai": break
        if s not in kandidat: print("Kandidat tidak valid"); continue
        suara.append(s)
    print("Hasil:",dict(hitung(suara,kandidat)))
