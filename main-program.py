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
menu = {
    "Ayam Goreng": 15000,
    "Burger King": 25000,
    "Kentang Goreng": 10000,
    "Es Teh Manis": 5000,
    "Coca-cola": 12000,
}

# Ngebungkus/wrap semua function menjadi 1, bernama main function() untuk dijadiin neested function
def main():
    # Deklarasi function pemilihan
    def pemilihan():
        print("=================== Daftar Menu ===================")
        for i in menu:
            print(
                i,
                "\t  | Rp.",
                menu[i],
            )
        print("===================================================")
        print("Pembelian diatas Rp100.000,- mendapatkan diskon 15%")
        print("===================================================")
        # Untuk input, harus ketik sesuai dictionaries menu{}, karna python case-sensitive language
        beli = input("Pilih Menu : ")

        # PERHITUNGAN UNTUK PEMBAYARAN
        # Jumlah input cuma bisa 1, untuk nambah input harus memakai null/empty list(array [in Python])
        jumlah = int(input("Jumlah Pesanan : "))
        bayar = jumlah * menu[beli]
        if bayar > 100000:
            diskon = bayar * 15 / 100
            total = bayar - diskon
        else:
            total = bayar
            bayar = jumlah * menu[beli]

        # Print Detail Pembayaran
        print("============== Detail Pembayaran ==================")
        print("Menu yang di pesan       : ", beli)
        print("Jumlah yang dipesan      : ", jumlah)
        print("Total Biaya              : ", bayar)
        print("Total yang harus dibayar : ", total)
        bayar = int(input("Bayar         :  "))
        kembalian = bayar - total
        print("Kembalian        : ", kembalian)
        print("===== Terima Kasih =====")

        # If-else statement jika uang yang di bayar 'pas' atau 'kurang'
        if bayar == total:
            print("Uang anda pas, Terima kasih telah berbelanja")
        elif bayar < total:
            tanya = input(
                "Maaf uang anda tidak cukup, Apakah anda ingin memesan ulang? [y/t]:"
            )
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
