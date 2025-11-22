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

# Fungsi 1 yang gaada parameternya
def tampilkan_header_utama():
    print("=" * 60)
    print("|      SELAMAT DATANG DI TOKO PERALATAN KUCING WINGKY      |")
    print("=" * 60)
