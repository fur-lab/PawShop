import os
import time
import pwinput
from prettytable import PrettyTable
import data  

def tampilkan_header_utama():
    os.system('cls || clear')
    print("=" * 60)
    print("|      SELAMAT DATANG DI TOKO PERALATAN KUCING WINGKY      |")
    print("=" * 60)

def menu_awal():
    print("\n1. Login")
    print("2. Register")
    print("3. Keluar")

def login():
    tampilkan_header_utama()
    print("\n-------------------- LOGIN SECTION -------------------------")
    
    try:
        username = input("Username: ")
        if not username:
            raise ValueError("Username tidak boleh kosong")
        
        password = pwinput.pwinput(prompt="Password: ", mask="*")
        if not password:
            raise ValueError("Password tidak boleh kosong")
        
        # Verifikasi login
        if username in data.pengguna and data.pengguna[username]["password"] == password:
            data.user_login = username
            data.role_login = data.pengguna[username]["role"]
            data.status_login = True
            
            print(f"\nLogin berhasil! Selamat datang, {username}")
            print(f"Role: {data.role_login}")  # Debug
            time.sleep(2)
            return True
        else:
            raise ValueError("Username atau password salah!")
    
    except ValueError as e:
        print(f"\nError: {e}")
        time.sleep(2)
        return False

def register():
    tampilkan_header_utama()
    print("\n-------------------- REGISTER SECTION ----------------------")
    
    try:
        username_baru = input("Username baru: ")
        if not username_baru:
            raise ValueError("Username tidak boleh kosong")
        
        if username_baru in data.pengguna:
            raise ValueError("Username sudah terdaftar!")
        
        username_baru = username_baru.encode('unicode_escape').decode()
        username_baru = username_baru.replace('\\\\','')
        
        password_baru = pwinput.pwinput(prompt="Silahkan input password baru: ", mask="*")
        if not password_baru:
            raise ValueError("Password tidak boleh kosong")
        
        # Validasi Password Minimal 8 Karakter
        if len(password_baru) < 8:
             raise ValueError("Password minimal 8 karakter!")
        
        data.pengguna[username_baru] = {
            "password": password_baru,
            "role": "user"
        }
        
        print(f"\nRegistrasi berhasil! Silakan login dengan username '{username_baru}'")
        time.sleep(2)
        return True
        
    except ValueError as e:
        print(f"\nError: {e}")
        time.sleep(2)
        return False

def menu_user():
    # Tetapkan lebar header yang diinginkan (sama dengan 50 karakter)
    width = 50
    header_text = f"MENU PELANGGAN - Halo, {data.user_login}!"

    # Gunakan str.center(lebar) untuk memusatkan teks dalam lebar 48 (50 - 2 untuk tanda |)
    centered_content = header_text.center(width - 2)

    print("=" * width)
    # Header dirapikan menggunakan string centering
    print(f"|{centered_content}|")
    print("=" * width)
    print("\n1. Lihat Semua Produk")
    print("2. Cari Produk")
    print("3. Tambah ke Keranjang")
    print("4. Lihat Keranjang")
    print("5. Hapus dari Keranjang")
    print("6. Checkout")
    print("7. Logout")

def tambah_keranjang():
    while True:  # loop utama untuk tambah barang
        print("=" * 59)
        print("|                  TAMBAH KE KERANJANG                    |")
        print("=" * 59)

        table = PrettyTable()
        table.field_names = ["ID", "Nama Produk", "Kategori", "Harga", "Stok"]
        table.align["ID"] = "c"
        table.align["Nama Produk"] = "l"
        table.align["Kategori"] = "l"
        table.align["Harga"] = "r"
        table.align["Stok"] = "c"

        for id_produk, produk_data in data.produk.items():
            table.add_row([
                id_produk,
                produk_data['nama'],
                produk_data['kategori'],
                f"Rp {produk_data['harga']:,}",
                produk_data['stok']
            ])

        print(table)

        try:
            id_beli = validasi_input_angka("\nMasukkan ID produk yang ingin dibeli: ", "ID harus berupa angka!")
            if id_beli is None:
                raise ValueError("Input dibatalkan")

            if id_beli not in data.produk:
                raise KeyError("Produk dengan ID tersebut tidak ditemukan!")

            jumlah_beli = validasi_input_angka("Jumlah: ", "Jumlah harus berupa angka!")
            if jumlah_beli is None or jumlah_beli <= 0:
                raise ValueError("Jumlah harus lebih dari 0")

            if jumlah_beli > data.produk[id_beli]["stok"]:
                raise ValueError(f"Stok tidak cukup! Stok tersedia: {data.produk[id_beli]['stok']}")

            if data.user_login not in data.keranjang:
                data.keranjang[data.user_login] = {}

            if id_beli in data.keranjang[data.user_login]:
                data.keranjang[data.user_login][id_beli]["jumlah"] += jumlah_beli
            else:
                data.keranjang[data.user_login][id_beli] = {
                    "nama": data.produk[id_beli]["nama"],
                    "harga": data.produk[id_beli]["harga"],
                    "jumlah": jumlah_beli
                }

            print(f"\n{data.produk[id_beli]['nama']} (x{jumlah_beli}) berhasil ditambahkan ke keranjang!")
            time.sleep(1)

            # Loop untuk tanya "Tambah barang lagi?"
            while True:
                tambah_lagi = input("\nTambah barang lagi? (y/n): ").lower()
                if tambah_lagi == 'y':
                    break  # ulang dari atas
                elif tambah_lagi == 'n':
                    print("Kembali ke menu pelanggan...")
                    time.sleep(1)
                    return  # keluar dari fungsi
                else:
                    print("Input tidak valid. Silakan masukkan 'y' atau 'n'.")

        except (ValueError, KeyError) as e:
            print(f"\nError: {e}")
            print("=" * 59)
            time.sleep(2)

