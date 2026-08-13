def konversi_menit(total_menit):
    return total_menit // 60, total_menit % 60

def main():
    menit = int(input("Total menit: "))
    jam, sisa = konversi_menit(menit)
    print(f"{menit} menit = {jam} jam {sisa} menit")

if __name__ == "__main__":
    main()
