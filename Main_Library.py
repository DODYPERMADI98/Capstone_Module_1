from tabulate import tabulate
import pyinputplus as pyip

# Dictionary data buku
buku = {
    "A001": {"Judul": "Letterland ABC", "Kategori": "Anak", "Penulis": "Richard Carlisle", "Tahun": 1985, "Stok": 2},
    "A002": {"Judul": "Animal Planet", "Kategori": "Anak", "Penulis": "Phil Whitfield", "Tahun": 2023, "Stok": 4},
    "N001": {"Judul": "Negeri 5 Menara", "Kategori": "Novel", "Penulis": "Ahmad Fuadi", "Tahun": 2009, "Stok": 2},
    "N002": {"Judul": "Laskar Pelangi", "Kategori": "Novel", "Penulis": "Andrea Hinata", "Tahun": 2005, "Stok": 2},
    "K001": {"Judul": "Naruto Shippuden", "Kategori": "Komik", "Penulis": "Masashi Kishimoto", "Tahun": 2007, "Stok": 14},
    "K002": {"Judul": "Si Juki", "Kategori": "Komik", "Penulis": "Faza Meonk", "Tahun": 2017, "Stok": 7},
    "M001": {"Judul": "Atomic Habits", "Kategori": "Motivasi", "Penulis": "James Clear", "Tahun": 2018, "Stok": 3},
    "M002": {"Judul": "How to Win Friends and Influence People", "Kategori": "Motivasi", "Penulis": "Dale Carnegie", "Tahun": 2936, "Stok": 2},
}

# List kosong untuk menyimpan data buku yang dipinjam
daftar_buku_dipinjam = []

# Tentukan header untuk tabel
header_tabel = ["Kode Buku", "Judul", "Penulis", "Kategori", "Tahun", "Stok"]

# Ekstrak nilai dari kamus data buku
data_tabel = [[kode, buku["Judul"], buku["Penulis"], buku["Kategori"], buku.get("Tahun", ""), buku["Stok"]] for kode, buku in buku.items()]

# Fungsi untuk membersihkan layar
def bersihkan_layar():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk menampilkan menu utama
def tampilkan_menu():
    bersihkan_layar()
    print("============================================\n")
    print("SELAMAT DATANG DI SISTEM PERPUSTAKAAN JCDS YK\n")
    print("============================================")
    print("Silahkan pilih menu di bawah:\n")
    print("1. Laporan Data Buku")
    print("2. Tambah Buku")
    print("3. Perbarui Data Buku")
    print("4. Hapus Data Buku")
    print("5. Pinjam Buku")
    print("6. Keluar dari Program\n")
    print("============================================")

# Fungsi untuk menampilkan data buku menggunakan tabulate
def tampilkan_buku():
    print(tabulate(data_tabel, headers=header_tabel, tablefmt="fancy_grid"))

# Fungsi untuk menu laporan
def tampilkan_menu_laporan():
    print("Menu Laporan")
    print("Silahkan pilih menu di bawah:\n")
    print("1. Semua data buku")
    print("2. Cari berdasarkan Kode Buku")
    print("3. Cari berdasarkan Kategori Buku")
    print("4. Kembali ke menu utama")

# Fungsi untuk menampilkan data buku berdasarkan Kode Buku
def tampilkan_buku_berdasarkan_kode():
    kode = pyip.inputStr("Masukkan Kode Buku: ").capitalize()
    buku_data = buku.get(kode)
    if buku_data:
        print("\nKode Buku:", kode)
        print("Judul:", buku_data['Judul'])
        print("Penulis:", buku_data['Penulis'])
        print("Kategori:", buku_data['Kategori'])
        print("Tahun:", buku_data.get("Tahun", ""))
        print("Stok:", buku_data['Stok'])
        print()
    else:
        print("Buku tidak ditemukan")

# Fungsi untuk mencari buku berdasarkan kategori
def cari_buku_berdasarkan_kategori():
    kategori = pyip.inputChoice(["Anak", "Novel", "Komik", "Motivasi"], prompt="Masukkan kategori: ").capitalize()
    buku_kategori = [buku for buku in buku.values() if buku["Kategori"] == kategori]
    if buku_kategori:
        data_tabel_kategori = [[buku["Judul"], buku["Penulis"], buku.get("Tahun", ""), buku["Stok"]] for buku in buku_kategori]
        header_tabel_kategori = ["Judul", "Penulis", "Tahun", "Stok"]
        print(tabulate(data_tabel_kategori, headers=header_tabel_kategori, tablefmt="fancy_grid"))
    else:
        print(f"Tidak ada buku dalam kategori '{kategori}'.")

