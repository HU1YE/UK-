try:
    num = int(input("Masukkan angka: "))

    result = 10 / num

    print("Hasil pembagian: ", result)

except ZeroDivisionError:
    print("Error: Anda mencoba membagi oleh nol")
except ValueError:
    print("Error: Masukan harus berupa angka")
except Exception as e:
    print("Error umum:", str(e))

else:
    print("Tidak ada error yang terjadi.")  

finally:
    print("Eksekusi program selesai.")  
