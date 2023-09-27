#Contoh Function
def penjumlahan(a, b, /):
    return a + b

print(penjumlahan(66, 50))




#Menginput panjang dan lebar persegi panjang
panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))

#Menghitung luas persegi panjang
luas = panjang * lebar

#Menampilkan Output
print("Luas persegi panjang adalah:", luas)