def tampilkan_isi_keranjang(current_user):
    print("=" * 59)
    print("|                   KERANJANG BELANJA                     |")
    print("=" * 59)
    
    if current_user not in data.keranjang or len(data.keranjang[current_user]) == 0:
        print("\nKeranjang belanja kosong.")
        print("=" * 59)
        return 0
    else:
        table = PrettyTable()
        table.field_names = ["No", "Nama Produk", "Harga", "Jumlah", "Subtotal"]
        table.align["No"] = "c"
        table.align["Nama Produk"] = "l"
        table.align["Harga"] = "r"
        table.align["Jumlah"] = "c"
        table.align["Subtotal"] = "r"
        
        nomor = 1
        list_items = []
        
        for id_produk, item in data.keranjang[current_user].items():
            subtotal = item["harga"] * item["jumlah"]
            list_items.append(item)
            table.add_row([
                nomor,
                item['nama'],
                f"Rp {item['harga']:,}",
                item['jumlah'],
                f"Rp {subtotal:,}"
            ])
            nomor += 1
        
        print(table)
        
        total = hitung_total_keranjang_rekursif(list_items)
        
        print(f"{'TOTAL':>10} Rp {total:,}")
        print("=" * 59)
        return total

def cari_produk_dan_tampilkan(keyword):
    print("\n" + "=" * 59)
    print("|                     HASIL PENCARIAN                     |")
    print("=" * 59)
    
    table = PrettyTable()
    table.field_names = ["ID", "Nama Produk", "Kategori", "Harga", "Stok"]
    table.align["ID"] = "c"
    table.align["Nama Produk"] = "l"
    table.align["Kategori"] = "l"
    table.align["Harga"] = "r"
    table.align["Stok"] = "c"
    
    ketemu = False
    for id_produk, produk_data in data.produk.items():
        if keyword.lower() in produk_data['nama'].lower():
            table.add_row([
                id_produk,
                produk_data['nama'],
                produk_data['kategori'],
                f"Rp {produk_data['harga']:,}",
                produk_data['stok']
            ])
            ketemu = True
    
    if ketemu:
        print(table)
    else:
        print("\nProduk tidak ditemukan.")
    print("=" * 59)

def hapus_dari_keranjang():
    print("=" * 38)
    print("|         HAPUS DARI KERANJANG       |")
    print("=" * 38)
    
    if data.user_login not in data.keranjang or len(data.keranjang[data.user_login]) == 0:
        print("\nKeranjang belanja kosong.")
        time.sleep(2)
    else:
        # Menggunakan PrettyTable untuk menampilkan isi keranjang
        table = PrettyTable()
        table.field_names = ["No", "ID", "Nama Produk", "Jumlah"]
        table.align["No"] = "c"
        table.align["ID"] = "c"
        table.align["Nama Produk"] = "l"
        table.align["Jumlah"] = "c"
        
        nomor = 1
        id_list = []
        for id_produk, item in data.keranjang[data.user_login].items():
            table.add_row([
                nomor,
                id_produk,
                item['nama'],
                item['jumlah']
            ])
            id_list.append(id_produk)
            nomor += 1
        
        print(table)
        
        try:
            id_hapus = validasi_input_angka("\nMasukkan ID produk yang ingin dihapus: ", "ID harus berupa angka!")
            if id_hapus is None:
                raise ValueError("Input dibatalkan")
            
            if id_hapus not in data.keranjang[data.user_login]:
                raise KeyError("Produk tidak ada di keranjang!")
            
            konfirmasi = input(f"\nYakin ingin menghapus '{data.keranjang[data.user_login][id_hapus]['nama']}' dari keranjang? (y/n): ")
            if konfirmasi.lower() == "y":
                del data.keranjang[data.user_login][id_hapus]
                print("\nProduk berhasil dihapus dari keranjang!")
            else:
                print("\nPenghapusan dibatalkan.")
            time.sleep(2)
            
        except (ValueError, KeyError) as e:
            print(f"\nError: {e}")
            time.sleep(2)


