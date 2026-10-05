# Playlist Manager
**Nama :** Nova Cynthia <br>
**NIM :** 2609116031 <br>
**Program Studi :** Sistem Informasi <br>
**Kelas :** A 2026 <br>
**Mata Kuliah :** Pratikum Dasar-Dasar Pemograman <br>

## Deskripsi
program ini bernama "Playlist Manager" dimana terdapat 2 role, yaitu Admin dan User. Perbedaannya berasal dari fasilitas yang didapat dan untuk login sebagai Admin harus menggunakan password. Fasilitas role 'Admin' dapat melihat lagu, menambahkan lagu, mengedit lagu yang sudah ada, dan menghapus lagu yang sudah ada. Sedangkan role 'User' hanya dapat melihat lagu, membuat playlist, menambahkan lagu ke playlist, dan menghapus lagu dari playlist. Berikut type kode-kode yang saya gunakan : <br>
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
11. ``else`` berfungsi dalam pengambilan keputusan jika *if* tidak terpenuhi atau terlaksana. Jenis *conditional statement* ini digunakan setiap peng*input*tan pada Pengguna jika kondisi **if** dan **elif** tidak terpenuhi.
12. ``break``berfungsi untuk menghentikan secara paksa program. Jenis *transfer statement* ini digunakan pada pemilihan "Exit" di bagian daftar menu.
13. ``continue`` berfungsi untuk melewatkan intruksi setelahnya atau kembali ke intruksi awal. Jenis *transfer statement* ini digunakan saat Pengguna memilih di daftar menu ketika Pengguna memasukkan angka yang tidak sesuai dengan yang disediakan.
14. ``return`` berfungsi untuk mengembalikan nilai dari sebuah fungsi ke bagian program yang memanggilnya. Digunakan pada setiap function yang saya buat untuk mengembalikan ke bagian menu.
15. ``print`` berfungsi untuk menampilkan intruksi yang kita berikan.
16. ``input`` berfungsi untuk memasukkan data dari Pengguna.

## Flowchart
### Menu Login
Flowchart berikut menggambarkan alur saat pembuka dan dalam pemilihan role. Sebelum melakukan peng*input*an Pengguna akan ditampilkan nama dari program Playlist Manager dan memasukkan nama. Setelah itu terdapat 3 pilihan yaitu, role Admin, User, dan keluar.
<br>
<img width="400" alt="Minpro_2-Page-1" src="https://github.com/user-attachments/assets/46fc71b1-6761-4052-a944-93dadf6ea59a" />
### Menu Role
Flowchart berikut menggambarkan alur setelah Pengguna memilih role. Khusus role Admin harus memasukkan password terlebih dahulu, jika password salah maka akan kembali ke menu login. Seperti yang terlihat role Admin dapat melakukan perubahan pada daftar lagu, yaitu menambahkan, mengedit, dan menghapus. Sedangkan untuk role User hanya dapat melakukan perubahan pada playlist, seperti menambahkan, menghapus, dan melihat playlist.
<br>
<img width="500" alt="Minpro_2-Page-2" src="https://github.com/user-attachments/assets/c9ddbd77-628c-4ba1-a3f5-e2e5ef6fdc99" />
### Menu Admin
Flowchart berikut menggambarkan alur dari isi menu Admin, yaitu menambahkan, mengedit, menghapus, dan melihat lagu sebelum dan sesudah ditambahkan. Bagian menambahkan dan mengedit lagu Pengguna diminta untuk menginputkan judul lagu dan nama artis, tetapi jika saat menambahkan lagu ada judul lagu yang sama maka tidak akan ditambahkan. Sedangkan untuk menghapus lagu Pengguna hanya diminta untuk meng*input*kan nomor lagu yang ingin dihapus dan daftar akan otomatis diperbarui. Terakhir untuk melihat hanya berfungsi untuk melihat saja.
<br>
<img width="450" alt="Minpro_2-Page-3" src="https://github.com/user-attachments/assets/b079b568-3797-4542-9cf7-97c16a4fe0fa" />
### Menu User
Flowchart berikut menggambarkan alur dari isi menu User, yaitu membuat playlist, menambahkan lagu ke playlist, menghapus lagu dari playlist, dan melihat lagu & playlist. Bagian membuat playlist Pengguna diminta untuk mengisi nama playlist, Pengguna bisa mendapatkan nama dengan angka *random* jika menekan "Enter". Sedangkan untuk menambahkan lagu ke playlist dan menghapus dari playlist dengan cara meng*input*kan nomor lagu yang ingin ditambahkan atau dihapus. Terakhir yaitu melihat lagu dan playlist hanya berfungsi untuk melihat saja, tetapi jika Pengguna belum menambahkan lagu maka playlist hanya kosong dan diminta untuk menambahkan lagu terlebih dahulu.
<br>
<img width="450" alt="Minpro_2-Page-4" src="https://github.com/user-attachments/assets/3fe46338-c107-4e4c-bcd7-409bb5615459" />

