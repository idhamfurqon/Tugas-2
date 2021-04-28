



nama = []
notelepon = []

def datakontak(): 
    print("Daftar Kontak :")
    for x in range(len(nama)):
        print("Nama : {}".format(nama[x]))
        print("No Telepon : {}".format(notelepon[x]))
        
def tambahkontak(): 
    nama.append(input("Nama :"))
    notelepon.append (int(input("No Telepon :")))
    print("Kontak berhasil ditambahkan")
  

print("Selamat datang!")
while True:
    print("----- Menu -----")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    menu = int(input("Pilih Menu :"))
    if menu == 1:
        datakontak()
    elif menu == 2:
        tambahkontak()
    elif menu == 3:
        print("Program selesai, sampai jumpa kembali!")
        break
    else:
        print("Menu tidak tersedia")
    