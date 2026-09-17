print("===============================")
print("3, OPERATOR BITWISE")
print("===============================")

angka1_3004=int(input("masukan angka bitwise-1: "))
angka2_3004=int(input("masukan angka bitwise-2: "))

print("\nAngka dalam bentuk biner dan desimal")
print("Angka 1 - Biner:", bin(angka1_3004), "- Desimal:", angka1_3004)
print("Angka 2 - Biner:", bin(angka2_3004), "- Desimal:", angka2_3004)

#Bitwise AND
hasil_3004= angka1_3004 & angka2_3004
print("\nOperator Bitwise AND (&)")
print(angka1_3004, "&", angka2_3004, "=", hasil_3004, "- Biner:", bin(hasil_3004))
print("Biner hasil (8 bit):", format(hasil_3004, '08b'))

#Bitwise OR
hasil_3004= angka1_3004 | angka2_3004
print("\nOperator Bitwise OR (|)")
print(angka1_3004, "|", angka2_3004, "=", hasil_3004,)
print("biner hasil =", bin(hasil_3004))
print("Biner hasil (8 bit):", format(hasil_3004, '08b'))

#Bitwise XOR
hasil_3004= angka1_3004 ^ angka2_3004   
print("\nOperator Bitwise XOR (^)")
print(angka1_3004, "^", angka2_3004, "=", hasil_3004,)
print("biner hasil =", bin(hasil_3004))
print("Biner hasil (8 bit):", format(hasil_3004, '08b'))

#bitwise NOT
hasil_3004= ~angka1_3004
print("\nOperator Bitwise NOT (~)")
print("~", angka1_3004, "=", hasil_3004,)
print("biner hasil =", bin(hasil_3004))
print("Biner hasil (8 bit):", format(hasil_3004, '08b'))

#bitwise left shift
jumlah_shift_3004 = int(input("\nMasukan jumlah pergeseran bit ke kiri: "))

hasil_3004= angka1_3004 << jumlah_shift_3004
print("\nOperator Bitwise Left Shift (<<)")
print(angka1_3004, "<<", jumlah_shift_3004, "=", hasil_3004,)
print("biner hasil =", bin(hasil_3004))
print("Biner hasil (8 bit):", format(hasil_3004, '08b'))

#bitwise right shift
hasil_3004= angka1_3004 >> jumlah_shift_3004
print("\nOperator Bitwise Right Shift (>>)")
print(angka1_3004, ">>", jumlah_shift_3004, "=", hasil_3004,)
print("biner hasil =", bin(hasil_3004))
print("Biner hasil (8 bit):", format(hasil_3004, '08b'))