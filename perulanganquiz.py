print("===================================")
print(" PROGRAM KELULUSAN UJIAN MATEMATIKA")
print("===================================")

mhs = input("Masukkan Nama Mahasiswa : ")

if mhs.lower() == 'andi':
    tbatas = 70
elif mhs.lower() == 'budi':
    tbatas = 75
elif mhs.lower() == 'citra':
    tbatas = 80
else:
    tbatas = int(input("Masukkan Target Nilai Mahasiswa : "))

print()
print("Nama mahasiswa :", mhs)
print("Target nilai  :", tbatas)
print()

percobaan = 1
lulus = False

while percobaan <= 3 and not lulus:
    print("Percobaan ke- ", percobaan)
    nilai = int(input("Masukkan nilai ujian: "))

    if nilai >= tbatas:
        print("Selamat! Anda LULUS.")
        lulus = True
    else:
        print("Nilai anda belum mencapai target.")
        print("Silahkan mengikuti remedial.")
    
    print()
    
    if not lulus and percobaan < 3:
        percobaan += 1
    elif not lulus and percobaan == 3:
        break
    
    if lulus:
        break
    else:
        if percobaan < 3:
            percobaan += 1
        else:
            break

print("===================================")
print("           HASIL AKHIR             ")
print("===================================")
if lulus:
    print(f"{mhs} berhasil lulus!")
    print("Jumlah percobaan: ", percobaan)
else:
    print(f"{mhs} tidak lulus setelah 3 kali percobaan!")
    print("Jumlah percobaan: 3")
print("===================================")

