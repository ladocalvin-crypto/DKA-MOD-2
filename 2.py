import numpy as np

n = int(input("Masukkan jumlah barang: "))

data = []

for i in range(n):
    print("\nData Barang ke-", i+1)

    nama = input("Nama Barang : ")
    kode = input("Kode Barang : ")
    jumlah = int(input("Jumlah      : "))
    harga = float(input("Harga/Unit  : "))

    data.append([nama, kode, jumlah, harga])

data = np.array(data, dtype=object)

print("\n=== DATA INVENTARIS ===")
for barang in data:
    print("Nama:", barang[0], "| Kode:", barang[1], "| Jumlah:", barang[2], "| Harga:", barang[3])

jumlah = data[:,2].astype(int)
harga = data[:,3].astype(float)

total_barang = jumlah * harga
total_inventaris = np.sum(total_barang)

print("\nTotal Nilai Inventaris:", total_inventaris)

cari = input("\nMasukkan Nama Barang atau Kode Barang: ")

for barang in data:
    if cari == barang[0] or cari == barang[1]:
        print("\nData Barang Ditemukan:")
        print("Nama Barang :", barang[0])
        print("Kode Barang :", barang[1])
        print("Jumlah      :", barang[2])
        print("Harga Unit  :", barang[3])
        print("Total Nilai :", int(barang[2]) * float(barang[3]))