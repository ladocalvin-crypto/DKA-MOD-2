import numpy as np

n = int(input("Masukkan jumlah mahasiswa: "))

data = []

for i in range(n):
    print("\nData Mahasiswa ke-", i+1)

    nama = input("Nama        : ")
    nim = input("NIM         : ")
    nilai = float(input("Nilai      : "))
    tahun = int(input("Tahun Masuk: "))

    data.append([nama, nim, nilai, tahun])

data = np.array(data, dtype=object)

print("\nDATA MAHASISWA")
for mhs in data:
    print("Nama:", mhs[0], "| NIM:", mhs[1], "| Nilai:", mhs[2], "| Tahun:", mhs[3])

nilai = data[:,2].astype(float)

print("\nNilai Tertinggi :", np.max(nilai))
print("Nilai Terendah  :", np.min(nilai))
print("Nilai Rata-rata :", np.mean(nilai))

cari = input("\nMasukkan Nama atau NIM yang dicari: ")

for mhs in data:
    if cari == mhs[0] or cari == mhs[1]:
        print("\nData ditemukan:")
        print("Nama:", mhs[0])
        print("NIM:", mhs[1])
        print("Nilai:", mhs[2])
        print("Tahun Masuk:", mhs[3]) 