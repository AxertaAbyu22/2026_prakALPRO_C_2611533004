batas_3004 =int(input("masukan nilai batas: "))
for line_3004 in range(1, batas_3004 + 1):
    for j_3004 in range(1, (-1 * line_3004 + batas_3004) + 1):
        print(".", end=" ")
    print(line_3004)