tinggi_3004= int(input("masukan tinggi pola(bilangan genap, misal 10): "))

if tinggi_3004 % 2 != 0:
    print("maaf, tinggi pola harus bilangan genap")
else:
    a_3004 = tinggi_3004
    c_3004 = a_3004 
    lebar_3004 =(2 * tinggi_3004) - 2

    for i_3004 in range(1, tinggi_3004 + 1):
        b_3004 = c_3004 + 1

        for j_3004 in range(1, lebar_3004 + 1):

            # Baris atas dan bawah
            if i_3004 == 1 or i_3004 == tinggi_3004:
                if j_3004 == 1 or j_3004 == lebar_3004:
                    print("#", end="")
                else:
                    print("=", end="")
            # Baris isi
            else:
                if j_3004 == 1 or j_3004 == lebar_3004:
                    print("|", end="")
                else:
                    if j_3004 == c_3004:
                        print("<", end="")
                    elif j_3004 == b_3004:
                        print(">", end="")
                    elif j_3004 == (lebar_3004 - c_3004):
                        print("<", end="")
                    elif j_3004 == (lebar_3004 - c_3004 + 1):
                        print(">", end="")
                    elif j_3004 > b_3004 and j_3004 < (lebar_3004 - c_3004):
                        print(".", end="")
                    else:
                        print(" ", end="") 

        print() 

        # logika asli java
        a_3004 -= 2

        if a_3004 <= 0:
            c_3004 = (-a_3004) + 2
        else:
            c_3004 = a_3004