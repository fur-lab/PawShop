import os
import time



def layar_bersih() :
    os.system("cls")

def loading(lama = 30, waktu = 2.5):
    for i in range(lama + 1):
        time.sleep(waktu / lama)  
        bar = "=" * i + "-" * (lama - i)  
        print(f"\rLoading: [{bar}] {i * 100 // lama}%", end="")
    layar_bersih()
    print("Berhasil memuat.....")
    input("Tekan ENTER untuk lanjut ke menu...")
    layar_bersih()

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
        

def tampilkan_header_utama():
    os.system('cls || clear')
    print("=" * 60)
    print("|      SELAMAT DATANG DI TOKO PERALATAN KUCING WINGKY      |")
    print("=" * 60)

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

