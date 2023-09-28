#IF - Elif
nilai = 85

if nilai >= 90:
    kategori = "A"
elif nilai >= 80:
    kategori = "B"
elif nilai >= 70:
    kategori = "C"
elif nilai >= 60:
    kategori = "D"
else:
    kategori = "E"

print("Nilai Anda:", nilai)
print("Kategori:", kategori)

#NestedIF
nilai = 85
if nilai == 90:
    print("Nilai anda adalah 90")
    if nilai > 90:
        print("A. Lulus")
    else:
        print("Nilai anda kurang dari 90")
else:
    print("Coba Lagi")


#Shorthand If Else
nilai = 85

hasil = "Lulus" if nilai >= 90 else "Tidak Lulus"
print(hasil)

#IF Multiconditional
nilai = 85

if nilai >= 60 and nilai <= 80:
    print("Nilai Anda lulus dan berada dalam rentang Average")
elif nilai > 80:
    print("Nilai Anda lulus dan berada dalam rentang B")
else:
    print("Anda belum lulus atau nilai Anda berada di bawah 60 dengan rentang E")


#IF Pass
nilai = 85  

passing_score = 76  
if nilai >= passing_score:
    print("Sealmat anda lulus!")
else:
    print("Mohon maaf anda belum lulus.")


#Slicing
my_list = [1, 2, 3, 4, 5]
hasil = my_list[1:3]
print(hasil)  

#Indexing
my_list = [1, 2, 3, 4, 5]
hasil = my_list[1]
print(hasil)  