# Mengimpor modul math untuk konstanta pi
import math

# Mendefinisikan fungsi lambda
circle_area = lambda radius: math.pi * (radius ** 2)

# Penggunaan contoh:
def main():
    radius = float(input("Masukkan jari-jari lingkaran: "))
    
    if radius < 0:
        print("Error: Jari-jari tidak boleh negatif.")
    else:
        area = circle_area(radius)
        print(f"Luas lingkaran dengan jari-jari {radius} adalah {area:.2f} satuan persegi.")

if __name__ == "__main__":
    main()