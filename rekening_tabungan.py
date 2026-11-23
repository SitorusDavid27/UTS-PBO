
# Subclass RekeningTabungan
from rekening import Rekening

class RekeningTabungan(Rekening):
    def __init__(self, nomor, nama, saldo, bunga):
        super().__init__(nomor, nama, saldo)

        self.__bunga = bunga
        self.__jenis = "Tabungan"
        self.__minimal_saldo = 50000

    # Getter
    def get_bunga(self):
        return self.__bunga

    def get_jenis(self):
        return self.__jenis

    def get_minimal_saldo(self):
        return self.__minimal_saldo

    # Menghitung bunga
    def hitung_bunga(self):
        return self.get_saldo() * self.__bunga / 100

    # Menampilkan informasi tabungan
    def tampilkan_tabungan(self):
        self.tampilkan_info()
        print("Jenis Rekening :", self.__jenis)
        print("Bunga          :", self.__bunga, "%")
        print("Minimal Saldo  : Rp", self.__minimal_saldo)
