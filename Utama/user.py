import os
import time
from prettytable import PrettyTable

from fungsi import *
from admin import *
from user import *
from data import *

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
