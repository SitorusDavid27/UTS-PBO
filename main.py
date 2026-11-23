
# Import semua class
from rekening_tabungan import RekeningTabungan
from rekening_giro import RekeningGiro
from transaksi import Transaksi

# Menyimpan data
daftar_rekening = []
daftar_transaksi = []


# Mencari rekening
def cari_rekening(nomor):
    for rekening in daftar_rekening:
        if rekening.get_nomor() == nomor:
            return rekening
    return None


# Tambah rekening
def tambah_rekening():
    print("\n=== TAMBAH REKENING ===")

    nomor = input("Nomor rekening: ")

    if cari_rekening(nomor):
        print("Nomor rekening sudah digunakan!")
        return

    nama = input("Nama pemilik: ")

    try:
        saldo = int(input("Saldo awal: Rp "))

        if saldo < 0:
            print("Saldo tidak boleh negatif!")
            return

        print("\n1. Rekening Tabungan")
        print("2. Rekening Giro")

        pilihan = input("Pilih jenis rekening: ")

        if pilihan == "1":
            rekening = RekeningTabungan(
                nomor, nama, saldo, 2
            )

        elif pilihan == "2":
            rekening = RekeningGiro(
                nomor, nama, saldo, 5000000
            )

        else:
            print("Pilihan tidak tersedia!")
            return

        daftar_rekening.append(rekening)
        print("Rekening berhasil ditambahkan!")

    except ValueError:
        print("Saldo harus berupa angka!")


# Tampilkan rekening
def tampilkan_rekening():
    print("\n=== DAFTAR REKENING ===")

    if not daftar_rekening:
        print("Belum ada rekening.")
        return

    for rekening in daftar_rekening:
        rekening.tampilkan_info()
        print("------------------------")


# Cari rekening
def cari_data():
    nomor = input("\nMasukkan nomor rekening: ")
    rekening = cari_rekening(nomor)

    if rekening:
        rekening.tampilkan_info()
    else:
        print("Rekening tidak ditemukan!")


# Ubah data rekening
def ubah_data():
    nomor = input("\nMasukkan nomor rekening: ")
    rekening = cari_rekening(nomor)

    if rekening:
        nama = input("Masukkan nama baru: ")
        rekening.ubah_nama(nama)
        print("Nama berhasil diubah!")
    else:
        print("Rekening tidak ditemukan!")


# Cek status rekening
def cek_status():
    nomor = input("\nMasukkan nomor rekening: ")
    rekening = cari_rekening(nomor)

    if rekening:
        rekening.tampilkan_info()

        print("\n1. Aktifkan")
        print("2. Nonaktifkan")
        pilihan = input("Pilih tindakan (0 untuk batal): ")

        if pilihan == "1":
            rekening.ubah_status("Aktif")
            print("Rekening berhasil diaktifkan!")

        elif pilihan == "2":
            rekening.ubah_status("Nonaktif")
            print("Rekening berhasil dinonaktifkan!")

        elif pilihan == "0":
            print("Tidak ada perubahan.")

        else:
            print("Pilihan tidak valid!")

    else:
        print("Rekening tidak ditemukan!")


# Transaksi setor dan tarik
def menu_transaksi():
    nomor = input("\nNomor rekening: ")
    rekening = cari_rekening(nomor)

    if rekening is None:
        print("Rekening tidak ditemukan!")
        return

    print("\n1. Setor Tunai")
    print("2. Tarik Tunai")

    pilihan = input("Pilih transaksi: ")

    try:
        jumlah = int(input("Jumlah uang: Rp "))

        if pilihan == "1":
            jenis = "Setor"
        elif pilihan == "2":
            jenis = "Tarik"
        else:
            print("Pilihan tidak tersedia!")
            return

        id_transaksi = len(daftar_transaksi) + 1

        transaksi = Transaksi(
            id_transaksi, jenis, jumlah, rekening
        )

        if transaksi.proses_transaksi():
            daftar_transaksi.append(transaksi)
            print("Transaksi berhasil!")
            transaksi.tampilkan_transaksi()
            print("Saldo sekarang: Rp", rekening.get_saldo())

        else:
            print("Transaksi gagal! Periksa saldo atau status.")

    except ValueError:
        print("Jumlah harus berupa angka!")


# Riwayat transaksi
def tampilkan_transaksi():
    print("\n=== RIWAYAT TRANSAKSI ===")

    if not daftar_transaksi:
        print("Belum ada transaksi.")
        return

    for transaksi in daftar_transaksi:
        transaksi.tampilkan_transaksi()
        print("------------------------")


# Menu utama
while True:
    print("\n================================")
    print("       APLIKASI REKENING BANK")
    print("================================")
    print("1. Tambah Rekening")
    print("2. Tampilkan Rekening")
    print("3. Cari Rekening")
    print("4. Ubah Data Rekening")
    print("5. Cek Status Rekening")
    print("6. Transaksi Setor/Tarik")
    print("7. Riwayat Transaksi")
    print("8. Keluar")
    print("================================")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_rekening()
    elif pilihan == "2":
        tampilkan_rekening()
    elif pilihan == "3":
        cari_data()
    elif pilihan == "4":
        ubah_data()
    elif pilihan == "5":
        cek_status()
    elif pilihan == "6":
        menu_transaksi()
    elif pilihan == "7":
        tampilkan_transaksi()
    elif pilihan == "8":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak tersedia!")