def checkout():
    print("=" * 59)
    print("|                       CHECKOUT                          |")
    print("=" * 59)
    
    if data.user_login not in data.keranjang or len(data.keranjang[data.user_login]) == 0:
        print("\nKeranjang belanja kosong. Tidak ada yang bisa dicheckout.")
        time.sleep(2)
    else:
        tampilkan_isi_keranjang(data.user_login)
        
        konfirmasi = input("\nLanjutkan checkout? (y/n): ")
        if konfirmasi.lower() == "y":
            # Kurangi stok
            for id_produk, item in data.keranjang[data.user_login].items():
                # Pastikan produk masih ada sebelum mengurangi stok (meskipun seharusnya ada)
                if id_produk in data.produk:
                    data.produk[id_produk]["stok"] -= item["jumlah"]
            
            # Kosongkan keranjang
            data.keranjang[data.user_login] = {}
            
            print("\n" + "=" * 59)
            print("|       Checkout berhasil! Terima kasih telah berbelanja!      |")
            print("=" * 59)
            time.sleep(3)
        else:
            print("\nCheckout dibatalkan.")
            time.sleep(2)

# --- FUNGSI UTAMA MENU LOOP ---

def run_user_menu():
    while data.status_login and data.role_login == "user":
        layar_bersih()
        menu_user()
        
        pilihan = input("\nMasukkan pilihan (1-7): ")
        
        if pilihan == '1':
            tampilkan_daftar_produk()
            input("Tekan ENTER untuk kembali...")
        elif pilihan == '2':
            keyword = input("Masukkan nama produk yang dicari: ")
            cari_produk_dan_tampilkan(keyword)
            input("Tekan ENTER untuk kembali...")
        elif pilihan == '3':
            # ✅ FIX UTAMA: Pastikan Loop berlanjut selama tambah_keranjang mengembalikan True ('y')
            lanjut_tambah = True
            while lanjut_tambah:
                # Nilai kembali dari tambah_keranjang (True/False) menentukan apakah loop ini berjalan lagi
                lanjut_tambah = tambah_keranjang() 
        elif pilihan == '4':
            tampilkan_isi_keranjang(data.user_login)
            input("Tekan ENTER untuk kembali...")
        elif pilihan == '5':
            layar_bersih()
            hapus_dari_keranjang()
        elif pilihan == '6':
            layar_bersih()
            checkout()
        elif pilihan == '7':
            data.status_login = False
            data.user_login = ""
            print("\nAnda telah berhasil Logout.")
            time.sleep(2)
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")
            time.sleep(1)

def main_loop():
    while True:
        tampilkan_header_utama()
        menu_awal()
        
        pilihan = input("\nMasukkan pilihan (1-3): ")
        
        if pilihan == '1':
            login_berhasil = login()
            if login_berhasil and data.role_login == "user":
                run_user_menu()
            # Asumsi: Jika ada role admin, tambahkan di sini
        elif pilihan == '2':
            register()
        elif pilihan == '3':
            print("\nTerima kasih telah mengunjungi Toko Wingky! Sampai jumpa.")
            time.sleep(2)
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")
            time.sleep(1)

if __name__ == "__main__":
    main_loop()

    

def validasi_input_angka(prompt, pesan_error="Input harus berupa angka!"):
    while True:
        try:
            input_str = input(prompt)
            if not input_str:
                return None
            hasil = int(input_str)
            return hasil
        except ValueError:
            print(f"\n{pesan_error}")
            time.sleep(2)
            return None

def hitung_total_keranjang_rekursif(list_items, index=0):
    if index >= len(list_items):
        return 0
    
    item_sekarang = list_items[index]
    subtotal = item_sekarang["harga"] * item_sekarang["jumlah"]
    return subtotal + hitung_total_keranjang_rekursif(list_items, index + 1)

