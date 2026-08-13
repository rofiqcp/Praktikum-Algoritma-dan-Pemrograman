def celsius_ke_fahrenheit(c):
    return c * 9 / 5 + 32

def celsius_ke_kelvin(c):
    return c + 273.15

def main():
    c = float(input("Suhu Celsius: "))
    print(f"Fahrenheit: {celsius_ke_fahrenheit(c):.2f} F")
    print(f"Kelvin    : {celsius_ke_kelvin(c):.2f} K")

if __name__ == "__main__":
    main()
