tinggi_3004 = int(input("masukan tinggi segitiga: "))

for i_3004 in range(1, tinggi_3004 + 1):
    print("", end=" ")

    for j_3004 in range(tinggi_3004 - i_3004):
        print("", end=" ")

    for j_3004 in range(1, i_3004 ):
        print("*", end=" ")

    print()