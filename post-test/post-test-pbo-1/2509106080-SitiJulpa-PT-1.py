class Tas:
    jenisProduk = "Luxury Pre-Owned"
    totalTas = 0
    kategoriTersedia = ["Tote Bag", "Shoulder Bag", "Clutch", "Crossbody"]

    def __init__(self, nama, merek, harga, tahun, kategori):
        self.nama = nama
        self.merek = merek
        self.harga = harga
        self.tahun = tahun
        self.kategori = kategori
        self.__status = "Tersedia"
        Tas.totalTas += 1

    def tampilkanData(self):
        print("Jenis Produk :", Tas.jenisProduk)
        print("Nama         :", self.nama)
        print("Merek        :", self.merek)
        print("Kategori     :", self.kategori)
        print("Harga        :", Tas.formatHarga(self.harga))
        print("Tahun        :", self.tahun)
        print("Status       :", self.__status)

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, statusBaru):
        if statusBaru != "Tersedia" and statusBaru != "Terjual":
            raise ValueError("Status harus 'Tersedia' atau 'Terjual'.")
        self.__status = statusBaru

    @classmethod
    def tambahKategori(cls, kategoriBaru):
        cls.kategoriTersedia.append(kategoriBaru)

    @staticmethod
    def formatHarga(harga):
        return "Rp" + str(harga)

class Pengguna:
    namaToko = "Luxe Archive"
    totalPengguna = 0

    def __init__(self, username, password, role):
        self.username = username
        self.role = role
        self.__password = password
        Pengguna.totalPengguna += 1

    def login(self, username, password):
        if self.username == username and self.__password == password:
            return True
        return False

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, passwordBaru):
        if len(passwordBaru) < 6:
            raise ValueError("Password minimal 6 karakter.")
        self.__password = passwordBaru


class Stock:
    gudangUtama = "Gudang Pusat"
    lokasiTersedia = ["Rak A", "Rak B", "Rak C"]

    def __init__(self, tas, lokasi):
        self.tas = tas
        self.lokasi = lokasi

    def tampilkanLokasi(self):
        print(self.tas.nama, "- Disimpan di:", self.__lokasi)

    @property
    def lokasi(self):
        return self.__lokasi

    @lokasi.setter
    def lokasi(self, lokasiBaru):
        if lokasiBaru not in Stock.lokasiTersedia:
            raise ValueError("Lokasi tidak dikenali.")
        self.__lokasi = lokasiBaru

    @staticmethod
    def validasiStatusTas(status):
        return status in ["Tersedia", "Terjual"]

# MAIN PROGRAM DISINI BANG

print('''+==============================================+
|                 LUXE ARCHIVE                 |
|       Luxury Pre-Owned Bag Inventory         |
+==============================================+
''')

print("========== DATA TAS ==========\n")

tas1 = Tas("Classic Flap Bag", "Chanel", 52000000, 2021, "Shoulder Bag")
tas2 = Tas("Boy Bag", "Chanel", 44000000, 2020, "Shoulder Bag")
tas3 = Tas("Lady Dior", "Dior", 48000000, 2022, "Tote Bag")
tas4 = Tas("Saddle Bag", "Dior", 40000000, 2021, "Crossbody")

daftarTas = [tas1, tas2, tas3, tas4]

for i in daftarTas:
    i.tampilkanData()
    print()

Tas.tambahKategori("Bucket Bag")

print("Kategori tersedia :", Tas.kategoriTersedia)
print("Total tas fisik   :", Tas.totalTas)


print("\n\n========== DATA PENGGUNA ==========\n")

staf1 = Pengguna("staff01", "staff123", "Staf Gudang")
staf2 = Pengguna("staff02", "staff456", "Staf Gudang")

print("Login staf1    :", staf1.login("staff01", "staff123"))
print("Login staf2    :", staf2.login("staff02", "staff444"))
print("Total pengguna :", Pengguna.totalPengguna)


print("\n========== DATA PENYIMPANAN ==========\n")

stok1 = Stock(tas1, "Rak A")
stok2 = Stock(tas2, "Rak B")

stok1.tampilkanLokasi()
stok2.tampilkanLokasi()

print(
    "Validasi status 'Tersedia' :",
    Stock.validasiStatusTas("Tersedia")
)

print("\n========== PENGUJIAN SETTER VALID ==========\n")

staf1.password = "passwordbaru"
print("Password staf1 berhasil diubah.")

tas1.status = "Terjual"
print("Status tas1 setelah diubah   :", tas1.status)

stok1.lokasi = "Rak C"
print("Lokasi tas1 setelah dipindah :", stok1.lokasi)

print("\n========== PENGUJIAN SETTER TIDAK VALID ==========\n")

try:
    staf1.password = "123"
except ValueError as e:
    print("Password gagal diubah :", e)

try:
    tas1.status = ""
except ValueError as e:
    print("Status gagal diubah   :", e)

try:
    stok1.lokasi = "Rak Z"
except ValueError as e:
    print("Lokasi gagal diubah   :", e)