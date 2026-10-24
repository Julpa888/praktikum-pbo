# LUXE ARCHIVE
## Sistem Manajemen Inventaris Tas Luxury Pre-Owned

Luxe Archive adalah program berbasis Python untuk mengelola inventaris tas mewah pre-owned. Program ini menggunakan konsep Pemrograman Berorientasi Objek (PBO), meliputi relasi antarkelas, inheritance, abstraksi, polimorfisme, dan operator overloading.

## Identitas

- **Nama:** Siti Julpa
- **NIM:** 2509106080
- **Kelas:** B2'25

## Fitur Program

1. Login staf gudang.
2. Menampilkan koleksi tas beserta informasi produk dan sertifikat keaslian.
3. Menambahkan koleksi tas reguler atau limited edition.
4. Memperbarui harga, status, dan lokasi penyimpanan tas.
5. Menghapus koleksi tas dari inventaris.

## Class Diagram

Gambar berikut menunjukkan hubungan antarkelas yang digunakan dalam program Luxe Archive.

![Class Diagram UML Luxe Archive](post-test-pbo-3/class_diagram.png)

## Penjelasan Relasi Antar Kelas

### 1. Asosiasi

Asosiasi diterapkan antara kelas `Pengguna` dan `Stock` melalui method `inspeksiStok(stock)`. Objek `Stock` diterima sebagai parameter dan digunakan ketika staf melakukan inspeksi, tanpa disimpan sebagai atribut permanen di dalam objek `Pengguna`.

### 2. Agregasi

Agregasi diterapkan antara kelas `Stock` dan `Tas`. Objek `Tas` dibuat terlebih dahulu di luar kelas `Stock`, kemudian diberikan melalui konstruktor dan disimpan pada atribut `self.tas`. Hubungan ini termasuk agregasi karena objek tas dibuat secara mandiri dan tidak harus dibuat bersamaan dengan objek `Stock`.

### 3. Komposisi

Komposisi diterapkan antara kelas `Tas` dan `SertifikatKeaslian`. Objek `SertifikatKeaslian` dibuat langsung di dalam konstruktor `Tas` dan disimpan pada atribut `self.sertifikat`. Hubungan ini menggambarkan bahwa sertifikat menjadi bagian dari tas yang bersangkutan.

## Penerapan Inheritance

Kelas `Tas` menjadi superclass bagi dua subclass, yaitu `TasPreOwnedReguler` dan `TasLimitedEdition`.

Kedua subclass menggunakan `super().__init__(...)` untuk memanggil konstruktor superclass sehingga atribut umum tidak perlu ditulis ulang.

Atribut tambahan pada masing-masing subclass adalah:

- `TasPreOwnedReguler`: atribut `kondisi`.
- `TasLimitedEdition`: atribut `nomorSeri` dan `edisiKhusus`.

Program juga menggunakan atribut protected seperti `_nama`, `_merek`, dan `_harga`, serta atribut private seperti `__status`, `__password`, dan `__lokasi`.

## Penerapan Abstraksi

Abstraksi diterapkan melalui kelas abstrak `Tas` yang mewarisi `ABC` dari modul `abc`.

Kelas `Tas` memiliki dua abstract method:

- `tampilkanDetailKhusus()`
- `deskripsiKoleksi()`

Kedua method tersebut wajib diimplementasikan oleh subclass. Selain itu, kelas `Tas` memiliki method konkret `tampilkanData()` yang digunakan bersama oleh subclass untuk menampilkan informasi umum tas.

### Bukti Abstract Class Tidak Dapat Diinstansiasi

Fungsi `bukti_abstraksi()` mencoba membuat objek secara langsung dari kelas abstrak `Tas`. Python menolak pembuatan objek tersebut dan menghasilkan `TypeError` karena abstract method belum diimplementasikan pada kelas `Tas`.

Bukti ini ditampilkan menggunakan `try-except TypeError` agar error dapat ditangkap dan hasil pengujiannya ditampilkan tanpa menghentikan program.

<!-- Masukkan screenshot terminal yang menunjukkan bukti TypeError di sini. -->

![Bukti abstraksi](post-test-pbo-3/output_abstraksi.png)

## Penerapan Polimorfisme

### 1. Polimorfisme Melalui Pewarisan

Polimorfisme melalui pewarisan diterapkan dengan meng-override method `tampilkanData()` pada kelas `TasPreOwnedReguler` dan `TasLimitedEdition`.

Kedua subclass memiliki method dengan nama yang sama, tetapi menghasilkan tampilan berbeda sesuai jenis tas. Method tersebut dipanggil melalui satu loop pada method `tampilkan_stok()`, sehingga setiap objek menjalankan implementasi yang sesuai dengan subclass-nya.

### 2. Duck Typing

Duck typing diterapkan melalui method `ringkasan()` yang terdapat pada kelas `Stock` dan `SertifikatKeaslian`. Kedua kelas tersebut tidak memiliki hubungan pewarisan, tetapi menyediakan method dengan nama yang sama.

Fungsi `tampilkan_ringkasan(objek)` dapat digunakan untuk memanggil method tersebut pada objek dari kedua kelas tanpa memeriksa tipe objeknya terlebih dahulu.

### 3. Operator Overloading

Operator overloading diterapkan melalui magic method `__str__()` pada kelas `Tas`. Method tersebut menentukan representasi teks objek tas ketika ditampilkan menggunakan `print()`.

![Output inventaris Luxe Archive](post-test-pbo-3/output_inventory.png)

## Penerapan Prinsip SOLID (Nilai Plus)

Prinsip SOLID yang diterapkan adalah **Liskov Substitution Principle (LSP)**. Prinsip ini menyatakan bahwa objek subclass harus dapat menggantikan objek superclass tanpa merusak perilaku program.

Penerapannya terlihat pada kelas `Tas` sebagai superclass bagi `TasPreOwnedReguler` dan `TasLimitedEdition`. Kelas `Stock` menerima objek dengan tipe dasar `Tas`, sedangkan method `tampilkan_stok()` memanggil `tampilkanData()` pada setiap objek tas tanpa perlu membedakan subclass-nya. Kedua subclass juga mengimplementasikan abstract method yang diwajibkan oleh superclass.

## Kesimpulan

Program Luxe Archive menerapkan konsep PBO melalui relasi antarkelas, inheritance, abstraksi, polimorfisme, dan operator overloading. Asosiasi diterapkan pada hubungan `Pengguna` dan `Stock`, agregasi pada hubungan `Stock` dan `Tas`, serta komposisi pada hubungan `Tas` dan `SertifikatKeaslian`.

Penerapan abstraksi menetapkan method yang wajib diimplementasikan oleh subclass, sedangkan polimorfisme memungkinkan objek dari subclass berbeda menjalankan perilakunya masing-masing melalui pemanggilan method yang sama. Prinsip LSP juga diterapkan secara sederhana melalui penggunaan subclass `Tas` pada proses pengelolaan inventaris.