def generate_id_produk_baru():
    if len(data.produk) == 0:
        id_baru = 1
    else:
        id_baru = max(data.produk.keys()) + 1
    return id_baru

def tampilkan_daftar_produk():
    print("\n" + "=" * 59)
    print("|                   DAFTAR PRODUK WINGKY                  |")
    print("=" * 59)
    
    if len(data.produk) == 0:
        print("Tidak ada produk tersedia.")
    else:
        table = PrettyTable()
        table.field_names = ["ID", "Nama Produk", "Kategori", "Harga", "Stok"]
        table.align["ID"] = "c"
        table.align["Nama Produk"] = "l"
        table.align["Kategori"] = "l"
        table.align["Harga"] = "r"
        table.align["Stok"] = "c"
        
        for id_produk, produk_data in data.produk.items():
            table.add_row([
                id_produk,
                produk_data['nama'],
                produk_data['kategori'],
                f"Rp {produk_data['harga']:,}",
                produk_data['stok']
            ])
        
        print(table)
    
    print("=" * 59)

def tambah_keranjang():
    while True:  # loop utama untuk tambah barang
        print("=" * 59)
        print("|                  TAMBAH KE KERANJANG                    |")
        print("=" * 59)

        table = PrettyTable()
        table.field_names = ["ID", "Nama Produk", "Kategori", "Harga", "Stok"]
        table.align["ID"] = "c"
        table.align["Nama Produk"] = "l"
        table.align["Kategori"] = "l"
        table.align["Harga"] = "r"
        table.align["Stok"] = "c"

        for id_produk, produk_data in data.produk.items():
            table.add_row([
                id_produk,
                produk_data['nama'],
                produk_data['kategori'],
                f"Rp {produk_data['harga']:,}",
                produk_data['stok']
            ])

        print(table)

        try:
            id_beli = validasi_input_angka("\nMasukkan ID produk yang ingin dibeli: ", "ID harus berupa angka!")
            if id_beli is None:
                raise ValueError("Input dibatalkan")

            if id_beli not in data.produk:
                raise KeyError("Produk dengan ID tersebut tidak ditemukan!")

            jumlah_beli = validasi_input_angka("Jumlah: ", "Jumlah harus berupa angka!")
            if jumlah_beli is None or jumlah_beli <= 0:
                raise ValueError("Jumlah harus lebih dari 0")

            if jumlah_beli > data.produk[id_beli]["stok"]:
                raise ValueError(f"Stok tidak cukup! Stok tersedia: {data.produk[id_beli]['stok']}")

            if data.user_login not in data.keranjang:
                data.keranjang[data.user_login] = {}

            if id_beli in data.keranjang[data.user_login]:
                data.keranjang[data.user_login][id_beli]["jumlah"] += jumlah_beli
            else:
                data.keranjang[data.user_login][id_beli] = {
                    "nama": data.produk[id_beli]["nama"],
                    "harga": data.produk[id_beli]["harga"],
                    "jumlah": jumlah_beli
                }

            print(f"\n{data.produk[id_beli]['nama']} (x{jumlah_beli}) berhasil ditambahkan ke keranjang!")
            time.sleep(1)

            # Loop untuk tanya "Tambah barang lagi?"
            while True:
                tambah_lagi = input("\nTambah barang lagi? (y/n): ").lower()
                if tambah_lagi == 'y':
                    break  # kembali ke atas loop utama
                elif tambah_lagi == 'n':
                    print("Kembali ke menu pelanggan...")
                    time.sleep(1)
                    return  # keluar dari fungsi
                else:
                    print("Input tidak valid. Silakan masukkan 'y' atau 'n'.")

        except (ValueError, KeyError) as e:
            print(f"\nError: {e}")
            print("=" * 59)
            time.sleep(2)

def tampilkan_isi_keranjang(current_user):
    print("=" * 59)
    print("|                   KERANJANG BELANJA                     |")
    print("=" * 59)
    
    if current_user not in data.keranjang or len(data.keranjang[current_user]) == 0:
        print("\nKeranjang belanja kosong.")
        print("=" * 59)
        return 0
    else:
        table = PrettyTable()
        table.field_names = ["No", "Nama Produk", "Harga", "Jumlah", "Subtotal"]
        table.align["No"] = "c"
        table.align["Nama Produk"] = "l"
        table.align["Harga"] = "r"
        table.align["Jumlah"] = "c"
        table.align["Subtotal"] = "r"
        
        nomor = 1
        list_items = []
        
        for id_produk, item in data.keranjang[current_user].items():
            subtotal = item["harga"] * item["jumlah"]
            list_items.append(item)
            table.add_row([
                nomor,
                item['nama'],
                f"Rp {item['harga']:,}",
                item['jumlah'],
                f"Rp {subtotal:,}"
            ])
            nomor += 1
        
        print(table)
        
        total = hitung_total_keranjang_rekursif(list_items)
        
        print(f"{'TOTAL':>10} Rp {total:,}")
        print("=" * 59)
        return total

