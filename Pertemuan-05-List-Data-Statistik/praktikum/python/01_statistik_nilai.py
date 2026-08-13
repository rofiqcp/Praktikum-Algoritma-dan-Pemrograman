def statistik(data):
    if not data: return None
    return {"jumlah":len(data),"min":min(data),"max":max(data),"rata":sum(data)/len(data),"lulus":sum(n>=75 for n in data)}

if __name__ == "__main__":
    data=[]
    try:
        jumlah=int(input("Jumlah siswa: "))
        for i in range(jumlah):
            n=float(input(f"Nilai {i+1}: "))
            if 0 <= n <= 100: data.append(n)
            else: print("Nilai diabaikan: harus 0-100")
    except ValueError: print("Input harus angka.")
    hasil=statistik(data)
    print("Belum ada data." if hasil is None else hasil)
