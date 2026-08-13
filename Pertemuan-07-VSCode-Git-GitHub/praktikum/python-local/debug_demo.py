# Latihan debugging: jalankan, baca traceback, cari baris, buat hipotesis, perbaiki pada salinan.
def rata_rata(total,jumlah):
    return total/jumlah

if __name__ == "__main__":
    print(rata_rata(100,0))  # sengaja ZeroDivisionError
