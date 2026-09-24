bulan_3004 =int(input("Masukan Bulan (1-12): "))

match bulan_3004:
    case 1:
        print("Januari")
    case 2:
        print("februari")
    case 3:
        print("Maret")
    case 4:
        print("April")
    case 5:
        print("Mei")
    case 6:
        print("Juni")
    case 7:
        print("July")
    case 8:
        print("Agustus")
    case 9:
        print("September")
    case 10:
        print("Oktober")
    case 11:
        print("November")
    case 12:
        print("Desember")
    case _:
        print("Angka tidak Valiid")

print("Program Selesai")