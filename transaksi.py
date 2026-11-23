
# Class Transaksi
class Transaksi:
    def __init__(self, id_transaksi, jenis, jumlah, rekening):
        self.__id_transaksi = id_transaksi
        self.__jenis = jenis
        self.__jumlah = jumlah
        self.__rekening = rekening

    # Getter
    def get_id(self):
        return self.__id_transaksi

    def get_jenis(self):
        return self.__jenis

    def get_jumlah(self):
        return self.__jumlah

    # Memproses transaksi
    def proses_transaksi(self):
        if self.__jenis == "Setor":
            return self.__rekening.setor(self.__jumlah)

        elif self.__jenis == "Tarik":
            return self.__rekening.tarik(self.__jumlah)

        return False

    # Menampilkan transaksi
    def tampilkan_transaksi(self):
        print("ID Transaksi :", self.__id_transaksi)
        print("Jenis        :", self.__jenis)
        print("Jumlah       : Rp", self.__jumlah)
        print("Rekening     :", self.__rekening.get_nomor())
