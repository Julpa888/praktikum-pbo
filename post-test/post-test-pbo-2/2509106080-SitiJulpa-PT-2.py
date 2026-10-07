class SertifikatKeaslian:
    def __init__(self, kodeSertifikat, penerbit="AuthenticGuarantor"):
        self.kodeSertifikat = kodeSertifikat
        self.penerbit = penerbit

    def tampilkanSertifikat(self):
        print(f"│ Kode Sertifikat : {self.kodeSertifikat} (Verified by {self.penerbit})")

class Tas:
    jenisProduk = "Luxury Pre-Owned Bag"
    totalTas = 0
    kategoriTersedia = ["Tote Bag", "Shoulder Bag", "Clutch", "Crossbody"]

    def __init__(self, nama, merek, harga, tahun, kategori, kodeSertifikat):
        self._nama = nama
        self._merek = merek
        self._harga = harga
        self.tahun = tahun
        self.kategori = kategori
        self.__status = "Tersedia"
        self.sertifikat = SertifikatKeaslian(kodeSertifikat)
        
        Tas.totalTas += 1

    def tampilkanData(self):
        print(f"│ Jenis Produk    : {self.jenisProduk}")
        print(f"│ Nama Tas        : {self._nama}")
        print(f"│ Merek           : {self._merek}")
        print(f"│ Kategori        : {self.kategori}")
        print(f"│ Harga           : {Tas.formatHarga(self._harga)}")
        print(f"│ Tahun Rilis     : {self.tahun}")
        print(f"│ Status Stok     : {self.__status}")
        self.sertifikat.tampilkanSertifikat()

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, statusBaru):
        if statusBaru not in ["Tersedia", "Terjual", "Booking"]:
            raise ValueError("Status harus 'Tersedia', 'Terjual', atau 'Booking'.")
        self.__status = statusBaru

    @classmethod
    def tambahKategori(cls, kategoriBaru):
        cls.kategoriTersedia.append(kategoriBaru)

    @staticmethod
    def formatHarga(harga):
        return f"Rp{harga:,.0f}".replace(",", ".")


class TasPreOwnedReguler(Tas):
    jenisProduk = "Luxury Pre-Owned (Reguler)"

    def __init__(self, nama, merek, harga, tahun, kategori, kodeSertifikat, kondisi):
        super().__init__(nama, merek, harga, tahun, kategori, kodeSertifikat)
        self.kondisi = kondisi

    def tampilkanData(self):
        super().tampilkanData()
        print(f"│ Kondisi Fisik   : {self.kondisi}")


class TasLimitedEdition(Tas):
    jenisProduk = "Luxury Pre-Owned (Limited Edition)"

    def __init__(self, nama, merek, harga, tahun, kategori, kodeSertifikat, nomorSeri, edisiKhusus):
        super().__init__(nama, merek, harga, tahun, kategori, kodeSertifikat)
        self.nomorSeri = nomorSeri     
        self.edisiKhusus = edisiKhusus  

    def tampilkanData(self):
        super().tampilkanData()
        print(f"│ Edisi Khusus    : {self.edisiKhusus}")
        print(f"│ Nomor Seri      : {self.nomorSeri}")

class Pengguna:
    namaToko = "Luxe Archive"
    totalPengguna = 0

    def __init__(self, username, password, role="Staf Gudang"):
        self.username = username
        self.role = role
        self.__password = password 
        Pengguna.totalPengguna += 1

    def login(self, username, password):
        return self.username == username and self.__password == password

    def inspeksiStok(self, stock):
        print(f"│ Diinspeksi oleh : Staf {self.username}")


