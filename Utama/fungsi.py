import os
import time
import pwinput
from prettytable import PrettyTable
from data import *

def tampilkan_header_utama():
    os.system('cls || clear')
    print("=" * 60)
    print("|      SELAMAT DATANG DI TOKO PERALATAN KUCING WINGKY      |")
    print("=" * 60)

def main():
    global user_login, role_login, status_login

##### TAMPILAN AWAL #####
def menu_awal():
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

def login() :
        print("=" * 50)
        print(f"|               MENU LOGIN              |")
        print("=" * 50)
        print("1. Admin")
        print("2. User")
        

def register () :
        print("\n-------------------- REGISTER SECTION ----------------------")
        
        try:
            username_baru = input("Username baru: ")
            if not username_baru:
                raise ValueError("Username tidak boleh kosong")
            
            if username_baru in pengguna:
                raise ValueError("Username sudah terdaftar!")
            
            password_baru = pwinput.pwinput(prompt="Silahkan input password baru: ", mask="*") # Menggunakan passwordnya
            if not password_baru:
                raise ValueError("Password tidak boleh kosong")
            
            pengguna[username_baru] = {
                "password": password_baru,
                "role": "user"
            }
            
            print(f"\nRegistrasi berhasil! Silakan login dengan username '{username_baru}'")
            time.sleep(4)
            
        except ValueError as e:
            print(f"\nError: {e}")
            time.sleep(4)

def menu_user() :
        print("=" * 50)
        print(f"|           MENU PELANGGAN - Halo, !          |")
        print("=" * 50)
        print("\n1. Lihat Semua Produk")
        print("2. Cari Produk")
        print("3. Tambah ke Keranjang")
        print("4. Lihat Keranjang")
        print("5. Hapus dari Keranjang")
        print("6. Checkout")
        print("7. Logout")

def validasi_input_angka(prompt, pesan_error="Input harus berupa angka!"):
    while True:
        try:
            input_str = input(prompt) #ini variabel lokal 
            if not input_str:
                return None
            hasil = int(input_str) #ini variabel lokal 
            return hasil
        except ValueError:
            print(f"\n{pesan_error}")
            time.sleep(4)
            return None

def hitung_total_keranjang_rekursif(list_items, index=0):
    if index >= len(list_items): #base case
        return 0
    
    item_sekarang = list_items[index]
    subtotal = item_sekarang["harga"] * item_sekarang["jumlah"]
    return subtotal + hitung_total_keranjang_rekursif(list_items, index + 1) #fungsi rekursif

def generate_id_produk_baru():
    if len(produk) == 0:
        id_baru = 1
    else:
        id_baru = max(produk.keys()) + 1
    return id_baru

def tampilkan_daftar_produk(): #prosedur 1
    print("\n" + "=" * 59)
    print("|                   DAFTAR PRODUK WINGKY                  |")
    print("=" * 59)
    
    if len(produk) == 0:
        print("Tidak ada produk tersedia.")
    else:
        table = PrettyTable()
        table.field_names = ["ID", "Nama Produk", "Kategori", "Harga", "Stok"]
        table.align["ID"] = "c"
        table.align["Nama Produk"] = "l"
        table.align["Kategori"] = "l"
        table.align["Harga"] = "r"
        table.align["Stok"] = "c"
        
        for id_produk, data in produk.items(): #ini variabel lokal yang ada dalam loop
            table.add_row([
                id_produk,
                data['nama'],
                data['kategori'],
                f"Rp {data['harga']:,}",
                data['stok']
            ])
        
        print(table)
    
    print("=" * 59)

