# Laporan Posttest 2 - Pemrograman Berorientasi Objek

## Identitas

- Nama  : Siti Julpa
- NIM   : 2509106080
- Kelas : B2'25

---

## LUXE ARCHIVE

**Sistem Manajemen Inventaris Tas Luxury Pre-Owned**

---

## Login

Program dijalankan lewat terminal. Setelah muncul portal login, masukkan salah satu akun staf di bawah ini.

| No | Role | Username | Password |
|---|---|---|---|
| 1 | Staf Gudang | `staff01` | `staff123` |
| 2 | Staf Gudang | `staff02` | `staff456` |

Kalau username dan password cocok, program menampilkan pesan berhasil lalu masuk ke menu utama inventaris.

---

## Gambaran Sistem

Luxe Archive adalah aplikasi CLI untuk mengelola stok tas mewah bekas. Hanya staf yang sudah login yang bisa mengakses menu. Fitur CRUD-nya:

1. **Create**: menambah tas baru, baik tipe Reguler maupun Limited Edition, sekaligus menentukan lokasi penyimpanannya di gudang.
2. **Read**: menampilkan seluruh stok tas, lengkap dengan data sertifikat keaslian dan nama staf yang melakukan inspeksi.
3. **Update**: mengubah harga, status (Tersedia, Terjual, Booking), dan lokasi rak.
4. **Delete**: menghapus tas dari daftar stok saat sudah terjual atau tidak lagi dijual, lalu menyesuaikan total unit.

---

## Penerapan Materi Posttest 2

### 1. Relasi UML

#### Asosiasi

Asosiasi adalah hubungan di mana satu objek hanya berinteraksi dengan objek lain, tanpa menyimpannya sebagai atribut. Di program ini, `Pengguna` (staf) menerima objek `Stock` lewat parameter method `inspeksiStok(stock)`, lalu memakainya untuk mencetak lokasi tas yang diperiksa. Objek `Stock` hanya dipakai selama method berjalan, jadi `Pengguna` tidak memilikinya.

```python
class Pengguna:

    def inspeksiStok(self, stock):
        print(f"│ Diinspeksi oleh : Staf {self.username}")
        print(f"│ Lokasi Dicek    : {stock.lokasi}")
```

#### Agregasi

Agregasi adalah hubungan "memiliki" yang longgar. Objek `Tas` dibuat di luar kelas `Stock`, lalu dimasukkan lewat konstruktor dan disimpan di `self.tas`. Kalau objek `Stock` dihapus, objek `Tas` tetap ada karena dibuat dan hidup secara terpisah.

```python
class Stock:
    def __init__(self, tas, lokasi):

        self.tas = tas
        self.__lokasi = lokasi
```

#### Komposisi

Komposisi adalah hubungan "memiliki" yang kuat / "terdiri dari". Objek `SertifikatKeaslian` dibuat langsung di dalam konstruktor `Tas`, dan tidak ada tanpa tas yang bersangkutan. Kalau objek `Tas` dihapus, sertifikatnya ikut hilang.

```python
class Tas:
    def __init__(self, nama, merek, harga, tahun, kategori, kodeSertifikat):
        self._nama = nama
        self._merek = merek
        self._harga = harga
        self.tahun = tahun
        self.kategori = kategori
        self.__status = "Tersedia"

        self.sertifikat = SertifikatKeaslian(kodeSertifikat)

        Tas.totalTas += 1
```

---

### 2. Inheritance

#### Superclass dan Subclass

Kelas `Tas` menjadi superclass. `TasPreOwnedReguler` dan `TasLimitedEdition` menjadi dua subclass yang mewarisi atribut dan method dari `Tas`.

```python
class Tas:

class TasPreOwnedReguler(Tas):

class TasLimitedEdition(Tas):
```

#### Penggunaan `super()`

Setiap subclass memanggil konstruktor superclass dengan `super().__init__(...)`, sehingga atribut dasar tas tidak perlu ditulis ulang.

```python
class TasPreOwnedReguler(Tas):
    def __init__(self, nama, merek, harga, tahun, kategori, kodeSertifikat, kondisi):
        super().__init__(nama, merek, harga, tahun, kategori, kodeSertifikat)
        self.kondisi = kondisi
```

#### Atribut Tambahan pada Subclass

Tiap subclass punya atribut yang tidak dimiliki superclass maupun subclass lainnya:

