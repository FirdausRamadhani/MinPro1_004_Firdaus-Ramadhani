usn_mahasiswa = "Mahasiswa"
pw_mahasiswa = "inimahasiswa"

usn_admin = "Admin"
pw_admin = "iniadmin"

semua_pengaduan = []
status = ("Menunggu", "Sedang Diproses", "Selesai")
status_pengaduan = []

while True:
    while True:
        print("\n=== Sistem Pelayanan Pengaduan Mahasiswa ===")
        print("============== Silahkan login ==============")
        print("1. Login")
        print("2. Keluar")
        pilihan = input("Pilih menu (1/2): ")
        if pilihan == "2":
            print("\n=== Terima kasih telah menggunakan sistem pengaduan ===")
            break
        elif pilihan == "1":

            while True:
                username = input("\nMasukkan username: ")
                password = input("Masukkan password: ")

                if username == usn_mahasiswa and password == pw_mahasiswa:
                    print("Login berhasil")
                    role = "mahasiswa"
                    break

                elif username == usn_admin and password == pw_admin:
                    print("Login berhasil")
                    role = "admin"
                    break
                else:
                    print("Username atau password salah. Silakan coba lagi.")  

            if role == "mahasiswa":
                while True:
                    print("\nMenu Mahasiswa:")
                    print("1. Buat Pengaduan")
                    print("2. Status Pengaduan")
                    print("3. Logout")
            
                    pilihan = input("Pilih menu (1/2/3): ")
            
                    if pilihan == "1":
                        pengaduan = input("\nMasukkan pengaduan: ")
                        semua_pengaduan.append(pengaduan)
                        status_pengaduan.append(status[0])
                        print("Pengaduan berhasil ditambahkan.")
                    elif pilihan == "2":
                        print("\n=== Pengaduan Saya ===")
                        if len(semua_pengaduan) == 0 :
                            print("\nBelum ada pengaduan.")
                        else:
                            for i in range(len(semua_pengaduan)):
                                print(str(i + 1) + ". ", semua_pengaduan[i])
                                print("Status : ",status_pengaduan[i])
                    elif pilihan == "3":
                        print("\nAnda telah logout.")
                        break
                    else:
                        print("\nPilihan tidak valid. Silakan coba lagi.")
            
            elif role == "admin":
                while True:
                    print("\nMenu Admin:")
                    print("1. Lihat Semua Pengaduan")
                    print("2. Hapus Pengaduan")
                    print("3. Ubah Status Pengaduan")
                    print("4. Logout")
            
                    pilihan = input("Pilih menu (1/2/3/4): ")
            
                    if pilihan == "1":
                        if semua_pengaduan:
                            print("\nDaftar Pengaduan:")
                            for i in range(len(semua_pengaduan)):
                                print(str(i + 1) + ". ", semua_pengaduan[i])
                                print("Status : ",status_pengaduan[i])
                        else:
                            print("Belum ada pengaduan.")
                    elif pilihan == "2":
                        if semua_pengaduan:
                            print("\nDaftar Pengaduan:")
                            for i in range(len(semua_pengaduan)):
                                print(str(i + 1) + ". ", semua_pengaduan[i])
                            index = int(input("Masukkan nomor pengaduan yang ingin dihapus: ")) - 1
                            if 0 <= index < len(semua_pengaduan):
                                del semua_pengaduan[index]
                                print("Pengaduan berhasil dihapus.")
                            else:
                                print("\nNomor pengaduan tidak valid. Silakan coba lagi.")
                        else:
                            print("\nBelum ada pengaduan.")
                    elif pilihan == "3":
                        if len(semua_pengaduan) == 0:
                            print("\nBelum ada Pengaduan.")
                        else:
                            print("\n=== Ubah Status Pengaduan ===")
                            for i in range(len(semua_pengaduan)):
                                print(str(i + 1) + ". ", semua_pengaduan[i], "-", status_pengaduan[i])

                            nomor = int(input("Pilih nomor pengaduan :"))
                            if nomor < 1 or nomor > len(semua_pengaduan):
                                print("\nPilihan tidak valid. Silakan coba lagi.")
                            else:
                                print("\nPilih Status :")
                                print("1. Sedang Diproses")
                                print("2. Selesai")

                                pilihan_status = input("Pilih status :")
                                if pilihan_status == "1":
                                    status_pengaduan[nomor - 1] = status[1]
                                    print("Status berhasil diubah")
                                elif pilihan_status == "2":
                                    status_pengaduan[nomor - 1] = status[2]
                                    print("Status berhasil diubah")
                                else:
                                    print("\nPilihan tidak valid. Silakan coba lagi.")
                    elif pilihan == "4" :
                        print("\nAnda Telah Logout.")
                        break
                    else:
                        print("\nPilihan tidak valid. Silakan coba lagi.")
    break