## Output
### Output Pembuka
Sebagai pembuka, program akan menampilkan nama dari program yaitu MusicaHolic dan meminta Pengguna untuk meng*input*kan nama.
<br>
<img width="450" alt="Screenshot 2026-10-05 161706" src="https://github.com/user-attachments/assets/22f15e70-bdba-453d-96a1-51a8d9ebed1b" />
### Output Menu Login
Setelah me*input*kan nama, program akan menampilkan menu login, yaitu Admin, User, dan keluar. Pada bagian ini, setelah Pengguna meng*input*kan pilihannya layar tampilan akan dibersihkan. Jika Pengguna meng*input*kan huruf atau angka yang tidak tersedia di pilihan, maka program akan menampilkan "Nomor tidak valid!" dan melakukan *looping* ke bagian menu login.
<br>
<img width="400" alt="Screenshot 2026-10-05 162024" src="https://github.com/user-attachments/assets/f72e38ce-b1b3-41eb-b3aa-f555530b5126" />
#### Output ketika tidak menginputkan angka dan angka tidak tersedia
<img width="400" alt="Screenshot 2026-10-05 162042" src="https://github.com/user-attachments/assets/e57c4ae1-ad15-4fee-afc1-ffdf06090f9a" />

### Output Menu Admin
Sebelum menampilkan daftar menu Admin, Pengguna diminta untuk memasukkan *password*. Jika *password* salah maka program akan melakukan *return* ke menu login, sedangkan jika *password* benar maka akan dianggap login berhasil dan langsung menampilkan menu Admin.
#### Output memasukkan password
a. Jika *password* salah
<br>
<img width="500" alt="Screenshot 2026-10-05 162735" src="https://github.com/user-attachments/assets/eaa4caff-034d-4090-82db-c1c9dc00db63" />




b. Jika *password* benar
<br>
<img width="500" alt="Screenshot 2026-10-05 162812" src="https://github.com/user-attachments/assets/dd1b825f-11ed-4097-92bc-7b68a6d32130" />

#### Output lihat lagu
Menu Admin yang fungsinya untuk melihat daftar lagu saat ini dan setelah diperbarui. Setelah itu program akan langsung melakukan *looping* ke menampilkan menu Admin.
<br>
<img width="500" alt="Screenshot 2026-10-05 164806" src="https://github.com/user-attachments/assets/eda33231-2760-4d91-973d-3d1f06e879c7" />

#### Output tambah lagu
Menu Admin yang fungsinya untuk menambahkan lagu ke daftar lagu yang sudah ada saat ini dengan cara memasukkan judul lagu dan nama artisnya. Setelah itu, program akan melakukan *validation* dengan menanyakan apakah sudah selesai menginput. Jika sudah maka akan kembali ke menu Admin, namun jika tidak maka akan melanjutkan memasukkan judul lagu dan nama artisnya. ***Catatan:*** Jika judul lagu sudah pernah diinputkan sebelumnya, maka program akan menampilkan lagu sudah ada di daftar lagu. <br>
a. Jika judul lagu belum ada di daftar lagu
<br>
<img width="300" alt="Screenshot 2026-10-05 164941" src="https://github.com/user-attachments/assets/eaf16a54-98a2-4a3f-9f89-223343c855b3" />



b. Jika judul lagu sudah ada di daftar lagu
<br>
<img width="300" alt="Screenshot 2026-10-05 165103" src="https://github.com/user-attachments/assets/13409b64-3f3d-4f13-a051-7808118b7b07" />