# Fungsi untuk menambahkan data buku
def menu_tambah_data_buku():
    while True:
        bersihkan_layar()
        print("TAMBAH BUKU")
        print("Silahkan pilih menu di bawah:\n")
        print("1. Tambah Buku")
        print("2. Kembali ke Menu Utama")

        pilihan_tambah = pyip.inputChoice(["1", "2"], prompt="Pilih menu 1-2: ")
        
        if pilihan_tambah == "1":
            kode = pyip.inputStr("Masukkan Kode Buku: ").capitalize()
            if kode in buku:
                print("Buku dengan Kode Buku tersebut sudah ada.")
            else:
                judul = pyip.inputStr("Judul Buku: ")
                penulis = pyip.inputStr("Penulis: ")
                kategori = pyip.inputChoice(["Anak", "Novel", "Komik", "Motivasi"], prompt="Masukkan kategori: ").capitalize()
                tahun = pyip.inputInt("Tahun Terbit: ")
                stok = pyip.inputInt("Stok: ")

                # Tampilkan informasi buku untuk konfirmasi
                print("\nInformasi Buku:")
                print(f"Kode Buku: {kode}")
                print(f"Judul: {judul}")
                print(f"Penulis: {penulis}")
                print(f"Kategori: {kategori}")
                print(f"Tahun Terbit: {tahun}")
                print(f"Stok: {stok}")

                konfirmasi = pyip.inputChoice(["Ya", "Tidak"], prompt="Konfirmasi penambahan buku ini? (Ya/Tidak): ")

                if konfirmasi == "Ya":
                    buku[kode] = {"Judul": judul, "Penulis": penulis, "Kategori": kategori, "Tahun": tahun, "Stok": stok}
                    data_tabel.append([kode, judul, penulis, kategori, tahun, stok])
                    print("Buku berhasil ditambahkan.")
                    input("Tekan Enter untuk melanjutkan...")
                else:
                    print("Buku tidak ditambahkan.")
                    input("Tekan Enter untuk melanjutkan...")

        elif pilihan_tambah == "2":
            break



# Fungsi untuk menghapus buku berdasarkan Kode Buku
def hapus_buku():
    bersihkan_layar()
    print("HAPUS DATA BUKU")
    kode = pyip.inputStr("Masukkan Kode Buku yang akan dihapus: ").capitalize()
    if kode in buku:
        buku_data = buku[kode]
        konfirmasi = pyip.inputChoice(["Ya", "Tidak"], prompt=f"Anda yakin ingin menghapus '{buku_data['Judul']}' (Kode Buku: {kode})? (Ya/Tidak): ")
        if konfirmasi == "Ya":
            # Hapus buku dari kamus dan data_tabel
            del buku[kode]
            for i, data_buku in enumerate(data_tabel):
                if data_buku[0] == kode:
                    del data_tabel[i]
            print(f"Buku '{buku_data['Judul']}' (Kode Buku: {kode}) berhasil dihapus.")
        else:
            print("Data buku tidak dihapus.")
    else:
        print("Buku dengan Kode Buku tidak ditemukan.")

# Fungsi untuk memperbarui data buku
def perbarui_buku():
    bersihkan_layar()
    print("PERBARUI DATA BUKU")
    print("Silahkan pilih menu di bawah:\n")
    print("1. Perbarui Informasi Buku")
    print("2. Kembali ke Menu Utama")

    pilihan_perbarui = pyip.inputChoice(["1", "2"], prompt="Pilih menu 1-2: ")
    if pilihan_perbarui == "1":
        kode = pyip.inputStr("Masukkan Kode Buku: ").capitalize()
        if kode in buku:
            print("Masukkan informasi baru (biarkan kosong untuk mempertahankan yang sebelumnya):")
            judul_baru = pyip.inputStr(f"Masukkan judul baru untuk '{buku[kode]['Judul']}': ", blank=True) or buku[kode]['Judul']
            penulis_baru = pyip.inputStr(f"Masukkan penulis baru untuk '{buku[kode]['Penulis']}': ", blank=True) or buku[kode]['Penulis']
            kategori_baru = pyip.inputChoice(
                ["Anak", "Novel", "Komik", "Motivasi"],
                prompt=f"Masukkan kategori baru untuk '{buku[kode]['Kategori']}': ",
                blank=True
            ) or buku[kode]['Kategori']
            tahun_baru = pyip.inputInt(f"Masukkan tahun terbit baru untuk '{buku[kode].get('Tahun', '')}': ", blank=True) or buku[kode].get('Tahun', None)
            stok_baru = pyip.inputInt(f"Masukkan stok baru untuk '{buku[kode]['Stok']}': ", blank=True) or buku[kode]['Stok']

            # Tampilkan informasi buku yang diperbarui untuk konfirmasi
            print("\nInformasi Buku yang Diperbarui:")
            print(f"Kode Buku: {kode}")
            print(f"Judul Baru: {judul_baru}")
            print(f"Penulis Baru: {penulis_baru}")
            print(f"Kategori Baru: {kategori_baru}")
            print(f"Tahun Terbit Baru: {tahun_baru}")
            print(f"Stok Baru: {stok_baru}")

            konfirmasi = pyip.inputChoice(["Ya", "Tidak"], prompt="Konfirmasi pembaruan data buku ini? (Ya/Tidak): ")

            if konfirmasi == "Ya":
                buku[kode]["Judul"] = judul_baru
                buku[kode]["Penulis"] = penulis_baru
                buku[kode]["Kategori"] = kategori_baru
                if tahun_baru is not None:
                    buku[kode]["Tahun"] = tahun_baru
                buku[kode]["Stok"] = stok_baru
                for i, data_buku in enumerate(data_tabel):
                    if data_buku[0] == kode:
                        data_tabel[i] = [kode, judul_baru, penulis_baru, kategori_baru, tahun_baru, stok_baru]
                print("Data buku berhasil diperbarui!")

                # Tampilkan database buku yang diperbarui
                tampilkan_database_buku()
            else:
                print("Data buku tidak diperbarui.")
        else:
            print("Buku dengan Kode Buku tidak ditemukan.")
    elif pilihan_perbarui == "2":
        return

