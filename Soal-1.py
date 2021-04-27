namakontak = []
notelepon = []

def daftarkontak(): 
    print("Daftar Kontak :")
    for i in range(len(namakontak)):
        print("Nama : {}".format(namakontak[i]))
        print("No Telepon : {}".format(notelepon[i]))
        
def tambahkontak(): 
    namakontak.append(input("Nama :"))
    notelepon.append(int(input("No Telepon :")))
    print("Kontak berhasil ditambahkan")

print("Selamat datang!")
while True:
    print("----- Menu -----")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    menu = int(input("Pilih Menu :"))
    if menu == 1:
        daftarkontak()
    elif menu == 2:
        tambahKontak()
    elif menu == 3:
        print("Program selesai, sampai jumpa!")
        break
    else:
        print("Menu tidak tersedia")