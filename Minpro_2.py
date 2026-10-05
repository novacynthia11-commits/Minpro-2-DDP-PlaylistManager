import os
import pwinput
import random

print("-" * 35)
print("   SELAMAT DATANG DI MusicaHolic")
print("-" * 35)

katalog = ["kiss me - Ariana Grande",
        "Drag Path - Twenty One Pilots",
        "Enter Sandman - Metallica",
        "Autumn - NIKI",
        "Sound Of Rain - Lany",
        "Join Me - HIM",
        "4ME 4ME - Malcolm Todd",
        "Bila Kau Tidak Disampingku - Sheila On 7",
        "Evanescence - your star",
        "Besame Mucho - Andrea Bocelli"]
playlist = {"ngaran_playlist": "",
            "lagu" : []}

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

#Lihat daftar lagi
def lihat_lagu():
    print("-" * 35)
    print ("            Daftar Lagu ")
    print("-" * 35)
    for i in range(len(katalog)):
        print(f"{i+1}. {katalog[i]}")

#Tambah lagu
def tambah_lagu():
    while True:
        bersihkan_layar()
        judul = input("Masukkan judul lagu: ")
        artis = input("Masukkan nama artis: ")
        lagu_baru = f"{judul} - {artis}"

        sudah_ada = False
        for lagu in katalog:
            if lagu.lower() == lagu_baru.lower():
                sudah_ada = True

        if judul == "" or artis == "":
            print("Judul lagu dan nama artis tidak boleh kosong!")
        elif sudah_ada:
            print("Lagu sudah ada dalam katalog!")
        else:
            katalog.append(f"{judul} - {artis}")
            print(f"\x1B[3mLagu '{judul} - {artis}' telah ditambahkan!\x1B[0m")

        betakun = input("Ingin menambahkan lagu lagi? (y/n): ").lower()
        if betakun != "y":
            return


#Edit lagu
def edit_lagu():
    lihat_lagu()
    while True:
        nomor = input("\nMasukkan nomor lagu yang ingin diedit (0 = 'batal/selesai'): ")

        if nomor == "0":
            return

        if not nomor.isdigit():
            print("Harus berupa angka!")
            continue

        nilai = int(nomor)
        if nilai < 1 or nilai > len(katalog):
            print("Nomor lagu tidak valid!")
            continue

        judul_baru = input("\nMasukkan judul lagu baru: ")
        artis_baru = input("Masukkan nama artis baru: ")
    
        ada = False
        for new in katalog:
            if new.lower() == judul_baru.lower():
                ada = True
            
        if judul_baru == "" or artis_baru == "":
            print("Judul lagu dan nama artis tidak boleh kosong!")
        elif ada :
            print("Lagu sudah ada di daftar!")
        else:
            katalog[int(nomor) - 1] = f"{judul_baru} - {artis_baru}"
            print(f"\x1B[0mLagu pada nomor {nomor} telah diperbarui menjadi '{judul_baru} - {artis_baru}'!\x1B[0m")

#Hapus lagu
def hapus_lagu():
    while True:
        lihat_lagu()
        try:
            angka = int(input("\nMasukkan nomor lagu yang ingin dihapus (0 = 'batal/selesai'): "))
        except ValueError:
            print("Harus berupa angka!")
            continue
        
        if angka == 0:
            return
        
        if angka < 1 or angka > len(katalog):
            print("Nomor tidak valid!")
            continue
        else:
            lagu_dihapus = katalog.pop(angka - 1)
            print(f"\x1B[3m{lagu_dihapus} berhasil dihapus!\x1B[0m")

# ==========================================================================================

#lihat playlist
def lihat_playlist():
    print("=" * 35)
    print(f"        Playlist {playlist['ngaran_playlist']}")
    print("=" * 35)

    if len(playlist["lagu"]) == 0:
        print("Playlist masih kosong ૮(˶╥︿╥)ა")
        return
    else:
        for i in range (len(playlist["lagu"])):
            lagu = playlist["lagu"][i]
            print(f"{i + 1}. {lagu}")

