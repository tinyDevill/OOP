import math

while True:
    try:
        a = int(input("Masukkan angka: "))        
        if a == 0:
            raise ValueError("Input tidak boleh sama dengan nol")
        elif a < 0:
            raise ValueError("Input tidak boleh negatif")
        else:
            print(f"Akar dari {a}: {math.sqrt(a)}")

        break
    except ValueError as e:
        if "invalid literal for int() with base 10" in str(e):
            print("Invalid input. Masukkan angka")
        else:
            print(e)