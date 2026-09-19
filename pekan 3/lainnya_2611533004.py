print("===============================")    
print("1, OPERATOR KEANGGOTAAN")
print("===============================")

input_data_3004 =input("Masukan beberapa angka, pisahkan dengan koma:")

data_3004=[int(angka.strip()) for angka in input_data_3004.split(",")]

nilai_dicari = [int(input("Masukan angka yang dicari: "))]

#Operator keanggotaan in
hasil_3004 = nilai_dicari in data_3004
print("\nOperator keanggotaan IN")
print(nilai_dicari, "in", data_3004, "=", hasil_3004)

# Operator keanggotaan not in
hasil_3004 = nilai_dicari not in data_3004
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari, "not in", data_3004, "=", hasil_3004)   

print("===============================")
print("2, OPERATOR IDENTITAS")
print("===============================")

# Objek1_3004 menggunakan list dari input pengguna
objek1_3004 = data_3004 

# Objek1_3004 merujuk pada
objek2_3004 = objek1_3004

objek3_3004 = data_3004.copy()

print("objek1_3004 =" ,objek1_3004)
print("objek2_3004 =" ,objek2_3004)
print("objek3_3004 =" ,objek3_3004)

#Operator identitas is
hasil_3004 = objek1_3004 is objek2_3004
print("\nOperator identitas IS")
print("objek1_3004 is objek2_3004 =", hasil_3004)

#Operator identitas is not
hasil_3004 = objek1_3004 is not objek3_3004
print("\nOperator identitas IS NOT")
print("objek1_3004 is not objek3_3004 =", hasil_3004)

#Membandiingkan identitas dan nilai
print("\nMembandingkan identitas dan nilai")
print("objek1_3004 is objek3_3004 =", objek1_3004 is objek3_3004)
print("objek1_3004 == objek3_3004 =", objek1_3004 == objek3_3004)       