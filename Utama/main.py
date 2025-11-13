# # import os
# # import time
# # from prettytable import PrettyTable

# # while True :

# #     loading()
# #     tampilkan_header_utama()
# #     menu_awal()

# #     pilihan_utama = input("Pilih menu (1-3): ")

# #     if pilihan_utama == "1":
# #                 layar_bersih()
# #                 login()
# #                 pilihan_login = input("Pilih menu (1-2): ")

# #                 if pilihan_login == "1" : # Login Admin
# #                     layar_bersih()
# #                     tampilkan_header_utama()
                
# #                     while percobaan < max_percobaan:
# #                             Login_Username = input("Masukkan username Admin : ")
# #                             Login_Password = input("Masukan password Admin : ")


# #                             if Login_Username == Username and Login_Password == Password  :
                
# #                                 Admin = True
# #                                 status_login = True
# #                                 break
                                    

# #                             else:
# #                                 percobaan += 1
# #                                 print("Username atau Password salah !!!")
# #                                 layar_bersih()

# #                                 if percobaan == max_percobaan :
# #                                     layar_bersih()
# #                                     print("Username atau Password salah !!!")
# #                                     input("Tekan Enter untuk memulai dari awal......")
# #                                     break
                    
# #                 if pilihan_login == "2" : # Login User
# #                     layar_bersih()
# #                     tampilkan_header_utama()

# #                     while percobaan < max_percobaan:
# #                         Login_Username = input("Masukkan username : ")
# #                         Login_Password = input("Masukan password : ")


# #                         if Login_Username == pengguna and Login_Password == Password  :
            
# #                             User = True
# #                             status_login = True
# #                             break
                                

# #                         else:
# #                             percobaan += 1
# #                             print("Username atau Password salah !!!")
# #                             layar_bersih()

# #                             if percobaan == max_percobaan :
# #                                 layar_bersih()
# #                                 print("Username atau Password salah !!!")
# #                                 input("Tekan Enter untuk memulai dari awal......")
# #                                 break

#      while Admin == True :
#                     while status_login == True:
#                         layar_bersih()
#                         menu_admin()

#                         pilihan_admin = input("Pilih menu (1-6): ")

#                         if pilihan_admin == "1":   # Lihat menu
#                             layar_bersih()
#                             tampilkan_daftar_produk() # ini pakai prosedur 1
                        
#                         elif pilihan_admin == "2":   # Update
#                             layar_bersih()
#                             update()
                        
#                         elif pilihan_admin == "3":   # Edit
#                             layar_bersih()
#                             edit()

#                         elif pilihan_admin == "4":   # Edit
#                             layar_bersih()
#                             hapus()
                        
#                         elif pilihan_admin == "5":   # Cari
#                             layar_bersih()
#                             print("=" * 59)
#                             print("|                      CARI PRODUK                        |")
#                             print("=" * 59)
#                             keyword = input("Masukkan nama produk: ")
                            
#                             cari_produk_dan_tampilkan(keyword)
                            
#                         elif pilihan_admin == "6":
#                                 layar_bersih()
#                                 print("Logout berhasil!")
#                                 Admin = False
#                                 status_login = False
                        
#                         else:
#                             print("Pilihan tidak valid!")