umur_3004 =int(input(" Input Umur Anda"))
sim =input("Apakah Anda Sudah Punya Sim C (y/t): ")[0]

if umur_3004 >= 17 and sim == 'y' :
    print("Anda Sudah dewasa dan Anda Boleh Bawa Motor")

if umur_3004 >= 17 and sim != 'y' :
    print("Anda Sudah dewasa dan Anda Tidak Boleh Bawa Motor")

if umur_3004 < 17 and sim == 'y' :
    print("Anda Belum Cukup Umur punya SIM")    

if umur_3004 < 17 and sim != 'y' :
    print("Anda Belum Cukup Umur punya SIM dan Bawa Motor")       