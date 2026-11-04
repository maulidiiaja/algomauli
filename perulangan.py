print("======PROGRAM PERULANGAN======")

jmlh = int(input("Masukkan jumlah Mahasiswa : "))

if jmlh >=5 and jmlh <=10:
        totaln = 0
        
        for h in range(1, jmlh + 1):
              nilai = int(input(f"Masukkan Nilai Mahasiswa-{h}: "))
              totaln += nilai
              
        rata2 = totaln / jmlh
        
        print()
        print("==========HASIL PENILAIN==========")
        print("Jumlah Nilai Mahasiswa   : ", jmlh)
        print("Total Nilai              : ", totaln)
        print("Nilai Rata-Rata          : ", rata2)

else:
       print("Jumlah Nilai yang Diinputkan harus 5 sampai 10")