#hapus dari playlist
def del_lagu_playlist():
    if playlist["ngaran_playlist"] == "":
        print("Buat playlist terlebih dahulu!")
        return
    
    while True:
        lihat_playlist()
        if len(playlist["lagu"]) == 0:
            print("Tidak ada yang bisa dihapus! Silahkan isi playlist Anda")
            return

        try:    
            mamilih = int(input("\nMasukkan nomor lagu yang ingin Anda hapus (0 = 'batal/selesai'): "))
        except ValueError:
            print("Harus berupa angka!")
            continue

        if mamilih == 0:
            return

        if mamilih < 1 or mamilih > len(playlist["lagu"]):
            print("Nomor tidak tersedia")
            continue
        else:
            d_lagu = playlist["lagu"].pop (mamilih - 1)
            print(d_lagu, "\x1B[3mberhasil dihapus dari playlist\x1B[0m")

#Buat Playlist
def buat_playlist():
    if playlist["ngaran_playlist"] != "":
        print(f"\x1B[3mPlaylist {playlist['ngaran_playlist']} berhasil dibuat\x1B[0m")
        ganti = input("Ganti nama playlist? (y/n): ")
        if ganti != "y":
            print("Nama playlist tidak diubah")
            return
    nama = input("Masukkan nama playlist (Tekan enter untuk nama acak): ").strip()
    if nama == "":
        nama = f"#{random.randint(1000, 9999)}"
        print("Nama kosong, diisi nama acak.")

    playlist["ngaran_playlist"] = nama
    print(f"\x1B[3mPlaylist {playlist['ngaran_playlist']} berhasil dibuat\x1B[0m")

#tambah ke playlist
def tambah_ke_playlist():
    if playlist["ngaran_playlist"] == "":
        print("Buat playlist terlebih dahulu!")
        return

    lihat_lagu()
    while True:
        try:    
            pilih = int(input("\nMasukkan nomor lagu yang ingin ditambahkan ke playlist (0 = 'selesai'): "))
        except ValueError:
            print("Harus berupa angka!")
            continue

        if pilih == 0:
            break

        if pilih < 1 or pilih > len(katalog):
            print("Nomor tidak valid")
            continue
    
        handak_dipilih = katalog[pilih - 1]
        if handak_dipilih in playlist["lagu"]:
            print("Lagu sudah ada di Playlist!")
        else:
            playlist["lagu"].append(handak_dipilih)
            print(f"\x1B[3mMenambahkan lagu {handak_dipilih} ke {playlist['ngaran_playlist']}\x1B[0m")



#role admin
def main_admin():
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Lihat lagu")
        print("2. Tambah lagu")
        print("3. Edit lagu")
        print("4. Hapus lagu")
        print("0. Logout")
        Amenu = input("Pilih menu: ")

        bersihkan_layar()
        if Amenu == "1":
            lihat_lagu()
        elif Amenu == "2":
            tambah_lagu()
        elif Amenu == "3":
            edit_lagu()
        elif Amenu == "4":
            hapus_lagu()
        elif Amenu == "0":
            print("Logout dari Admin")
            break
        else:
            print("Pilihan tidak tersedia!")
            continue

#role user
def main_user():
    while True:
        print("\n=== MENU USER ===")
        print("1. Lihat lagu")
        print("2. Buat playlist")
        print("3. Lihat playlist")
        print("4. Tambah lagu ke playlist")
        print("5. Hapus lagu dari playlist")
        print("0. Logout")
        Umenu = input("Pilih menu: ")

        bersihkan_layar()
        if Umenu == "1":
            lihat_lagu()
        elif Umenu == "2":
            buat_playlist()
        elif Umenu == "3":
            lihat_playlist()
        elif Umenu == "4":
            tambah_ke_playlist()
        elif Umenu == "5":
            del_lagu_playlist()
        elif Umenu == "0":
            print("Logout dari User")
            break
        else:
            print("Pilihan tidak tersedia!")
            continue

#role
password_admin = "AdminKece#00"
def main():
    ngaran = input("\nMasukkan nama Anda: ")
    while True:
        print ("\n=====APLIKASI MusicaHolic=====")
        print ("1. Login sebagai Admin")
        print ("2. Login sebagai User")
        print ("0. Keluar")
        print ("=" * 31)
        role = input("Pilih menu: ")

        bersihkan_layar()
        if role == "1":
            pwd = pwinput.pwinput("Masukkan password: ")
            if pwd == password_admin:
                print("Login berhasil!")
                print(f"\nSelamat datang, {ngaran}!")
                main_admin()
            else:
                print("Password salah!")
        elif role == "2":
            print(f"Login berhasil!")
            print(f"\nHalo, {ngaran}!")
            main_user()
        elif role == "0":
            print("Terima Kasih dan sampai jumpa kembali! ")
            break
        else:
            print("Nomor tidak valid!")

main()