- `TasPreOwnedReguler`: `kondisi` (kondisi fisik tas)
- `TasLimitedEdition`: `nomorSeri` dan `edisiKhusus`

```python
class TasPreOwnedReguler(Tas):
    def __init__(self, nama, merek, harga, tahun, kategori, kodeSertifikat, kondisi):
        super().__init__(nama, merek, harga, tahun, kategori, kodeSertifikat)
        self.kondisi = kondisi

class TasLimitedEdition(Tas):
    def __init__(self, nama, merek, harga, tahun, kategori, kodeSertifikat, nomorSeri, edisiKhusus):
        super().__init__(nama, merek, harga, tahun, kategori, kodeSertifikat)
        self.nomorSeri = nomorSeri
        self.edisiKhusus = edisiKhusus
```

#### Method Overriding

Method `tampilkanData()` milik `Tas` di-override di kedua subclass. Masing-masing memanggil versi superclass lebih dulu lewat `super().tampilkanData()`, lalu menambahkan baris untuk atribut uniknya dan satu baris ringkasan yang memakai atribut protected dari superclass.

```python
class TasPreOwnedReguler(Tas):
    def tampilkanData(self):
        super().tampilkanData()
        print(f"│ Kondisi Fisik   : {self.kondisi}")
        print(f"│ Ringkasan       : {self._merek} {self._nama} ({self.kondisi})")

class TasLimitedEdition(Tas):
    def tampilkanData(self):
        super().tampilkanData()
        print(f"│ Edisi Khusus    : {self.edisiKhusus}")
        print(f"│ Nomor Seri      : {self.nomorSeri}")
        print(f"│ Ringkasan       : {self._merek} {self._nama} No. {self.nomorSeri}")
```

#### Tingkat Akses (Protected dan Private)

**Protected** (awalan `_`) dipakai untuk `_nama`, `_merek`, dan `_harga` di superclass `Tas`, karena datanya perlu diakses langsung oleh subclass. Contohnya, `_merek` dan `_nama` dipakai langsung di method `tampilkanData()` milik kedua subclass (lihat bagian Method Overriding di atas).

```python
class Tas:
    def __init__(self, nama, merek, harga, tahun, kategori, kodeSertifikat):
        self._nama = nama
        self._merek = merek
        self._harga = harga
```

**Private** (awalan `__`) dipakai untuk data yang hanya boleh diakses dari dalam kelasnya sendiri: `__status` di `Tas`, `__password` di `Pengguna`, dan `__lokasi` di `Stock`.

```python
class Tas:
    def __init__(self, nama, merek, harga, tahun, kategori, kodeSertifikat):
        self.__status = "Tersedia"

class Pengguna:
    def __init__(self, username, password, role="Staf Gudang"):
        self.__password = password

class Stock:
    def __init__(self, tas, lokasi):
        self.__lokasi = lokasi
```

---

## Kesimpulan

Pada posttest ini, sistem Luxe Archive dikembangkan dengan menerapkan relasi antar kelas dan pewarisan. Dari sisi relasi UML, asosiasi dipakai pada hubungan `Pengguna` dengan `Stock`, agregasi pada hubungan `Stock` dengan `Tas`, dan komposisi pada hubungan `Tas` dengan `SertifikatKeaslian`. Ketiganya dibedakan dari seberapa erat objek-objek tersebut saling terikat: pada asosiasi objek hanya dipakai sementara, pada agregasi objek disimpan tetapi tetap hidup sendiri, dan pada komposisi objek bagian ikut hilang bersama induknya.

Dari sisi inheritance, kelas `Tas` menjadi superclass bagi `TasPreOwnedReguler` dan `TasLimitedEdition`. Kedua subclass memakai `super().__init__(...)` untuk mewarisi atribut dasar, menambahkan atribut uniknya sendiri, dan meng-override `tampilkanData()` agar data khususnya ikut tampil. Dengan cara ini kode tidak perlu ditulis berulang dan jenis tas baru lebih mudah ditambahkan nantinya.

Pemakaian atribut protected (`_nama`, `_merek`, `_harga`) dan private (`__status`, `__password`, `__lokasi`) juga membantu menjaga data. Atribut protected bisa dipakai langsung oleh subclass, sedangkan data sensitif seperti password dan status hanya bisa diubah lewat kelasnya sendiri.
