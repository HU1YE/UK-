import unittest

# Fungsi sederhana yang akan diuji
def tambah(a, b):
    return a + b

# Membuat sebuah kelas turunan dari unittest.TestCase
class TestTambah(unittest.TestCase):
    
    # Metode tes harus diawali dengan "test_"
    def test_tambah_angka_positif(self):
        hasil = tambah(3, 4)
        self.assertEqual(hasil, 7)  # Memastikan hasilnya benar

    def test_tambah_angka_negatif(self):
        hasil = tambah(-2, -5)
        self.assertEqual(hasil, -7)  # Memastikan hasilnya benar

    def test_tambah_campuran(self):
        hasil = tambah(2, -3)
        self.assertEqual(hasil, -1)  # Memastikan hasilnya benar

if __name__ == '__main__':
    unittest.main()
