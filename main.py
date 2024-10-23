def converttemperature(temp_value, temp_unit):
    
    if temp_unit.upper() == 'C':
        # Mengonversi Celsius ke Fahrenheit
        converted_temp = (temp_value * 9/5) + 32
        return converted_temp
    elif temp_unit.upper() == 'F':
        # Mengonversi Fahrenheit ke Celsius
        converted_temp = (temp_value - 32) * 5/9
        return converted_temp
    else:
        raise ValueError("Unit suhu tidak valid. Harap gunakan 'C' untuk Celsius atau 'F' untuk Fahrenheit.")

# Penggunaan contoh:
def main():
    temp_value = float(input("Masukkan nilai suhu: "))
    temp_unit = input("Masukkan unit suhu (C/F): ")
    
    try:
        converted_temp = converttemperature(temp_value, temp_unit)
        print(f"{temp_value} {temp_unit} sama dengan {converted_temp} {'F' if temp_unit.upper() == 'C' else 'C'}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
            