def cari_produk_dan_tampilkan(keyword):
    print("\n" + "=" * 59)
    print("|                     HASIL PENCARIAN                     |")
    print("=" * 59)
    
    table = PrettyTable()
    table.field_names = ["ID", "Nama Produk", "Kategori", "Harga", "Stok"]
    table.align["ID"] = "c"
    table.align["Nama Produk"] = "l"
    table.align["Kategori"] = "l"
    table.align["Harga"] = "r"
    table.align["Stok"] = "c"
    
    ketemu = False
    for id_produk, produk_data in data.produk.items():
        if keyword.lower() in produk_data['nama'].lower():
            table.add_row([
                id_produk,
                produk_data['nama'],
                produk_data['kategori'],
                f"Rp {produk_data['harga']:,}",
                produk_data['stok']
            ])
            ketemu = True
    
    if ketemu:
        print(table)
    else:
        print("\nProduk tidak ditemukan.")
    print("=" * 59)

def hapus_dari_keranjang():
    print("=" * 38)
    print("|         HAPUS DARI KERANJANG       |")
    print("=" * 38)
    
    if data.user_login not in data.keranjang or len(data.keranjang[data.user_login]) == 0:
        print("\nKeranjang belanja kosong.")
        time.sleep(2)
    else:
        # Menggunakan PrettyTable untuk menampilkan isi keranjang
        table = PrettyTable()
        table.field_names = ["No", "ID", "Nama Produk", "Jumlah"]
        table.align["No"] = "c"
        table.align["ID"] = "c"
        table.align["Nama Produk"] = "l"
        table.align["Jumlah"] = "c"
        
        nomor = 1
        id_list = []
        for id_produk, item in data.keranjang[data.user_login].items():
            table.add_row([
                nomor,
                id_produk,
                item['nama'],
                item['jumlah']
            ])
            id_list.append(id_produk)
            nomor += 1
        
        print(table)
        
        try:
            id_hapus = validasi_input_angka("\nMasukkan ID produk yang ingin dihapus: ", "ID harus berupa angka!")
            if id_hapus is None:
                raise ValueError("Input dibatalkan")
            
            if id_hapus not in data.keranjang[data.user_login]:
                raise KeyError("Produk tidak ada di keranjang!")
            
            konfirmasi = input(f"\nYakin ingin menghapus '{data.keranjang[data.user_login][id_hapus]['nama']}' dari keranjang? (y/n): ")
            if konfirmasi.lower() == "y":
                del data.keranjang[data.user_login][id_hapus]
                print("\nProduk berhasil dihapus dari keranjang!")
            else:
                print("\nPenghapusan dibatalkan.")
            time.sleep(2)
            
        except (ValueError, KeyError) as e:
            print(f"\nError: {e}")
            time.sleep(2)


def checkout():
    print("=" * 59)
    print("|                       CHECKOUT                          |")
    print("=" * 59)
    
    if data.user_login not in data.keranjang or len(data.keranjang[data.user_login]) == 0:
        print("\nKeranjang belanja kosong. Tidak ada yang bisa dicheckout.")
        time.sleep(2)
    else:
        tampilkan_isi_keranjang(data.user_login)
        
        konfirmasi = input("\nLanjutkan checkout? (y/n): ")
        if konfirmasi.lower() == "y":
            # Kurangi stok
            for id_produk, item in data.keranjang[data.user_login].items():
                data.produk[id_produk]["stok"] -= item["jumlah"]
            
            # Kosongkan keranjang
            data.keranjang[data.user_login] = {}
            
            print("\n" + "=" * 59)
            print("|       Checkout berhasil! Terima kasih telah berbelanja!      |")
            print("=" * 59)
            time.sleep(3)
        else:
            print("\nCheckout dibatalkan.")
            time.sleep(2)

def layar_bersih():
    os.system('cls || clear')

def loading(lama=30, waktu=2.5):
    for i in range(lama + 1):
        time.sleep(waktu / lama)
        bar = "=" * i + "-" * (lama - i)
        print(f"\rLoading: [{bar}] {i * 100 // lama}%", end="")
    layar_bersih()
    print("Berhasil memuat.....")
    input("Tekan ENTER untuk lanjut ke menu...")
    layar_bersih()

