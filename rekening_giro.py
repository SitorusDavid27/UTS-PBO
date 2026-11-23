
# Subclass RekeningGiro
from rekening import Rekening

class RekeningGiro(Rekening):
    def __init__(self, nomor, nama, saldo, limit):
        super().__init__(nomor, nama, saldo)

        self.__limit = limit
        self.__jenis = "Giro"
        self.__biaya_admin = 10000

    # Getter
    def get_limit(self):
        return self.__limit

    def get_jenis(self):
        return self.__jenis

    def get_biaya_admin(self):
        return self.__biaya_admin

    # Mengecek limit penarikan
    def cek_limit(self):
        return self.__limit

    # Menampilkan informasi giro
    def tampilkan_giro(self):
        self.tampilkan_info()
        print("Jenis Rekening :", self.__jenis)
        print("Limit Tarik    : Rp", self.__limit)
        print("Biaya Admin    : Rp", self.__biaya_admin)
