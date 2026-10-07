# LUXE ARCHIVE
# Sistem Manajemen Inventaris Tas Luxury Pre-Owned

## Deskripsi

Program ini merupakan simulasi sederhana sistem manajemen inventaris pada sebuah toko yang menjual tas branded bekas (*luxury pre-owned*). Program dibuat menggunakan konsep Pemrograman Berorientasi Objek (PBO) dengan tiga class utama, yaitu **Tas**, **Pengguna**, dan **Stock**.

Ketiga class tersebut memiliki fungsi berbeda, tetapi dapat saling berinteraksi dalam mengelola data inventaris toko.

| Class | Fungsi |
|---|---|
| Tas | Menyimpan informasi tas seperti nama, merek, kategori, harga, tahun, dan status ketersediaan |
| Pengguna | Menyimpan data pengguna sistem yang mengelola inventaris toko |
| Stock | Menyimpan informasi lokasi penyimpanan setiap tas di gudang |

Program menerapkan konsep dasar OOP meliputi class, object, attribute, method, encapsulation, dan property. Setiap objek Tas merepresentasikan satu barang fisik yang unik, karena barang *pre-owned* tidak ada yang benar-benar identik satu sama lain.

## Struktur Class

### 1. Class Tas

Class Tas digunakan untuk menyimpan dan mengelola data tas yang tersedia di toko.

Atribut kelas yang digunakan adalah `jenisProduk`, `totalTas`, dan `kategoriTersedia`. Untuk setiap objek Tas, terdapat atribut publik `nama`, `merek`, `harga`, `tahun`, dan `kategori`. Status ketersediaan dibuat sebagai atribut privat `__status`, karena perubahannya perlu divalidasi.

Method yang digunakan antara lain:
- `tampilkanData()` — menampilkan seluruh informasi sebuah tas.
- `tambahKategori(kategoriBaru)` — class method untuk menambah pilihan kategori baru yang berlaku untuk semua objek Tas.
- `formatHarga(harga)` — static method untuk memformat angka harga menjadi format rupiah.
- Property `status` digunakan untuk mengakses dan mengubah status dengan validasi, di mana nilainya hanya boleh "Tersedia" atau "Terjual".

### 2. Class Pengguna

Class Pengguna digunakan untuk menyimpan data pengguna yang mengelola sistem inventaris toko.

Atribut kelas pada class ini adalah `namaToko` dan `totalPengguna`. Setiap objek memiliki atribut publik `username` dan `role`. Password disimpan sebagai atribut privat `__password` dan diakses melalui property agar perubahan password dapat divalidasi.

Method yang digunakan antara lain:
- `login(username, password)` — memeriksa kecocokan username dan password.
- Property `password` digunakan untuk mengakses dan mengubah password melalui setter dengan validasi minimal 6 karakter.

### 3. Class Stock

Class Stock digunakan untuk mencatat lokasi penyimpanan setiap tas di gudang. Class ini menggunakan objek Tas, sehingga setiap catatan penyimpanan dapat diketahui tas mana yang dimaksud.

Atribut kelas yang digunakan yaitu `gudangUtama` dan `lokasiTersedia`. Setiap objek memiliki atribut publik `tas` dan atribut privat `__lokasi`.

Method yang digunakan antara lain:
- `tampilkanLokasi()` — menampilkan nama tas beserta lokasi penyimpanannya.
- `validasiStatusTas(status)` — static method untuk memeriksa apakah suatu status termasuk status yang valid.
- Property `lokasi` digunakan untuk mengakses dan mengubah lokasi penyimpanan dengan validasi, di mana lokasi harus termasuk dalam daftar `lokasiTersedia`.

## Panduan Menjalankan Program

1. Unduh file program.
2. Buka file tersebut menggunakan VS Code atau text editor lain yang mendukung Python.
3. Jalankan program melalui terminal dengan perintah `python nama_file.py`.

## Panduan Pengujian

Pengujian program dilakukan pada bagian utama program dan dibagi menjadi beberapa bagian sesuai dengan class yang digunakan.

### 1. Class Tas

Pada bagian ini dibuat empat objek Tas dengan merek dan kategori yang berbeda-beda. Setiap objek kemudian ditampilkan datanya menggunakan instance method `tampilkanData()`, yang sekaligus menunjukkan pemanggilan static method `formatHarga()` untuk memformat harga.

Selanjutnya, class method `tambahKategori()` diuji untuk menambahkan kategori baru ke dalam daftar kategori yang tersedia. Jumlah total objek Tas yang telah dibuat juga ditampilkan melalui atribut kelas `totalTas`.

### 2. Class Pengguna

Pada bagian ini dibuat dua objek Pengguna. Instance method `login()` diuji dengan kombinasi username dan password yang benar maupun salah, untuk menunjukkan bahwa proses autentikasi berjalan sesuai harapan. Jumlah total pengguna yang terdaftar juga ditampilkan melalui atribut kelas `totalPengguna`.

### 3. Class Stock

Pada bagian ini dibuat dua objek Stock yang masing-masing menyimpan lokasi penyimpanan tas yang berbeda. Lokasi setiap tas ditampilkan menggunakan `tampilkanLokasi()`, dan static method `validasiStatusTas()` diuji untuk memeriksa validitas suatu status.

### 4. Pengujian Setter Valid

Setter pada ketiga class diuji dengan data yang valid, yaitu:
- Password pengguna diubah dengan password baru yang memenuhi syarat minimal 6 karakter.
- Status tas diubah dari "Tersedia" menjadi "Terjual".
- Lokasi penyimpanan tas diubah ke lokasi lain yang terdaftar dalam `lokasiTersedia`.

Seluruh perubahan berhasil dilakukan dan ditampilkan nilai barunya.

### 5. Pengujian Setter Tidak Valid

Setter juga diuji dengan data yang tidak memenuhi ketentuan, yaitu:
- Password diisi dengan karakter kurang dari 6.
- Status tas diisi dengan string kosong.
- Lokasi diisi dengan nama lokasi yang tidak terdaftar.

Setiap percobaan tersebut menghasilkan error `ValueError` yang ditangkap menggunakan blok `try-except`, sehingga data lama tetap dipertahankan dan tidak berubah menjadi nilai yang tidak valid.

## Kesimpulan

Program ini menerapkan konsep dasar OOP melalui tiga class, yaitu Tas, Pengguna, dan Stock. Konsep yang diterapkan meliputi class, object, attribute, method, encapsulation, dan property. Program juga menyediakan pengujian terhadap seluruh method dan setter menggunakan data valid maupun tidak valid.

Seluruh pengujian dikatakan berhasil karena hasil output sesuai dengan yang diharapkan.