c. Jika ingin menambahkan lagu lagi
<br>
<img width="300" alt="Screenshot 2026-10-05 165222" src="https://github.com/user-attachments/assets/87ef8149-250b-41d3-b8e7-b00a5ff01580" />



d. Jika tidak ingin menambahkan lagu lagi
<br>
<img width="300" alt="Screenshot 2026-10-05 165307" src="https://github.com/user-attachments/assets/0ad7b13f-e316-4a74-9526-ffc942a1f7fd" />

#### Output hapus lagu
Menu Admin yang fungsinya untuk menghapus lagu yang sudah ada di daftar lagu dengan cara memasukkan nomor lagu yang ingin dihapus. Pada bagian ini, daftar lagu akan ditampilkan secara terus-menerus setelah Pengguna memasukkan nomor lagu tersebut dan daftar lagu otomatis akan diperbarui. Pengguna dapat mengetikkan nomor "0" untuk selesai atau batal. <br>
a. Jika tidak berupa angka dan angka tidak tersedia
<br>
<img width="400" alt="Screenshot 2026-10-05 165450" src="https://github.com/user-attachments/assets/edace682-eec3-4a8b-a5c8-df1f864adf0b" />




<img width="400" alt="Screenshot 2026-10-05 165436" src="https://github.com/user-attachments/assets/5ce43f3f-0ea9-4719-bb78-4e619f0869f1" />




b. Jika sesuai angka yang tersedia
<br>
<img width="300" alt="Screenshot 2026-10-05 165619" src="https://github.com/user-attachments/assets/eafb5f3e-44d3-4495-b205-a573d6fef9ca" />




c. Jika "0" untuk batal/selesai
<br>
<img width="400" alt="Screenshot 2026-10-05 181131" src="https://github.com/user-attachments/assets/c9822f04-6a41-4931-87f2-029a89f06929" />


#### Output logout
Menu Admin yang fungsinya keluar dari mode Admin dan langsung akan menampilkan ke menu login.
<br>
<img width="300" alt="Screenshot 2026-10-05 170049" src="https://github.com/user-attachments/assets/cda4e89f-698f-46fe-95d8-23c333d27c77" />

### Output Menu User
Pada menu ini Pengguna tidak dimintai *password* dan langsung ditampilkan ke menu User. Pada menu User terdapat banyak pilihan yang tersedia tapi hanya pada bagian playlist, yaitu :
#### Output lihat lagu
yang berfungsi untuk melihat daftar lagu yang sudah diperbarui oleh role Admin. Setelah itu program akan langsung melakukan *looping* ke menampilkan menu User.
<br>
<img width="300" alt="Screenshot 2026-10-05 171620" src="https://github.com/user-attachments/assets/5c25e1ec-58fd-468a-922b-2b939a2dce59" />

#### Output buat playlist
Menu User yang berfungsi untuk membuat nama playlist dan menyimpan lagu yang sudah ditambahkan User. Pengguna dapat membuat nama dengan nomor angka yaitu menekan tombol enter dan juga dapat memasukkan nama yang diinginkan dengan huruf, angka, atau kombinasi. Jika sebelumnya sudah pernah membuat playlist, Pengguna dapat mengganti namanya lagi. Setelah selesai memebuat playlist, program akan melakukan *looping* ke menu User. <br>
a. Nama dengan angka random
<br>
<img width="300" alt="Screenshot 2026-10-05 170724" src="https://github.com/user-attachments/assets/515f04c3-966b-4802-9cef-b5b716256d33" />



b. Ganti nama playlist
<br>
<img width="450" alt="Screenshot 2026-10-05 172036" src="https://github.com/user-attachments/assets/227df9b1-a151-47a0-958c-62eeb242abbf" />

#### Lihat playlist
Menu User yang berfungsi untuk melihat isi playlist saat ini dan yang sudah diperbarui. Jika Pengguna belum membuat playlist, maka program akan menampilkan "playlist kosong" dan melakukan *return* ke menu User.<br>
a. Playlist kosong
<br>
<img width="400" alt="Screenshot 2026-10-05 172219" src="https://github.com/user-attachments/assets/2dcc5251-10ee-4fa3-af57-5a75e2e90da3" />



