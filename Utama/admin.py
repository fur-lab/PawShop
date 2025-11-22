from prettytable import PrettyTable
from fungsi import *
import data
import time

def menu_admin():
    print("=" * 50)
    print(f"|            MENU ADMIN - Halo, Admin!             |")
    print("=" * 50)
    print("1. Lihat Semua Produk")
    print("2. Tambah Produk")
    print("3. Update Produk")
    print("4. Hapus Produk")
    print("5. Cari Produk")
    print("6. Logout")

def update():
    print("=" * 50)
    print("|                TAMBAH PRODUK                   |")
    print("=" * 50)
    
    try:
        nama = input("Nama produk: ")
        if not nama:
            raise ValueError("Nama tidak boleh kosong")
        
        kategori = input("Kategori: ")
        if not kategori:
            raise ValueError("Kategori tidak boleh kosong")
        
        harga = validasi_input_angka("Harga: ", "Harga harus berupa angka!")
        if harga is None or harga <= 0:
            raise ValueError("Harga harus lebih dari 0")
        
        stok = validasi_input_angka("Stok: ", "Stok harus berupa angka!")
        if stok is None or stok < 0:
            raise ValueError("Stok tidak boleh negatif")
        
        id_baru = generate_id_produk_baru()
        data.produk[id_baru] = {
            "nama": nama,
            "kategori": kategori,
            "harga": harga,
            "stok": stok
        }
        
        print(f"\nProduk '{nama}' berhasil ditambahkan dengan ID {id_baru}!")
        time.sleep(2)
    
    except ValueError as e:
        print(f"\nError: {e}")
        time.sleep(2)

def edit():
    print("=" * 50)
    print("|                UPDATE PRODUK                   |")
    print("=" * 50)
    
    table = PrettyTable()
    table.field_names = ["ID", "Nama Produk"]
    table.align["ID"] = "c"
    table.align["Nama Produk"] = "l"
    
    for id_produk, produk_data in data.produk.items():
        table.add_row([id_produk, produk_data['nama']])
    
    print(table)
    
    try:
        id_update = validasi_input_angka("\nMasukkan ID produk yang ingin diupdate: ", "ID harus berupa angka!")
        if id_update is None:
            raise ValueError("Input dibatalkan")
        
        if id_update not in data.produk:
            raise KeyError("Produk dengan ID tersebut tidak ditemukan!")
        
        print(f"\nProduk ditemukan: {data.produk[id_update]['nama']}")
        print("\nPilih yang ingin diupdate:")
        print("1. Nama")
        print("2. Kategori")
        print("3. Harga")
        print("4. Stok")
        pilih = input("Pilihan: ")

        if pilih == "1":
            nama_baru = input("Nama baru: ")
            if not nama_baru:
                raise ValueError("Nama tidak boleh kosong")
            data.produk[id_update]["nama"] = nama_baru
            print("\nNama produk berhasil diupdate!")
        elif pilih == "2":
            kategori_baru = input("Kategori baru: ")
            if not kategori_baru:
                raise ValueError("Kategori tidak boleh kosong")
            data.produk[id_update]["kategori"] = kategori_baru
            print("\nKategori produk berhasil diupdate!")
        elif pilih == "3":
            harga_baru = validasi_input_angka("Harga baru: ", "Harga harus berupa angka!")
            if harga_baru is None or harga_baru <= 0:
                raise ValueError("Harga harus lebih dari 0")
            data.produk[id_update]["harga"] = harga_baru
            print("\nHarga produk berhasil diupdate!")
        elif pilih == "4":
            stok_baru = validasi_input_angka("Stok baru: ", "Stok harus berupa angka!")
            if stok_baru is None or stok_baru < 0:
                raise ValueError("Stok tidak boleh negatif")
            data.produk[id_update]["stok"] = stok_baru
            print("\nStok produk berhasil diupdate!")
        else:
            print("\nPilihan tidak valid!")
        time.sleep(2)
    
    except (ValueError, KeyError) as e:
        print(f"\nError: {e}")
        time.sleep(2)

def hapus():
    print("=" * 50)
    print("|                 HAPUS PRODUK                   |")
    print("=" * 50)
    
    table = PrettyTable()
    table.field_names = ["ID", "Nama Produk"]
    table.align["ID"] = "c"
    table.align["Nama Produk"] = "l"
    
    for id_produk, produk_data in data.produk.items():
        table.add_row([id_produk, produk_data['nama']])
    
    print(table)
    
    try:
        id_hapus = validasi_input_angka("\nMasukkan ID produk yang ingin dihapus: ", "ID harus berupa angka!")
        if id_hapus is None:
            raise ValueError("Input dibatalkan")
        
        if id_hapus not in data.produk:
            raise KeyError("Produk dengan ID tersebut tidak ditemukan!")
        
        konfirmasi = input(f"\nYakin ingin menghapus '{data.produk[id_hapus]['nama']}'? (y/n): ")
        if konfirmasi.lower() == "y":
            del data.produk[id_hapus]
            print("\nProduk berhasil dihapus!")
        else:
            print("\nPenghapusan dibatalkan.")
        time.sleep(2)
        
    except (ValueError, KeyError) as e:
        print(f"\nError: {e}")
        time.sleep(2)