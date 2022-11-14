menu = {
    "Ayam Goreng": 15000,
    "Burger King": 25000,
    "Kentang Goreng": 10000,
    "Es Teh Manis": 5000,
    "Coca-cola": 12000,
}
print("========================= Daftar Menu =========================")
for i in menu:
    print("Daftar Menu: ",i,"\t Harga : ",menu[i])
print("Pembelian diatas Rp100.000,- mendapatkan diskon 15%")
print("===================================================")
beli = input("Pilih Menu : ")
jumlah = int(input("Jumlah Pesanan : "))
bayar = jumlah * menu[beli]

if bayar > 100000:
    diskon = bayar*15/100
    total = bayar - diskon
else:
    total = bayar
    
print("========================= Detail Pembayaran =========================")
print ("Menu yang di pesan       : ",beli)
print ("Jumlah yang dipesan      : ",jumlah)
print ("Total Biaya              : ",bayar)
print ("Total yang harus dibayar : ",total)