def tambah_keranjang () :
                print("=" * 59)
                print("|                  TAMBAH KE KERANJANG                    |")
                print("=" * 59)
                
                # Menggunakan PrettyTable untuk menampilkan list produk
                table = PrettyTable()
                table.field_names = ["ID", "Nama Produk", "Kategori", "Harga", "Stok"]
                table.align["ID"] = "c"
                table.align["Nama Produk"] = "l"
                table.align["Kategori"] = "l"
                table.align["Harga"] = "r"
                table.align["Stok"] = "c"
                
                for id_produk, data in produk.items():
                        table.add_row([
                                id_produk,
                                data['nama'],
                                data['kategori'],
                                f"Rp {data['harga']:,}",
                                data['stok']
                        ])
                
                print(table)
                
                try:
                        global keranjang
                
                        id_beli = validasi_input_angka("\nMasukkan ID produk yang ingin dibeli: ", "ID harus berupa angka!")
                        if id_beli is None:
                                raise ValueError("Input dibatalkan")
                        
                        if id_beli not in produk:
                                raise KeyError("Produk dengan ID tersebut tidak ditemukan!")
                        
                        jumlah_beli = validasi_input_angka("Jumlah: ", "Jumlah harus berupa angka!")
                        if jumlah_beli is None or jumlah_beli <= 0:
                                raise ValueError("Jumlah harus lebih dari 0")
                        
                        if jumlah_beli > produk[id_beli]["stok"]:
                                raise ValueError(f"Stok tidak cukup! Stok tersedia: {produk[id_beli]['stok']}")
                        
                        # Inisialisasi keranjang user jika belum ada
                        if user_login not in keranjang:
                                keranjang[user_login] = {}
                        
                        # Tambah ke keranjang
                        if id_beli in keranjang[user_login]:
                                keranjang[user_login][id_beli]["jumlah"] += jumlah_beli
                        else:
                                keranjang[user_login][id_beli] = {
                                "nama": produk[id_beli]["nama"],
                                "harga": produk[id_beli]["harga"],
                                "jumlah": jumlah_beli
                                }
                        
                        print(f"\n{produk[id_beli]['nama']} (x{jumlah_beli}) berhasil ditambahkan ke keranjang!")
                        time.sleep(4)
                        print("=" * 59)
                
                except (ValueError, KeyError) as e:
                        print(f"\nError: {e}")
                        print("=" * 59)
                        time.sleep(4)

def tampilkan_isi_keranjang(current_user): #prosedur ke 2
    global keranjang
    
    print("=" * 59)
    print("|                   KERANJANG BELANJA                     |")
    print("=" * 59)
    
    if current_user not in keranjang or len(keranjang[current_user]) == 0:
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
        
        nomor = 1 #ini variabel lokal 
        list_items = [] #ini variabel lokal 
        
        for id_produk, item in keranjang[current_user].items(): #ini ada pakai variabel lokal 
            subtotal = item["harga"] * item["jumlah"] #ini ada pakai variabel lokal 
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
        
        #fungsi rekursif untuk hitung total
        total = hitung_total_keranjang_rekursif(list_items) #ini ada pakai variabel lokal 
        
        print(f"{'TOTAL':>10} Rp {total:,}")
        print("=" * 59)
        return total

# Fungsi khusus untuk pencarian produk (fitur buat mempermudah cari produk)
def cari_produk_dan_tampilkan(keyword):
    print("\n" + "=" * 59)
    print("|                     HASIL PENCARIAN                     |")
    print("=" * 59)
    
    # Menggunakan PrettyTable untuk menampilkan hasil pencarian
    table = PrettyTable()
    table.field_names = ["ID", "Nama Produk", "Kategori", "Harga", "Stok"]
    table.align["ID"] = "c"
    table.align["Nama Produk"] = "l"
    table.align["Kategori"] = "l"
    table.align["Harga"] = "r"
    table.align["Stok"] = "c"
    
    ketemu = False
    for id_produk, data in produk.items():
        if keyword.lower() in data['nama'].lower():
            table.add_row([
                id_produk,
                data['nama'],
                data['kategori'],
                f"Rp {data['harga']:,}",
                data['stok']
            ])
            ketemu = True
    
    if ketemu:
        print(table)
    else:
        print("\nProduk tidak ditemukan.")
    print("=" * 59)

def layar_bersih():
    os.system('cls')

def loading(lama = 30, waktu = 2.5):
    for i in range(lama + 1):
        time.sleep(waktu / lama)  
        bar = "=" * i + "-" * (lama - i)  
        print(f"\rLoading: [{bar}] {i * 100 // lama}%", end="")
    layar_bersih()
    print("Berhasil memuat.....")
    input("Tekan ENTER untuk lanjut ke menu...")
    layar_bersih()

