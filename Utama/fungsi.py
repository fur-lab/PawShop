import os
import time
import data
import pwinput
from prettytable import PrettyTable


def tampilkan_header_utama():
    layar_bersih()
    print("=" * 60)
    print("|      SELAMAT DATANG DI TOKO PERALATAN HEWAN PAWSHOP      |")
    print("=" * 60)

def menu_awal():
    print("\n1. Login")
    print("2. Register")
    print("3. Keluar")

def login():
    tampilkan_header_utama()
    print("\n-------------------- LOGIN SECTION -------------------------")
    
    try:
        username = input("Username: ").strip()
        
        # Validasi username tidak boleh kosong
        if not username or username == "":
            raise ValueError("Username tidak boleh kosong!")
        
        password = pwinput.pwinput(prompt="Password: ", mask="*")
        
        # Validasi password tidak boleh kosong
        if not password or password.strip() == "":
            raise ValueError("Password tidak boleh kosong!")
        
        # Verifikasi login
        if username in data.pengguna and data.pengguna[username]["password"] == password:
            data.user_login = username
            data.role_login = data.pengguna[username]["role"]
            data.status_login = True
            
            print(f"\nLogin berhasil! Selamat datang, {username}")
            print(f"Role: {data.role_login}")
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
        username_baru = input("Username baru: ").strip()
        
        # Validasi username tidak boleh kosong atau hanya spasi
        if not username_baru or username_baru == "":
            raise ValueError("Username tidak boleh kosong!")
        
        # Validasi username tidak boleh mengandung spasi
        if ' ' in username_baru:
            raise ValueError("Username tidak boleh mengandung spasi!")
        
        # Validasi username hanya boleh huruf dan angka
        if not username_baru.isalnum():
            raise ValueError("Username hanya boleh mengandung huruf dan angka!")
        
        # Validasi username sudah terdaftar
        if username_baru in data.pengguna:
            raise ValueError("Username sudah terdaftar!")
        
        password_baru = pwinput.pwinput(prompt="Silahkan input password baru: ", mask="*")
        
        # Validasi password tidak boleh kosong
        if not password_baru or password_baru.strip() == "":
            raise ValueError("Password tidak boleh kosong!")
        
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
    print("|                   DAFTAR PRODUK PAW SHOP                |")
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

def cari_produk_dan_tampilkan(keyword):
    print("\n" + "=" * 59)
    print("|                  HASIL PENCARIAN                        |")
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