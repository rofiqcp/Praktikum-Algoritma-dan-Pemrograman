def rata_rata_bug(data):
    total=0
    for nilai in data:
        total=nilai  # sengaja salah untuk latihan
        print("TRACE total =",total)
    return total/len(data)

def rata_rata_benar(data):
    if not data: raise ValueError("data kosong")
    total=0
    for nilai in data: total += nilai
    return total/len(data)

if __name__ == "__main__":
    data=[80,90,70]
    print("Bug:",rata_rata_bug(data))
    print("Benar:",rata_rata_benar(data))
