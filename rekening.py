
# Superclass Rekening
class Rekening:
    def __init__(self, nomor, nama, saldo):
        # Atribut private
        self.__nomor = nomor
        self.__nama = nama
        self.__saldo = saldo
        self.__status = "Aktif"

    # Getter untuk mengambil data
    def get_nomor(self):
        return self.__nomor

    def get_nama(self):
        return self.__nama

    def get_saldo(self):
        return self.__saldo

    def get_status(self):
        return self.__status

    # Mengubah nama pemilik
    def ubah_nama(self, nama_baru):
        self.__nama = nama_baru

    # Mengubah status rekening
    def ubah_status(self, status):
        self.__status = status

    # Menyetorkan uang
    def setor(self, jumlah):
        if self.__status != "Aktif" or jumlah <= 0:
            return False

        self.__saldo += jumlah
        return True

    # Menarik uang
    def tarik(self, jumlah):
        if self.__status != "Aktif" or jumlah <= 0:
            return False

        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
            return True

        return False

    # Menampilkan informasi rekening
    def tampilkan_info(self):
        print("Nomor Rekening :", self.__nomor)
        print("Nama Pemilik   :", self.__nama)
        print("Saldo          : Rp", self.__saldo)
        print("Status         :", self.__status)
