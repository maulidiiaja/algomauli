print("================================")
print("   Sistem Penilaian Akademik")
print("================================")

def nilai_kategori(nilai):
    if nilai >= 85:
        return "A (Sangat Baik)"
    elif nilai >= 75:
        return "B (Baik)"
    elif nilai >= 60:
        return "C (Cukup)"
    else:
        return "D (Tidak Lulus)"

data = []
lulus = 0
tidak_lulus = 0

jumlah = int(input("Masukkan jumlah mahasiswa: "))

for i in range(jumlah):
    print("--- Mahasiswa ke-", i+1, "---")
    nama = input("Nama Mahasiswa: ")
    nilai = int(input("Nilai: "))

    kategori = nilai_kategori(nilai)
    data.append((nama, nilai, kategori))

    if nilai >= 60:
        lulus += 1
    else:
        tdk_lulus += 1

# 5. Tampilkan Hasil
print("\n=== HASIL PENILAIAN ===")
for nama, nilai, kategori in data:
    print("Nama: ", nama)
    print("Nilai: ", nilai)
    print("Kategori: ", kategori)

print("-----------------------")
print("Jumlah Lulus: ", lulus)
print("Jumlah Tidak Lulus: ",tdk_lulus)