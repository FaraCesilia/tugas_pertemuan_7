import function

daftar_kontak = []

while True:
    print("----DAFTAR MENU----")
    print("|1. Daftar Kontak |")
    print("|2. Tambah Kontak |")
    print("|3. Cari Kontak   |")
    print("|4. Hapus Kontak  |")
    print("|5. Keluar Program|")
    print("-------------------")
    pilih = input("Silakan Pilih Menu: ")

    if pilih == "5":
        break
    elif pilih == "1":
        function.tampil(daftar_kontak)
    elif pilih == "2":
        kontak = function.kontak_baru()
        daftar_kontak.append(kontak)
    elif pilih == "3":
        function.cari(daftar_kontak)
    elif pilih == "4":
        function.hapus(daftar_kontak)
    else:
        print(10*"=")
        print("Menu Tidak Tersedia!")

print("Anda Keluar Dari Program! \nSampai Jumpa Lagi! <3")