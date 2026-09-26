umur_3004 = int(input("Input Umur Anda"))
sim_3004 =input("Apakah Anda sudah punya sim C : ")[0]

if umur_3004 >= 17 and sim_3004 == 'y':
    print("anda Sudah dewasa dan boleh bawa motor")
elif umur_3004 >= 17 and sim_3004 != 'y':
    print("anda Sudah dewasa tetapi tidak boleh bawa motor")
elif umur_3004 < 17 and sim_3004 == 'y' :
    print("Anda Belum Cukup Umur punya SIM") 
else:
    print(" Anda belum cukup umur dan anda tidak boleh membawa motor")

print("program selesai")