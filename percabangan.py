# #input
# nilai = int(input("Masukkan Nilai = "))
# #proses
# if nilai >=80 and nilai <=100:
#     print("Anda Mendapatkan Nilai A")
# elif nilai >=70 and nilai <=80:
#     print("Anda Mendapatkan Nilai B")
# elif nilai >=50 and nilai <=70:
#     print("Anda Mendapatkan Nilai C")
# elif nilai >=30 and nilai <=50:
#     print("Anda Mendapatkan Nilai D")
# elif nilai >=0 and nilai <=30:
#     print("Anda Mendapatkan Nilai E")
# else:
#     print("Data Tidak Valid")

print()
print("===========Latihan===========")
#input
barang = input("Masukkan Nama Barang : ")
harga = int(input("Masukkan Harga : "))
#proses
if barang =="kulkas":
    print(barang)
    print(harga - (0.10 * harga))
elif barang =="tv":
    print(barang)
    print(harga - (0.05 * harga))
else:
    print(barang)
    print(harga)

