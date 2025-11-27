import os
import time
import data
from prettytable import PrettyTable
from admin import *
from fungsi import *
from user import *

def main():
    # Loadingnya hanya sekali pas di awal program
    loading()
    
    while True:
        tampilkan_header_utama()
        menu_awal()
        
        pilihan_utama = input("\nPilih menu (1-3): ")
        
        # Menu Login
        if pilihan_utama == "1":
            layar_bersih()
            berhasil_login = login()
            
            if berhasil_login:
                input("Press enter...")  # Debug pause
                
                # Cek role user setelah login berhasil
                if data.role_login == "admin":
                    # Menu Admin
                    while data.status_login:
                        layar_bersih()
                        menu_admin()
                        
                        pilihan_admin = input("\nPilih menu (1-6): ")
                        
                        if pilihan_admin == "1":
                            layar_bersih()
                            tampilkan_daftar_produk()
                            input("\nTekan ENTER untuk kembali...")
                        
                        elif pilihan_admin == "2":
                            layar_bersih()
                            update()
                            
                        elif pilihan_admin == "3":
                            layar_bersih()
                            edit()
                        
                        
                        elif pilihan_admin == "4":
                            layar_bersih()
                            hapus()
                        
                        elif pilihan_admin == "5":
                            layar_bersih()
                            keyword = input("Masukkan nama produk: ")
                            cari_produk_dan_tampilkan(keyword)

                        elif pilihan_admin == "6":
                            layar_bersih()
                            print("Logout berhasil!")
                            time.sleep(2)
                            data.status_login = False
                            data.user_login = ""
                            data.role_login = ""
                            break
                        
                        else:
                            print("\nPilihan tidak valid!")
                            time.sleep(2)
                
                elif data.role_login == "user":
                    # Menu User
                    while data.status_login:
                        layar_bersih()
                        menu_user()
                        
                        pilihan_user = input("\nPilih menu (1-7): ")
                        
                        if pilihan_user == "1":
                            layar_bersih()
                            tampilkan_daftar_produk()
                            input("\nTekan ENTER untuk kembali...")
                        
                        elif pilihan_user == "2":
                            layar_bersih()
                            cari()
                        
                        elif pilihan_user == "3":
                            layar_bersih()
                            tambah_keranjang()
                        
                        elif pilihan_user == "4":
                            layar_bersih()
                            tampilkan_isi_keranjang(data.user_login)
                            input("\nTekan ENTER untuk kembali...")
                        
                        elif pilihan_user == "5":
                            layar_bersih()
                            hapus_dari_keranjang()
                            time.sleep(2)
                        
                        elif pilihan_user == "6":
                            layar_bersih()
                            checkout()
                            time.sleep(2)
                        
                        elif pilihan_user == "7":
                            layar_bersih()
                            print("Logout berhasil!")
                            time.sleep(2)
                            data.status_login = False
                            data.user_login = ""
                            data.role_login = ""
                            break
                        
                        else:
                            print("\nPilihan tidak valid!")
                            time.sleep(2)
        
        # Menu Register
        elif pilihan_utama == "2":
            layar_bersih()
            register()
        
        # Menu Keluar
        elif pilihan_utama == "3":
            layar_bersih()
            print("=" * 60)
            print("|         Terima kasih telah menggunakan aplikasi!         |")
            print("=" * 60)
            break
        
        else:
            print("\nPilihan tidak valid!")
            time.sleep(2)
            layar_bersih()

if __name__ == "__main__":
    main()

