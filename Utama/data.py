#Variabel global digunakan untuk menyimpan data pengguna, produk, dan keranjang belanja, serta status login.
# cara bacanya {username: {"password": password, "role": role}}
pengguna = { 
    "gea": {
        "password": "pacar seokjin",
        "role": "admin"
    },
    "user": {
        "password": "user123",
        "role": "user"
    }
}

# cara bacanya: {id: {"nama": nama, "kategori": kategori, "harga": harga, "stok": stok}}
produk = { 
    1: {"nama": "Whiskas 1kg", "kategori": "Makanan", "harga": 50000, "stok": 20},
    2: {"nama": "Royal Canin 2kg", "kategori": "Makanan", "harga": 150000, "stok": 15},
    3: {"nama": "Pasir Gumpal 5kg", "kategori": "Kebersihan", "harga": 45000, "stok": 30},
    4: {"nama": "Sisir Kucing", "kategori": "Grooming", "harga": 25000, "stok": 50},
    5: {"nama": "Mainan Bola", "kategori": "Mainan", "harga": 15000, "stok": 40}
}

# formatnya {username: {id_produk: {"nama": nama, "harga": harga, "jumlah": jumlah}}}
keranjang = {} 

# Variabel yang digunakan untuk ngecek user yang login 
user_login = "" 
role_login = "" 
status_login = False 

# List kategori produk yang valid (Opsional: memudahkan validasi di Functions.py)
KATEGORI_VALID = ["Makanan", "Kebersihan", "Grooming", "Mainan"]