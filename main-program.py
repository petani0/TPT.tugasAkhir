print("|=================================================|")
print("|==================== Restoran ===================|")
print("|=================================================|\n")

# Import date time
from datetime import datetime

# men-set variable current(Day,Month,Year) dengan waktu yang ada di komputer/pc
currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year
print(currentDay, "/", currentMonth, "/", currentYear)


# Input Dictionaries
# Key : Menu | Value : Harga [Key-Value Pair]
# Dict menu
menu = {
    "ayam goreng": 15000,
    "burger king": 25000,
    "kentang goreng": 10000,
    "nasi goreng": 15000,
}

# Dict minuman
minuman = {
    "es teh manis": 5000,
    "coca cola": 7000,
    "jus jeruk": 10000,
    "jus alpukat": 15000,
}


# Ngebungkus/wrap semua function menjadi 1, bernama main function() untuk dijadiin neested function
def main():
    # Deklarasi function pemilihan
    def pemilihan():
        print("=================== Daftar Menu ===================")
        for i in menu:
            print(i,"\t  | Rp.",menu[i],)
        print("===================================================")
        print("Pembelian diatas Rp100.000,- mendapatkan diskon 15%")
        print("===================================================")
        
        # Untuk input, harus ketik sesuai dictionaries menu{}, karna python case-sensitive language
        # Input Makanan
        beli1 = input("Pilih Menu : ")
        jumlah1 = int(input("Jumlah Pesanan : "))
        print("\n")

        # Input Minuman
        print("=================== Daftar Minum ==================")
        for i in minuman:
            print(i,"\t  | Rp.",minuman[i],)
        # Input Minuman
        beli2 = input("Pilih Minum : ")
        jumlah2 = int(input("Jumlah Pesanan: "))
        print("\n")

        # PERHITUNGAN UNTUK PEMBAYARAN
        bayar = (menu[beli1] * jumlah1) + (minuman[beli2] * jumlah2)
        if bayar > 100000:
            diskon = bayar * 15 / 100
            total = bayar - diskon
        else:
            total = bayar
            bayar = (menu[beli1] * jumlah1) + (minuman[beli2] * jumlah2)

        # Print Detail Pembayaran
        print("============== Detail Pembayaran ==================")
        print("Menu yang di pesan       : ", beli1, "dan", beli2)
        print(
            f"Jumlah yang dipesan      :  {jumlah1} Makanan dan {jumlah2} Minuman",
        )
        print("Total Biaya              : ", bayar)
        print("Total yang harus dibayar : ", total)
        pembayaran = int(input("Bayar         :  "))
        kembalian = pembayaran - total

        # If-else statement jika uang yang di bayar perlu 'kembalian' , 'pas' atau 'kurang'
        # UANG PAS
        if pembayaran == total:
            print("Uang anda pas\n")
            tambah()

        # KEMBALIAN
        elif pembayaran > total:
            print("Kembalian        : ", kembalian)
            tambah()

        # UANG TIDAK CUKUP
        elif pembayaran < total:

            # MENANYAKAN APAKAH INGIN MEMESAN PESAN ULANG
            tanya = input(
                "Maaf uang anda tidak cukup, Apakah anda ingin memesan ulang? [y/t]:"
                )
            if tanya == "y":
                pemilihan()
            elif tanya == "t":
                print("===== Terima Kasih ======")
            else:
                # MENANYAKAN UNTUK KEDUA KALI JIKA INGIN MEMESAN ULANG
                print("Pilihan yang anda masukan salah!")
                tanya = tanya = input(
                    "Maaf uang anda tidak cukup, Apakah anda ingin memesan ulang? [y/t]:"
                )
                if tanya == "y":
                    pemilihan()
                elif tanya == "t":
                    print("===== Terima Kasih ======")
                else:
                    # JIKA PILIHAN SELAIN Y/T DIKELUARKAN LAGI, MAKA PROGRAM AKAN MEMAKSA LOGOUT
                    print("Pilihan yang anda masukan salah!, Anda Terpaksa Logout!")
    
    # function tambah(), Jika ingin memesan makanan lagi
    def tambah():
        print("=====================================")
        tanya = input("Apakah anda ingin memesan lagi? [y/t] : ")
        print("=====================================\n")
        if tanya == "y":
            pemilihan()
        elif tanya == "t":
            print("===== Terima Kasih ======")
        else:
            print("Pilihan yang anda masukan salah!")

    # Deklarasi function untuk login
    def get_login():
        print("*" * 30)
        print("Silahkan Login!")

        # input username dan password
        username = input("Masukan Username Anda: ")
        password = input("Masukan Password: ")

        # Menentukan username dan password
        if username == "melvin" and password == "melvin":
            print("Login Berhasil...\n\n")
            pemilihan()
        else:
            print("Login Gagal. Coba Lagi..")
            get_login()

    # Membuat program nge-execute function get_login() pertama kali
    if __name__ == "__main__":
        get_login()


# memanggil/memulai main() function
main()
