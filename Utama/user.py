import os
import time
from prettytable import PrettyTable

from fungsi import *
from admin import *
from user import *
from data import *

def menu_user() :
        print("=" * 50)
        print(f"|           MENU PELANGGAN - Halo, !             |")
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

def tambah_keranjang():
        while True:  # loop utama untuk tambah barang
                print("=" * 60)
                print("|                   TAMBAH KE KERANJANG                    |")
                print("=" * 60)

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
                                        layar_bersih()
                                        break  # kembali ke atas loop utama
                                elif tambah_lagi == 'n':
                                        print("Kembali ke menu pelanggan...")
                                        time.sleep(1)
                                        return
                                else:
                                        print("Input tidak valid. Silakan masukkan 'y' atau 'n'.")
                                        return  # keluar dari fungsi

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
        print("|                   HASIL PENCARIAN                     |")
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
