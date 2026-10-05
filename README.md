# Playlist Manager
**Nama :** Nova Cynthia <br>
**NIM :** 2609116031 <br>
**Program Studi :** Sistem Informasi <br>
**Kelas :** A 2026 <br>
**Mata Kuliah :** Pratikum Dasar-Dasar Pemograman <br>

## Deskripsi
Saya membuat program "Playlist Manager" dimana terdapat 2 role, yaitu Admin dan User. Perbedaannya berasal dari fasilitas yang didapat dan untuk login sebagai Admin harus menggunakan password. Fasilitas role 'Admin' dapat melihat lagu, menambahkan lagu, mengedit lagu yang sudah ada, dan menghapus lagu yang sudah ada. Sedangkan role 'User' hanya dapat melihat lagu, membuat playlist, menambahkan lagu ke playlist, dan menghapus lagu dari playlist. Berikut type kode-kode yang saya gunakan : <br>
1. ``os`` berfungsi untuk mengatur dan berinteraksi dengan sistem operasi komputer. Jenis library ini saya gunakan untuk membersihkan layar setiap pengguna selesai melakukan peng*input*an, kecuali pada bagian hapus lagu dan hapus lagu di playlist.
2. ``pwinput`` berfungsi untuk menyembunyikan *password* dengan cara menampilkan "**" saat peng*input*an. Jenis library ini saya gunakan ketika role 'Admin' ingin *login* dan memasukkan password.
3. ``random`` berfungsi untuk menghasilkan angka acak atau melakukan operasi berbasis keacakkan. Jenis library ini saya gunakan untuk pemilihan nama playlist dengan angka acak.
4. ``function`` berfungsi untuk blok kode dalam fungsi yang tidak akan dijalankan jika tidak dipanggil. Jenis tipe data ini saya gunakan untuk membuat setiap bagian menu dan membuat bagian pada pilihan menu.
5. ``list`` berfungsi untuk menyimpan banyak data dalam satu variabel yang dapat diubah. Jenis tipe data ini saya gunakan untuk menyimpan daftar lagu.
6. ``dictionary`` berfungsi untuk menyimpan data dalam bentuk pasangan. Saya gunakan pada bagian playlist untuk nama dan lagu-lagu yang akan ditambahkan.
7. ``while`` berfungsi melakukan perulangan atau *looping* pada intruksi yang diberikan yang tidak akan berhenti, kecuali terdapat transfer statement (continue dan break). Jenis *looping* ini digunakan pada bagian peng*input*tan angka untuk pemilihan lagu.
8. ``for`` berfungsi melakukan perulangan atau *looping* pada setiap objek yang bisa diulang, seperti **list** dan **tuple**. Digunakan untuk menampilkan perulangan pada daftar lagu dan isi lagu playlist
9. ``if`` berfungsi dalam pengambilan keputusan yang dilakukan oleh Pengguna dan program akan dijalankan sesuai dengan intruksi yang dibuat. Jenis *conditional statement* ini digunakan setiap peng*input*an pada Pengguna.
10. ``elif`` berfungsi dalam menangani keputusan yang banyak pada pengambilan keputusan. Jenis *conditional statement* ini juga digunakan setiap peng*input*an pada Pengguna jika kondisi **if** tidak terpenuhi.
11. ``else`` berfungsi dalam pengambilan keputusan jika *if* tidak terpenuhi atau terlaksana. Jenis *conditional statement* ini digunakan setiap peng*inputtan pada Pengguna jika kondisi **if** dan **elif** tidak terpenuhi.
12. ``break``berfungsi untuk menghentikan secara paksa program. Jenis *transfer statement* ini digunakan pada pemilihan "Exit" di bagian daftar menu.
13. ``continue`` berfungsi untuk melewatkan intruksi setelahnya atau kembali ke intruksi awal. Jenis *transfer statement* ini digunakan saat Pengguna memilih di daftar menu ketika Pengguna memasukkan angka yang tidak sesuai dengan yang disediakan.
14. ``return`` berfungsi untuk mengembalikan nilai dari sebuah fungsi ke bagian program yang memanggilnya. Digunakan pada setiap function yang saya buat untuk mengembalikan ke bagian menu.
15. ``print`` berfungsi untuk menampilkan intruksi yang kita berikan.
16. ``input`` berfungsi untuk memasukkan data dari Pengguna.
17. ``return`` berfungsi untuk menghentikan eksekusi sebuah fungsi dan mengembalikan nilai ke bagian program yang memanggilnya. Digunakan untuk mengembalikan nilai dari operasi matematika biaya hotel.

## Flowchart