class Stock:
    gudangUtama = "Gudang Pusat Luxe Archive"
    lokasiTersedia = ["Rak A1", "Rak B2", "Brankas Khusus"]

    def __init__(self, tas, lokasi):
        self.tas = tas
        self.__lokasi = lokasi

    @property
    def lokasi(self):
        return self.__lokasi

    @lokasi.setter
    def lokasi(self, lokasiBaru):
        if lokasiBaru not in Stock.lokasiTersedia:
            raise ValueError(f"Lokasi '{lokasiBaru}' tidak valid!")
        self.__lokasi = lokasiBaru


class SistemInventaris:
    def __init__(self):
        self.daftar_staf = [
            Pengguna("staff01", "staff123", "Staf Gudang"),
            Pengguna("staff02", "staff456", "Staf Gudang")
        ]
        
        tas1 = TasPreOwnedReguler("Classic Flap Bag", "Chanel", 52000000, 2021, "Shoulder Bag", "CERT-CHN-001", "Like New (9.5/10)")
        tas2 = TasLimitedEdition("Lady Dior Art x KAWS", "Dior", 75000000, 2023, "Tote Bag", "CERT-DIR-002", "LE-05/10", "Artist Collaboration")
        
        self.daftar_stok = [
            Stock(tas1, "Rak A1"),
            Stock(tas2, "Brankas Khusus")
        ]
        self.staf_aktif = None

    def login_system(self):
        print("✦ ────────────────────────────────────────── ✦")
        print("       LUXE ARCHIVE — PORTAL LOGIN (⁠✧⁠ω⁠✧⁠)    ")
        print("✦ ────────────────────────────────────────── ✦")
        username = input("Username : ")
        password = input("Password : ")

        for staf in self.daftar_staf:
            if staf.login(username, password):
                self.staf_aktif = staf
                print(f"\nLogin Berhasil! Selamat datang, {staf.username} ⸜(⁠｡⁠･⁠ω⁠･⁠｡⁠)⸝\n")
                return True
        
        print("\nUsername atau Password salah! (T_T)\n")
        return False

    def tambah_tas(self):
        print("\n✧ ─── TAMBAH KOLEKSI BARU (⁠๑⁠•̀⁠ㅂ⁠•́⁠)⁠و ─── ✧")
        print("Jenis Tas:")
        print("1. Tas Pre-Owned Reguler")
        print("2. Tas Limited Edition")
        pilihan = input("Pilihan (1/2): ")

        if pilihan not in ["1", "2"]:
            print("Pilihan tidak valid!")
            return

        nama = input("Nama Tas        : ")
        merek = input("Merek           : ")
        harga = float(input("Harga (Rp)      : "))
        tahun = int(input("Tahun Rilis     : "))
        kategori = input(f"Kategori {Tas.kategoriTersedia}: ")
        kode_cert = input("Kode Sertifikat : ")
        lokasi = input(f"Lokasi {Stock.lokasiTersedia}: ")

        if lokasi not in Stock.lokasiTersedia:
            print("Lokasi tidak valid!")
            return

        if pilihan == "1":
            kondisi = input("Kondisi Fisik   : ")
            obj_tas = TasPreOwnedReguler(nama, merek, harga, tahun, kategori, kode_cert, kondisi)
        else:
            no_seri = input("Nomor Seri      : ")
            edisi = input("Edisi Khusus    : ")
            obj_tas = TasLimitedEdition(nama, merek, harga, tahun, kategori, kode_cert, no_seri, edisi)

        self.daftar_stok.append(Stock(obj_tas, lokasi))
        print(f"\nTas '{nama}' berhasil ditambahkan ke inventaris! (⁠⁠✿⁠⌒⁠∇⁠⌒⁠)")

    def tampilkan_stok(self):
        print("\n✦ ─────────────────────────────────────────── ✦")
        print("          KATALOG KOLEKSI TAS (o^^o)        ")
        print("✦ ─────────────────────────────────────────── ✦")
        if not self.daftar_stok:
            print("Inventaris masih kosong.")
            return

        for idx, stok in enumerate(self.daftar_stok, 1):
            print(f"┌─ [ KOLEKSI #{idx} ] ───────────────────────────")
            stok.tas.tampilkanData()
            print(f"│ Lokasi Gudang   : {stok.lokasi}")
            self.staf_aktif.inspeksiStok(stok)
            print("└────────────────────────────────────────────\n")
            
        print(f"Total Tas Tersedia: {Tas.totalTas} Unit")

    def ubah_tas(self):
        self.tampilkan_stok()
        if not self.daftar_stok:
            return

        print("\n✧ ─── PERBARUI DETAIL TAS (⁠•̀⁠ᴗ⁠•́⁠)⁠و ─── ✧")
        try:
            idx = int(input("Nomor Koleksi yang Ingin Diubah: ")) - 1
            if idx < 0 or idx >= len(self.daftar_stok):
                print("Nomor koleksi tidak ditemukan!")
                return
        except ValueError:
            print("Masukkan angka yang valid!")
            return

        stok_terpilih = self.daftar_stok[idx]
        tas = stok_terpilih.tas

        print("\nOpsi Perubahan:")
        print("1. Ubah Harga")
        print("2. Ubah Status (Tersedia/Terjual/Booking)")
        print("3. Pindah Lokasi Gudang")
        pilihan = input("Pilihan (1-3): ")

        try:
            if pilihan == "1":
                tas._harga = float(input("Harga Baru (Rp): "))
                print("Harga berhasil diperbarui!")
            elif pilihan == "2":
                tas.status = input("Status Baru (Tersedia/Terjual/Booking): ")
                print("Status berhasil diperbarui!")
            elif pilihan == "3":
                stok_terpilih.lokasi = input(f"Lokasi Baru {Stock.lokasiTersedia}: ")
                print("Lokasi penyimpanan berhasil dipindahkan!")
            else:
                print("Pilihan opsi tidak valid!")
        except ValueError as err:
            print(f"Gagal memperbarui : {err}")

    def hapus_tas(self):
        self.tampilkan_stok()
        if not self.daftar_stok:
            return

        print("\n✧ ─── HAPUS / TAS TERJUAL (⁠⊃⁠｡⁠•́⁠‿⁠•̀⁠｡⁠)⁠⊃ ─── ✧")
        try:
            idx = int(input("Nomor Koleksi yang Dihapus/Terjual: ")) - 1
            if idx < 0 or idx >= len(self.daftar_stok):
                print("Nomor koleksi tidak ditemukan!")
                return
        except ValueError:
            print("Masukkan angka yang valid!")
            return

        stok_dihapus = self.daftar_stok.pop(idx)
        Tas.totalTas -= 1
        print(f"\nTas '{stok_dihapus.tas._nama}' berhasil dikeluarkan dari stok!")

    def menu_utama(self):
        while True:
            print("\n✦ ────────────────────────────────────────── ✦")
            print(f"   LUXE ARCHIVE — STAF: {self.staf_aktif.username} (⁠˶⁠ᵔ⁠ ⁠ᵕ⁠ ⁠ᵔ⁠˶⁠)")
            print("✦ ────────────────────────────────────────── ✦")
            print("1. Lihat Koleksi Tas")
            print("2. Tambah Koleksi Baru")
            print("3. Perbarui Detail Tas")
            print("4. Hapus / Tas Terjual")
            print("5. Logout & Keluar")
            pilihan = input("Pilih Menu (1-5): ")

            if pilihan == "1":
                self.tampilkan_stok()
            elif pilihan == "2":
                self.tambah_tas()
            elif pilihan == "3":
                self.ubah_tas()
            elif pilihan == "4":
                self.hapus_tas()
            elif pilihan == "5":
                print("\nBerhasil Logout. Sampai jumpa lagi! (⁠⁠✿⁠´⁠ヮ⁠`)\n")
                break
            else:
                print("Pilihan tidak valid!")

sistem = SistemInventaris()
if sistem.login_system():
    sistem.menu_utama()