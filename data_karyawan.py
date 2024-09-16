employees = [
    {'nik': '1001', 'nama': 'Fauzi', 'jabatan': 'Manager', 'umur': 39, 'gaji': 80000},
    {'nik': '1002', 'nama': 'Reihan Jantika', 'jabatan': 'Designer', 'umur': 32, 'gaji': 55000},
    {'nik': '1003', 'nama': 'Mega Sari', 'jabatan': 'Admin Purchasing', 'umur': 40, 'gaji': 60000},
    {'nik': '1004', 'nama': 'Irawan', 'jabatan': 'Analyst', 'umur': 25, 'gaji': 45000},
    {'nik': '1005', 'nama': 'Sisca', 'jabatan': 'Tester', 'umur': 29, 'gaji': 48000}
]

def find_employee_by_nik(nik): #deklarasi fungsi pencarian karyawan berdasarkan NIK
    for emp in employees:
        if emp['nik'] == nik:
            return emp
    return None

def is_valid_nik(nik): #deklarasi fungsi untuk memvalidasi penginputan NIK
    return nik.isdigit() and len(nik) == 4 and not any(emp['nik'] == nik for emp in employees)

def main_menu():
    while True:
        print("\n========================= Data Karyawan Perusahaan XYZ ======================") #Menu Utama
        print("Menu:")
        print("1. Tambah Data Karyawan")
        print("2. Update Data Karyawan")
        print("3. Hapus Data Karyawan")
        print("4. Tampilkan Data Semua Karyawan")
        print("5. Keluar Menu")
        print("\n")

        choice = input("Pilih Menu (1/2/3/4/5): ")

        if choice == '1':
            while True:
                nik = input("Masukkan NIK Karyawan yang ingin ditambahkan: ")
                empnik = is_valid_nik(nik)
                if empnik:
                    try:
                        nama = str(input("Masukkan Nama: "))
                        jabatan = str(input("Masukkan Jabatan: "))
                        while True:
                                umur = int(input("Masukkan Umur: "))
                                if 15 <= umur <=70:
                                    break
                                else:
                                    print("Error! Umur tidak boleh lebih dari 70 & kurang dari 15 tahun!") 
                        gaji = int(input("Masukkan Gaji: "))
                        confirms = input("Sudah sesuai Format! Yakin ingin menambahkan data ini? (Y/N): ").strip().upper()
                        if confirms == 'Y':
                                    employees.append({
                                    'nik': nik,
                                    'nama': nama,
                                    'jabatan': jabatan,
                                    'umur': umur,
                                    'gaji': gaji
                                })
                                    print("Data karyawan berhasil ditambahkan.")
                                    return main_menu()
                        elif confirms == 'N' :
                             print("Penambahan Dibatalkan")
                             break
                        else:
                             print("Pilihan tidak valid.. ketik 'Y' atau 'N'")
                    except :
                            print("Error: Gaji harus berupa angka yang valid")
                else:
                    print("Error: Format NIK tidak sesuai / NIK Sudah ada")
        elif choice == '2':
            while True:
                print("\nMenu Update Karyawan:")
                print("1. Update Data Karyawan")
                print("2. Kembali ke Menu Utama")
				
                Menu_update = input("Pilih opsi (1/2): ")

                if Menu_update == '1':
                    nik = input("Masukkan NIK Karyawan yang ingin diupdate: ")
                    emp = find_employee_by_nik(nik)
                    if emp:
                            print(f"\nData Karyawan yang akan diupdate:")
                            print(f"NIK: {emp['nik']}")
                            print(f"Nama: {emp['nama']}")
                            print(f"Umur: {emp['umur']}")
                            print(f"Jabatan: {emp['jabatan']}")
                            print(f"Gaji: {emp['gaji']}")
                            confirms = input("Lanjutkan mengupdate data ini? (Y/N): ").strip().upper()
                            if confirms == 'Y':
                                try:
                                        print("\nPilih atribut yang ingin diupdate:")
                                        print("1. Nama")
                                        print("2. Umur")
                                        print("3. Jabatan")
                                        print("4. Gaji")
                                        print("5. Selesai")

                                        choice = input("Pilih opsi (1/2/3/4/5): ").strip()
                                        if choice == '1':
                                            new_name = str(input("Masukkan Nama Baru: ")).strip()
                                            emp['nama'] = new_name
                                            if new_name == '':
                                                 print ("Nama tidak boleh kosong.")
                                            else:
                                                print(f"Nama berhasil diperbarui menjadi: {emp['nama']}")
                                        elif choice == '2':
                                            new_age = input("Masukkan Umur Baru: ").strip()
                                            if new_age == '':
                                                print("Umur tidak boleh kosong.")
                                            else:
                                                try:
                                                        new_age = int(new_age)
                                                        if 15 <= new_age <= 70:
                                                            emp['umur'] = new_age
                                                            print(f"Umur berhasil diperbarui menjadi: {emp['umur']}")
                                                        else:
                                                            print("Error: Umur harus dalam rentang 15 hingga 70.")
                                                except ValueError:
                                                         print("Input tidak valid. Masukkan angka yang benar.")
                                        elif choice == '3':
                                            new_position = input("Masukkan Jabatan Baru: ").strip()
                                            emp['jabatan'] = new_position
                                            if new_position == '':
                                                 print ("jabatan tidak boleh kosong.")
                                            else:
                                                print(f"Jabatan berhasil diperbarui menjadi: {emp['jabatan']}")
                                        elif choice == '4':
                                            new_salary = input("Masukkan Gaji Baru: ").strip()
                                            if new_salary == '':
                                                print("Gaji tidak boleh kosong.")
                                            else:
                                                try:
                                                        new_salary = int(new_salary)
                                                        emp['gaji'] = new_salary
                                                        print(f"Gaji berhasil diperbarui menjadi: {emp['gaji']}")
                                                except ValueError:
                                                        print("Input tidak valid. Masukkan angka yang benar.")
                                        elif choice == '5':
                                            print("Update selesai.")
                                            break
                                        else:
                                            print("Pilihan tidak valid. Silakan coba lagi.")
                                except ValueError:
                                     print("Pilihan tidak valid. Silakan coba lagi.")
                            elif confirms == 'N':
                                print("Kembali ke Menu..")
                            else :
                                print("Pilihan tidak valid. Silakan ketik 'Y' atau 'N'.")
                    else:
                        print("Error: NIK tidak ditemukan. Silakan coba lagi.")	
                elif Menu_update == '2':
                            print("Kembali ke Menu Utama...")
                            break
                else:
                        print("Pilihan tidak valid. Silakan pilih opsi yang benar.")
        elif choice == '3':
                while True:
                    print("\nMenu Hapus Karyawan:")
                    print("1. Hapus Data Karyawan")
                    print("2. Kembali ke Menu Utama")

                    Menu_Hapus = input("Pilih opsi (1/2): ")
                    if Menu_Hapus == '1':
                     nik = input("Masukkan NIK Karyawan yang ingin dihapus: ")
                     emp = find_employee_by_nik(nik)
                     if emp:
                            print(f"\nData Karyawan yang akan dihapus:")
                            print(f"NIK: {emp['nik']}")
                            print(f"Nama: {emp['nama']}")
                            confirm = input("Yakin ingin menghapus data ini? (Y/N): ").upper()
                            if confirm == 'Y':
                                employees.remove(emp)
                                print("Data karyawan berhasil dihapus.")
                            elif confirm == 'N':
                                print("Penghapusan data dibatalkan.")
                            else:
                                print("Pilihan tidak valid. Silakan ketik 'Y' atau 'N'.")
                     else:
                        print("Error: NIK tidak ditemukan. Silakan coba lagi.")
                    elif Menu_Hapus == '2':
                            print("Kembali ke Menu Utama...")
                            break
                    else:
                        print("Pilihan tidak valid. Silakan pilih opsi yang benar.")
        elif choice == '4':
            while True:
                print("\nTampilan Data Karyawan:")
                print("1. Tampilkan Semua Karyawan")
                print("2. Cari Karyawan Berdasarkan NIK")
                print("3. Kembali ke Menu Utama")
        
                choice = input("Pilih opsi (1/2/3): ")
        
                if choice == '1':
                    if not employees:
                        print("Daftar karyawan kosong. Tambahkan Data Karyawan di Main Menu")
                    else:
                        for emp in employees:
                             print(f"NIK: {emp['nik']}, Nama: {emp['nama']}, Jabatan: {emp['jabatan']}, Umur: {emp['umur']}, Gaji: {emp['gaji']}")
                elif choice == '2':
                    nik = input("Masukkan NIK Karyawan yang ingin dicari: ")
                    emp = find_employee_by_nik(nik)
                    if emp:
                        print(f"NIK: {emp['nik']}"), 
                        print(f"Nama: {emp['nama']}")
                        print(f"Jabatan: {emp['jabatan']}")
                        print(f"Umur: {emp['umur']}")
                        print(f"Gaji: {emp['gaji']}")
                    else:
                        print("Error: NIK tidak ditemukan. Masukan NIK yang valid")
                elif choice == '3':
                    print("Kembali ke Menu Utama...")
                    break
                else:
                    print("Pilihan tidak valid. Silakan pilih opsi yang benar.")
        elif choice == '5':
            print("Keluar dari menu.")
            print("\nTerima kasih sudah menggunakan program ini.\n")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

main_menu()
