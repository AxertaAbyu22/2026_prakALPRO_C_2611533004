ulang_3004=int(input("masukan nilai batas: "))

jumlah_3004 = 0
for i_3004 in range(1, ulang_3004 + 1):
    if i_3004 % 2 == 0:
        print(i_3004, end=" ")
        jumlah_3004 = jumlah_3004 + i_3004
        
        if i_3004 < ulang_3004:
            print (" + ", end="")
        else:
            print (" = ", jumlah_3004, end="")
print()
print(" jumlah = ", jumlah_3004)