b. Playlist berisi
<br>
<img width="400" alt="Screenshot 2026-10-05 173940" src="https://github.com/user-attachments/assets/2c2c2c5f-47a1-43c7-90cb-34fb88267cc2" />

#### Tambah lagu ke playlist
Menu User yang berfungsi untuk menambahkan lagu ke playlist dengan cara memasukkan nomor lagu yang ingin ditambahkan. Jika memasukkan selain angka atau nomor yang dimasukkan tidak tersedia, maka program akan menampilkan "harus berupa angka" atau "nomor tidak tersedia" dan melakukan *looping* ke bagian peng*input*tan nomor lagu. Apabila pengguna belum membuat playlist maka pengguna diharuskan untuk membuat terlebih dahulu. Pengguna dapat memasukkan angka "0" untuk selesai/batal. ***Catatan:*** Jika Pengguna memasukkan nomor yang sama, maka program akan menampilkan lagu sudah ada di playlist.<br>
a. Belum membuat playlist
<br>
<img width="450" alt="Screenshot 2026-10-05 172714" src="https://github.com/user-attachments/assets/9d0028f2-2b53-43ca-9cde-067f1b1d590e" />



b. Jika tidak berupa angka dan angka tidak tersedia
<br>
<img width="450" alt="Screenshot 2026-10-05 173004" src="https://github.com/user-attachments/assets/d6b0273d-6988-4067-9748-d22eb82dbb23" />



c. Jika sesuai angka yang tersedia
<br>
<img width="450" alt="Screenshot 2026-10-05 173129" src="https://github.com/user-attachments/assets/d876a875-b416-4da7-a2d7-ea2ef2d6f5aa" />



d. Jika lagu sudah ada di playlist
<br>
<img width="350" alt="Screenshot 2026-10-05 173302" src="https://github.com/user-attachments/assets/b437ff5a-036b-4fe7-8277-c964cd300671" />

#### Hapus lagu
Menu User yang berfungsi untukmenghapus lagu dari playlist dengan cara memasukkan nomor lagu yang ingin ditambahkan. Jika memasukkan selain angka atau nomor yang dimasukkan tidak tersedia, maka program akan menampilkan "harus berupa angka" atau "nomor tidak tersedia" dan melakukan *looping* ke bagian peng*input*tan nomor lagu. Apabila pengguna belum membuat playlist maka pengguna diharuskan untuk membuat terlebih dahulu. Pengguna dapat memasukkan angka "0" untuk selesai/batal. ***Catatan:*** Jika Pengguna memasukkan nomor yang sama, maka program akan menampilkan lagu sudah ada di playlist. <br>
a. Belum membuat playlist
<br>
<img width="400" alt="Screenshot 2026-10-05 173454" src="https://github.com/user-attachments/assets/2d690f9d-8b43-4cc5-8f34-5b7ee0f22648" />


b. Belum menambahkan lagu
<br>
<img width="400" alt="Screenshot 2026-10-05 173535" src="https://github.com/user-attachments/assets/1e42d96a-bd18-401a-8d47-d2d3387a1223" />



c. Jika tidak berupa angka dan angka tidak tersedia
<br>
<img width="400" alt="Screenshot 2026-10-05 173747" src="https://github.com/user-attachments/assets/f3a16c4b-2980-4202-8829-478f9a9c10af" />



<img width="400" alt="Screenshot 2026-10-05 173731" src="https://github.com/user-attachments/assets/c013c89e-3eeb-4982-9916-7f837f8e0d9c" />




c. Jika sesuai angka yang tersedia
<br>
<img width="400" alt="Screenshot 2026-10-05 173649" src="https://github.com/user-attachments/assets/985bcc70-90be-4d1b-91b7-d05b0fe1fc05" />

#### Logout
Menu User yang fungsinya keluar dari mode User dan langsung akan menampilkan ke menu login.
<br>
<img width="400" alt="Screenshot 2026-10-05 174127" src="https://github.com/user-attachments/assets/8363ac28-5929-47b8-ae9a-61db8b5f21ac" />

### Output Keluar
Pilihan ini berfungsi untuk keluar dari program. <br>
<img width="400" alt="Screenshot 2026-10-05 174142" src="https://github.com/user-attachments/assets/fa2d4b8b-5009-45de-9c98-7323ad31138e" />