# Fungsi untuk menampilkan database buku
def tampilkan_database_buku():
    print("Database Buku Saat Ini:")
    print(tabulate([[kode, buku["Judul"], buku["Penulis"], buku["Kategori"], buku.get("Tahun", ""), buku["Stok"]] for kode, buku in buku.items()], headers=header_tabel, tablefmt="fancy_grid"))

# Fungsi untuk meminjam buku
def pinjam_buku():
    bersihkan_layar()
    print("PINJAM BUKU")
    print("Anda dapat meminjam antara 1 hingga 4 buku yang berbeda.")
    jumlah_buku_pinjam = pyip.inputInt("Masukkan jumlah buku yang ingin dipinjam: ", min=1, max=4)

    # List untuk melacak buku yang berhasil dipinjam
    buku_berhasil_dipinjam = []

    for i in range(jumlah_buku_pinjam):
        kode = pyip.inputStr(f"Masukkan Kode Buku untuk buku ke-{i+1}: ").capitalize()
        buku_data = buku.get(kode)
        if buku_data:
            if buku_data["Stok"] > 0:
                # Tambahkan buku yang dipinjam ke daftar
                daftar_buku_dipinjam.append(buku_data)
                # Kurangi stok
                buku_data["Stok"] -= 1
                # Tambahkan ke daftar buku yang berhasil dipinjam
                buku_berhasil_dipinjam.append(buku_data)
                print(f"Buku '{buku_data['Judul']}' (Kode Buku: {kode}) berhasil dipinjam.")
            else:
                print(f"Buku '{buku_data['Judul']}' habis stok.")
        else:
            print(f"Buku dengan Kode Buku '{kode}' tidak ditemukan.")

    if buku_berhasil_dipinjam:
        print("\nAnda telah meminjam buku-buku berikut:")
        print(tabulate([[buku_data["Judul"], buku_data["Penulis"]] for buku_data in buku_berhasil_dipinjam], headers=["Judul", "Penulis"], tablefmt="fancy_grid"))

    # Tampilkan database buku yang diperbarui
    tampilkan_database_buku()

    # Tunggu input pengguna sebelum kembali ke menu utama
    input("Tekan Enter untuk melanjutkan...")

# Loop program utama
while True:
    tampilkan_menu()
    pilihan = pyip.inputChoice(["1", "2", "3", "4", "5", "6"], prompt= "Silahkan Menu 1-6: ")
    if pilihan == "1":
        while True:
            tampilkan_menu_laporan()
            pilihan_laporan = pyip.inputChoice(["1", "2", "3", "4"], prompt= "Silahkan Menu 1-4: ")
            if pilihan_laporan == "1":
                tampilkan_buku()
            elif pilihan_laporan == "2":
                tampilkan_buku_berdasarkan_kode()
            elif pilihan_laporan == "3":
                cari_buku_berdasarkan_kategori()
            elif pilihan_laporan == "4":
                break
            else:
                print("Pilihan tidak valid, silakan pilih menu yang valid.")
    elif pilihan == "2":
        menu_tambah_data_buku()
    elif pilihan == "3":
        perbarui_buku()
    elif pilihan == "4":
        hapus_buku()
    elif pilihan == "5":
        pinjam_buku()
    elif pilihan == "6":
        print("Terima kasih telah menggunakan program ini.")
        break
