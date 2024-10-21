#contoh maslah 1: menghitung gaji karyawan dengan bonus

#input data
pilihan = input("apakah anda merupakan member toko FAVO: \n1. Ya\n2. Tidak\nMasukkan pilhan anda: ")
minimal_pembelajaan = 500000

#percabangan bersarang untuk menghitung bonus
if pilihan == "1":
    total_belanja = int(input("masukkan total belanjaan: "))
    if total_belanja >= minimal_pembelajaan:
        print("anda mendapatkan diskon: 50%")
        diskon = total_belanja * 50/100
        hasil = total_belanja - diskon
        print("Total belanjaan anda adalah:", hasil)
    else:
        print("anda mendapatkan diskon: 10%")
        diskon = total_belanja * 10/100
        hasil = total_belanja - diskon
        print("Total belanjaan anda adalah:", hasil)
elif pilihan == "2":
    pilihan = "tidak"
    total_belanja = int(input("masukkan total belanjaan: "))
    if total_belanja >= minimal_pembelajaan:
        print("anda mendapatkan diskon: 25%")
        diskon = total_belanja * 25/100
        hasil = total_belanja - diskon
        print("Total belanjaan anda adalah:", hasil)
    else:
        print("anda mendapatkan diskon: Tidak Mendapatkan Diskon")
        diskon = 0
        hasil = total_belanja - diskon
        print("Total belanjaan anda adalah:", hasil)
else:
    print ("pernytaan anda tidak valid, silahkan jlankan program kembali")