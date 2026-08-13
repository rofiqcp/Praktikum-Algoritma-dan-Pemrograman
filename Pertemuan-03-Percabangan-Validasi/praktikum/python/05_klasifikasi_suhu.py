def kategori_suhu(c):
    if c < 18: return "dingin"
    if c <= 27: return "nyaman"
    return "panas"

if __name__ == "__main__": print("Kategori:",kategori_suhu(float(input("Suhu Celsius: "))))
