phone_number_list = [
    {"nama" : "Syahid Ahmad", "noTelepon" : "085717117166", "keterangan" : "Penghuni Kamar 110 ", "alamat" : "Rusun TB 02", "email" : "syahidamd26@gmail.com", "emergency" : "No"},
    {"nama" : "Novaldy Yesaya", "noTelepon" : "08223451233", "keterangan" : "Penjual Galon", "alamat"  :"Rusun BPJS Kabil", "email" : "-", "emergency" : "No"},
    {"nama" : "Handika", "noTelepon" : "112233445566", "keterangan" : "Maintainance Rusun ", "alamat" : "Rusun BPJS Kabil", "email" : "ekihandika@gmail.com",  "emergency" : "No"},
    {"nama" : "Alfi Rafi", "noTelepon" : "07787100011", "keterangan" : "Pemadam Kebakaran", "alamat" : "Jl Patimura", "email" : "pemadam_kabil@gmail.com", "emergency" : "Yes"},
    {"nama" : "Rifat Rahmad", "noTelepon" : "07787491000", "keterangan" : "Polsek Nongsa", "alamat" : "Jln Kavling Senjulung", "email" : "polseknongsa@gmail.com", "emergency" : "Yes"},
    {"nama" : "Ahmad Atang", "noTelepon" : "0888888888888", "keterangan" : "Soto Ayam", "alamat" : "Jl Raya Pelabuhan", "email" : "-", "emergency" : "No"},
    {"nama" : "Junior Robertlewandowski", "noTelepon" : "223344556677", "keterangan" : "Penghuni Kamar 113", "alamat":"Rusun TB 02", "email" : "robertjunior@yahoo.com", "emergency" : "No"},
    {"nama" : "Rudi Saptaji", "noTelepon" : "08123123123", "keterangan" : "Soto Kudus", "alamat" : "Jln Hang Kesturi", "email" : "-",  "emergency" : "No"},
    {"nama" : "Ros Nalfisah", "noTelepon" : "0778711960", "keterangan" : "Rumah Sakit Soedarsono", "alamat" : "Jl Hang Kesturi 2", "email" : "rssudarsono@ymail.com", "emergency" : "Yes"},
    {"nama" : "Beti Sukati", "noTelepon" : "334455667788", "keterangan" : "Ayam Bakar Bu Beti", "alamat" : "Jl Hang Kesturi", "email" : "bubetibakaran@gmail.com ", "emergency" : "No"},
]

backup_data = []


def display_menu():
    print('''
Selamat Datang di Yellow Pages Rusun BPJS Kabil

    List Menu :
    1. Menampilkan daftar nomor telepon
    2. Menambah data nomor telepon baru
    3. Memperbarui data nomor telepon
    4. Menghapus data nomor telepon
    5. Mencari data nomor telepon
    6. Daftar Nomor telepon darurat
    7. Menghapus semua atau mengembalikan data nomor telepon
    8. Exit program
''')

def display_read():
    print("""
Menampilkan Daftar Nomor Telepon

    List Menu :
    1. Menampilkan semua daftar nomor telepon
    2. Cek detail informasi berdasarkan nomor telepon
    3. Kembali ke menu utama
""")

def display_add():
    print("""
Menambah Data Nomor Telepon Baru

    List Menu :
    1. Menambahkan nomor telepon baru
    2. Kembali ke menu utama
""")

def display_update():
    print("""
Memperbarui Daftar Nomor Telepon

    List Menu :
    1. Memperbarui daftar nomor telepon
    2. Kembali ke menu utama
""")

def display_delete():
    print("""
Menghapus Data Nomor Telepon
    
    List Menu :
    1. Menghapus data pada daftar nomor telepon
    2. Kembali ke menu utama
""")

def display_option_update():
    print("""
Input Menu Kolom yang Ingin Diperbarui :

    - Nama
    - Nomor
    - Keterangan
    - Alamat
    - Email
    - Darurat
""")

def display_search():
    print("""
Mencari Data Nomor Telepon

    List Menu :
    1. Mencari data berdasarkan suatu kata
    2. Kembali ke menu utama
""")

def display_emergency():
    print("""
Daftar Nomor Telepon Darurat

    List Menu :
    1. Melihat daftar kontak darurat
    2. Kembali ke menu utama
""")

def display_clear_n_backup():
    print("""
Menghapus Semua atau Mengembalikan Data Nomor Telepon
    
    List Menu :
    1. Menghapus semua data
    2. Mengembalikan data yang telah dihapus
    3. Kembali ke menu utama
""")


def display(data):
    print("\nDaftar Nomor Telepon Rusun BPJS Kabil\n")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("No. | Nama                             | Nomor Telepon    | Keterangan                       | Alamat                           | Email                            | Emergency |")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for no in range(len(data)):
        length_no = 3 - len(str(no+1))
        number = str(no+1) + " "*length_no
        length_name = 32 - len(data[no]["nama"])
        name = data[no]["nama"] + " "*length_name
        length_phone_number = 16 - len(data[no]["noTelepon"])
        phone_number = data[no]["noTelepon"] + " "*length_phone_number
        length_information = 32 - len(data[no]["keterangan"])
        information = data[no]["keterangan"] + " "*length_information
        length_address = 32 - len(data[no]["alamat"])
        address = data[no]["alamat"] + " "*length_address
        length_email = 32 - len(data[no]["email"])
        email = data[no]["email"] + " "*length_email
        length_emergency = 9 - len(data[no]["emergency"])
        emergency = data[no]["emergency"] + " "*length_emergency
        print(f'{number} | {name} | {phone_number} | {information} | {address} | {email} | {emergency} |')
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

def user_display(data):
    print("\nDaftar Nomor Telepon Rusun BPJS Kabil\n")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("No. | Nama                             | Nomor Telepon    | Keterangan                       | Alamat                           | Email                            |")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for no in range(len(data)):
        length_no = 3 - len(str(no+1))
        number = str(no+1) + " "*length_no
        length_name = 32 - len(data[no]["nama"])
        name = data[no]["nama"] + " "*length_name
        length_phone_number = 16 - len(data[no]["noTelepon"])
        phone_number = data[no]["noTelepon"] + " "*length_phone_number
        length_information = 32 - len(data[no]["keterangan"])
        information = data[no]["keterangan"] + " "*length_information
        length_address = 32 - len(data[no]["alamat"])
        address = data[no]["alamat"] + " "*length_address
        length_email = 32 - len(data[no]["email"])
        email = data[no]["email"] + " "*length_email
        print(f'{number} | {name} | {phone_number} | {information} | {address} | {email} |')
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")


def yellow_pages():
    while(True):
        display_menu()
        menu_option = input("Masukan angka menu yang ingin dijalankan : ")
        if (menu_option == "1"):
            menu_read()

        elif (menu_option == "2"):
            menu_add()

        elif (menu_option == "3"):
            menu_update()

        elif (menu_option == "4"):
            menu_delete()

        elif (menu_option == "5"):
            menu_search()

        elif (menu_option == "6"):
            menu_emergency()

        elif (menu_option == "7"):
            menu_clear_n_backup()

        elif (menu_option == "8"):
            menu_exit()
            break

        else:
            print("--------------------------------------")
            print("Opsi menu yang dipilih tidak benar.\nSilahkan masukan opsi sesuai list menu")
            print("--------------------------------------")


def menu_read():
    while(True):
        display_read()
        option_in_read = input("Masukan angka menu yang ingin dijalankan : ")
        if option_in_read == "1" :
            if len(phone_number_list) == 0:
                print("---------------------")
                print("Daftar telepon kosong")
                print("---------------------")
            else: 
                display(phone_number_list)

        elif option_in_read == "2" :
            phone_number = input("Masukan nomor telepon untuk mengetahui detail informasi : ")
            if len(phone_number_list) == 0:
                print("---------------------")
                print("Daftar telepon kosong")
                print("---------------------")
            elif phone_number.isnumeric() == False or (len(phone_number)<10) or (len(phone_number) > 13) :
                print("----------------------------------------------------------")
                print("Nomor telepon harus berupa angka dan berjumlah 10-13 digit")
                print("----------------------------------------------------------")
            else:
                primary_key=[]
                for no in range(len(phone_number_list)):
                    if phone_number_list[no]["noTelepon"] == phone_number:
                        primary_key.append(phone_number_list[no])
                        break
                if len(primary_key) != 0:
                    display(primary_key)
                else: 
                    print("-----------------------------")
                    print("Nomor telepon belum terdaftar")
                    print("-----------------------------")

        elif option_in_read == "3":
            break

def menu_add():
    while(True):
        display_add()
        option_in_add = input("Masukan angka menu yang ingin dijalankan : ")    
        if option_in_add == "1":    
            while (True):
                back_to_menu_add = False
                all_data_entered = False
                add_number = input(f"Masukan nomor telepon : ")
                if (add_number.isnumeric() == False) or (len(add_number) < 10) or (len(add_number) > 13):
                    print("Nomor telepon harus berupa angka dan berjumlah 10-13 digit")
                else:
                    primary_key = []
                    for no in range(len(phone_number_list)):
                        if phone_number_list[no]["noTelepon"] == add_number:
                            primary_key.append(phone_number_list[no]["noTelepon"])    
                    if len(primary_key) != 0 :
                        print("-----------------------------")
                        print("Nomor telepon telah terdaftar")
                        print("-----------------------------")
                        break
                    else:
                        while (True):
                            add_first_name = input("Masukan nama depan : ").capitalize()
                            if add_first_name.isalpha() == False or len(add_first_name) > 16:
                                print("Nama depan harus berupa alfabet (a-z) dan maksimal 16 karakter")
                            else:
                                break

                        while (True):
                            add_last_name = input("Masukan nama belakang : ").capitalize()
                            if add_last_name == "-":
                                add_last_name = ""
                                break
                            elif add_last_name.isalpha() == False or len(add_last_name) > 16:
                                print("Nama belakang harus berupa alfabet (a-z) dan maksimal 16 karakter.\nIsi dengan \"-\" apabila tidak ada nama belakang")
                            else:
                                break

                        while (True):
                            add_information = input("Masukan keterangan terkait nomor telepon : ").strip()
                            if len(add_information) > 32 or add_information == "":
                                print("Apabila tidak ada keterangan, bisa diisi \"-\" dan maksimal 32 karakter")
                            else:
                                break

                        while (True):
                            add_address = input("Masukan alamat : ").strip()
                            if len(add_address) > 32  or add_address == "":
                                print("Apabila tidak mengetahui alamat, bisa diisi \"-\" dan maksimal 32 karakter")
                            else:
                                break

                        while (True):
                            add_email = input("Masukan alamat email : ").strip()
                            if add_email == "-":
                                break
                            elif (len(add_email) > 32)  or (add_email == "") or ("@" not in add_email) or (" " in add_email) :
                                print("Apabila tidak mengetahui email, bisa diisi \"-\".\nJangan lupa untuk email gunakan \"@\" dan maksimal 32 karakter")
                            else:
                                break

                        while (True):
                            add_emergency = input("Apakah kontak ini merupakan nomor darurat? (\"Yes\" / \"No\") : ").capitalize()
                            if add_emergency != "Yes" and add_emergency != "No":
                                print("Hanya dapat diisi \"Yes\" / \"No\"")
                            elif add_emergency == "Yes" or add_emergency == "No":
                                all_data_entered = True
                                break    
                        new_list_phone_number = [{"nama": add_first_name+" "+add_last_name , "noTelepon": add_number, "keterangan" : add_information , "alamat" : add_address , "email": add_email , "emergency" : add_emergency }]
                        display(new_list_phone_number)

                        while (True):
                            save_data = input("\nApakah data ingin disimpan? (\"Yes\" / \"No\") : ").capitalize()
                            if save_data != "Yes" and save_data != "No":
                                print("hanya dapat memilih (\"Yes\" / \"No\")")
                            elif save_data == "No":
                                back_to_menu_add = True
                                break
                            elif save_data == "Yes":
                                phone_number_list.extend(new_list_phone_number)
                                print("-----------------------------------------------")
                                print("Data nomor telepon baru telah berhasil disimpan")
                                print("-----------------------------------------------")
                                break
                        if all_data_entered == True:
                            break
                        elif back_to_menu_add == True:
                            break
        elif option_in_add == "2":
            break    

def menu_update():
    while(True):
        display_update()
        option_in_update = input("Masukan angka menu yang ingin dijalankan : ")    
        if option_in_update == "1":
            back_to_menu_update = False
            data_updated = False
            phone_number = input(f"Masukan nomor telepon untuk memperbarui data : ")
            if phone_number.isnumeric() == False or (len(phone_number) < 10) or (len(phone_number) > 13):
                print("----------------------------------------------------------")
                print("Nomor telepon harus berupa angka dan berjumlah 10-13 digit")
                print("----------------------------------------------------------")
            else:
                value_update = []
                no_list = 0
                for no in range(len(phone_number_list)):
                    if phone_number_list[no]["noTelepon"] == phone_number:
                        value_update.append(phone_number_list[no].copy()) 
                        no_list = no
                if len(value_update)==0:
                        print("-----------------------------")
                        print("Nomor telepon tidak terdaftar")
                        print("-----------------------------") 
                else: 
                    display(value_update)
                    while (True):
                        update_option = input("\nApakah Anda ingin melanjutkan untuk memperbarui data? (\"Yes\" / \"No\") : ").capitalize()
                        if update_option != "Yes" and update_option != "No":
                            print("hanya dapat memilih \"Yes\" / \"No\"")
                        elif update_option == "No":
                            back_to_menu_update = True
                            break
                        elif update_option == "Yes":
                            break

                    if back_to_menu_update == True:
                        continue
                    else:
                        display_option_update()
                        while (True):
                            option_update = input("Masukan kolom yang ingin diperbarui : ").capitalize() 
                            update_key = ""
                            new_data = ""
                            if option_update not in ["Nama","Nomor","Keterangan","Alamat","Email","Darurat"] :
                                display_option_update()
                                print("Input berdasarkan salah satu kolom di atas") 

                            elif option_update == "Nama":
                                update_key = "nama"
                                while (True):
                                    new_first_name = input(f"Nama sebelumnya \"{value_update[0][update_key].strip()}\", Masukan nama depan baru : ").capitalize()
                                    if new_first_name.isalpha() == False or len(new_first_name) > 16:
                                        print("Nama depan harus berupa alfabet (a-z) dan maksimal 16 karakter")
                                    else:
                                        break
                                while (True):
                                    new_last_name = input("Masukan nama belakang baru : ").capitalize()
                                    if new_last_name == "-" :
                                        new_last_name = ""
                                        new_data = new_first_name + " " + new_last_name
                                        value_update[0][update_key] = new_data
                                        break
                                    elif new_last_name.isalpha() == False or len(new_last_name) > 16:
                                        print("Nama belakang harus berupa alfabet (a-z) dan maksimal 16 karakter.\nIsi dengan \"-\" apabila tidak ada nama belakang")
                                    else:
                                        new_data = new_first_name + " " + new_last_name
                                        value_update[0][update_key] = new_data
                                        break

                            elif option_update == "Nomor":
                                update_key = "noTelepon"
                                while (True):
                                    new_number = input(f"Nomor telepon sebelumnya \"{value_update[0][update_key].strip()}\", Masukan nomer telepon baru : ")
                                    primary_key=[]
                                    if new_number.isnumeric() == False or (len(new_number) < 10) or (len(new_number) > 13):
                                        print("Nomor telepon harus angka dan berjumlah 10-13 digit")
                                    else:    
                                        for no in range(len(phone_number_list)):
                                            if phone_number_list[no]["noTelepon"] == new_number:
                                                primary_key.append(phone_number_list[no]["noTelepon"])    
                                        if len(primary_key) != 0 :
                                            print("Nomor telepon telah terdaftar. Silahkan masukan nomor telepon lain")
                                        else:
                                            new_data = new_number
                                            value_update[0][update_key] = new_data
                                            break

                            elif option_update == "Keterangan":
                                while (True):
                                    update_key = "keterangan"
                                    new_information = input(f"Keterangan sebelumnya \"{value_update[0][update_key].strip()}\", Masukan keterangan baru : ").strip()
                                    if len(new_information) > 32 or new_information == "":
                                        print("Apabila tidak ada keterangan, bisa diisi \"-\" dan maksimal 32 karakter")
                                    else:
                                        new_data = new_information
                                        value_update[0][update_key] = new_data
                                        break

                            elif option_update == "Alamat":
                                while (True):
                                    update_key = "alamat"
                                    new_address = input(f"Alamat sebelumnya \"{value_update[0][update_key].strip()}\", Masukan alamat baru : ").strip()
                                    if len(new_address) > 32  or new_address == "":
                                        print("Apabila tidak mengetahui alamat, bisa diisi \"-\" dan maksimal 32 karakter")
                                    else:
                                        new_data = new_address
                                        value_update[0][update_key] = new_data
                                        break

                            elif option_update == "Email":
                                while (True):
                                    update_key = "email"
                                    new_email = input(f"Email sebelumnya \"{value_update[0][update_key].strip()}\", Masukan email baru : ")
                                    if new_email == "-":
                                        new_data = new_email
                                        value_update[0][update_key] = new_data
                                        break
                                    elif (len(new_email) > 32)  or (new_email == "") or ("@" not in new_email) or (" " in new_email):
                                        print("Apabila tidak mengetahui email, bisa diisi \"-\".\nJangan lupa untuk email gunakan \"@\" dan maksimal 32 karakter")
                                    else:
                                        new_data = new_email
                                        value_update[0][update_key] = new_data
                                        break
                                        
                            elif option_update == "Darurat":
                                while (True):
                                    update_key = "emergency"
                                    new_emergency = input(f"Nomor merupakan nomor darurat ? Sebelumnya :\"{value_update[0][update_key].strip()}\" Masukan keterangan nomor darurat baru (\"Yes\" / \"No\") : ").capitalize()
                                    if new_emergency != "Yes" and new_emergency != "No":
                                        print("Hanya dapat diisi (\"Yes\" or \"No\")")
                                    elif new_emergency == "Yes" or new_emergency == "No":
                                        new_data = new_emergency
                                        value_update[0][update_key] = new_data
                                        break

                            if len(new_data) != 0:
                                display(value_update)
                                while (True):    
                                    save_new_data = input("\nApakah data baru ingin disimpan? (\"Yes\" / \"No\") : ").capitalize()
                                    if save_new_data != "Yes" and save_new_data != "No":
                                        print("hanya dapat memilih \"Yes\" / \"No\"")
                                    elif save_new_data == "No":
                                        back_to_menu_update = True
                                        break
                                    elif save_new_data == "Yes":
                                        phone_number_list[no_list] = value_update[0]
                                        data_updated = True
                                        print("----------------------------------------------------")
                                        print("Memperbarui data telah berhasil, data telah disimpan")
                                        print("----------------------------------------------------")
                                        break   
                                if back_to_menu_update == True:
                                    break
                                elif data_updated == True:
                                    break        

        elif option_in_update == "2":
            break

def menu_delete():
    while(True):
        display_delete()
        option_in_del = input("Masukan angka menu yang ingin dijalankan : ")
        if option_in_del == "1" :
            phone_number = input(f"Masukan nomor telepon untuk menghapus data pada daftar telepon : ")
            if (phone_number.isnumeric() == False) or (len(phone_number) > 13) or (len(phone_number) < 10):
                print("----------------------------------------------------------")
                print("Nomor telepon harus berupa angka dan berjumlah 10-13 digit")
                print("----------------------------------------------------------")
                continue
            else:
                delete_value = []
                no_list = 0
                for no in range(len(phone_number_list)):
                    if phone_number_list[no]["noTelepon"] == phone_number:
                        delete_value.append(phone_number_list[no]) 
                        no_list = no
                        break
                if len(delete_value) == 0:
                        print("-----------------------------------------------")
                        print("Nomor telepon yang anda masukan tidak terdaftar")
                        print("-----------------------------------------------")
                        continue
                else: 
                    display(delete_value)
                    while (True):
                        delete_option = input("\nApakah anda ingin melanjutkan untuk menghapus data diatas? (\"Yes\" / \"No\") : ").capitalize()
                        if delete_option != "Yes" and delete_option != "No":
                            print("Hanya dapat memilih \"Yes\" / \"No\"")
                        elif delete_option == "No":
                            break
                        elif delete_option == "Yes":
                            list_no_backup = []
                            if len(backup_data)!=0:
                                for num in range(len(backup_data)):
                                    list_no_backup.append(backup_data[num]["noTelepon"])
                                if phone_number_list[no_list]["noTelepon"] not in list_no_backup:
                                        backup_data.append(phone_number_list[no_list])
                            else:
                                backup_data.append(phone_number_list[no_list])
                            del phone_number_list[no_list]
                            print("---------------------------------------------------------------------------")
                            print(f"Data dengan nomor {delete_value[0]['noTelepon'].strip()}, atas nama \"{delete_value[0]['nama'].strip()}\" berhasil dihapus")
                            print("---------------------------------------------------------------------------")
                            break 
                        
                    
        elif option_in_del == "2":
            break

def menu_search():
    while(True):
        display_search()
        option_search = input("Masukan angka menu yang ingin dijalankan : ")    
        if option_search == "1":    
            while (True):
                data_searched = input(f"Masukan kata kunci untuk mencari data : ").strip()
                data_searched = data_searched.lower()
                if data_searched == "":
                    print("----------------------------------------------")
                    print("Kata yang dicari harus berupa huruf atau nomor")
                    print("----------------------------------------------")
                else:
                    all_data_found = [] 
                    for no in range (len(phone_number_list)):
                        list_contact = list(phone_number_list[no].values())
                        sentence = (" ".join(list_contact[:-1])).lower()
                        if data_searched in sentence:
                            all_data_found.append(phone_number_list[no])
                    if len(all_data_found) == 0:
                        print("----------------------------------------")
                        print("Data tidak ditemukan pada daftar telepon")
                        print("----------------------------------------")
                        break
                    else:
                        user_display(all_data_found)
                        print("----------------------------------------------------------------------------------")
                        print(f"Data diatas merupakan daftar yang ditemukan berdasarkan kata \"{data_searched}\"")
                        print("----------------------------------------------------------------------------------")
                        break
                    
        elif option_search == "2":
            break

def menu_emergency():
    while(True):
        display_emergency()
        option_emergency = input("Masukkan angka menu yang ingin dijalankan : ")    
        if option_emergency == "1":    
            emergency_list=[]
            while (True):
                for no in range(len(phone_number_list)):
                    if phone_number_list[no]["emergency"] == "Yes":
                        emergency_list.append(phone_number_list[no]) 
                if len(emergency_list) == 0:
                    print("-------------------------------")
                    print("Tidak ada daftar kontak darurat")
                    print("-------------------------------")
                    break 
                else:   
                    user_display(emergency_list)
                    print("-------------------------------------------")
                    print("Data diatas merupakan daftar kontak darurat")
                    print("-------------------------------------------")
                    break
        elif option_emergency == "2":
            break

def menu_clear_n_backup():
    while(True):
        display_clear_n_backup()
        option_in_clear_n_backup = input("Masukan angka menu yang ingin dijalankan : ")
        if option_in_clear_n_backup == "1" :
            if len(phone_number_list) == 0:
                print("---------------------------")
                print("Daftar nomor telepon kosong")
                print("---------------------------")
            else:
                while (True):
                    display(phone_number_list)
                    clear_option = input("\nApakah anda ingin melanjutkan untuk menghapus semua data diatas? (\"Yes\" / \"No\") : ").capitalize()
                    if clear_option != "Yes" and clear_option != "No":
                        print("Hanya dapat memilih \"Yes\" / \"No\"")
                    elif clear_option == "No":
                        break
                    elif clear_option == "Yes":
                        list_no_backup = []
                        if len(backup_data)!=0:
                            for num in range(len(backup_data)):
                                list_no_backup.append(backup_data[num]["noTelepon"])
                            for no in range(len(phone_number_list)):
                                if phone_number_list[no]["noTelepon"] not in list_no_backup:
                                    backup_data.append(phone_number_list[no])
                        else:
                            backup_data.extend(phone_number_list)
                        phone_number_list.clear()
                        print("-----------------------------------------------------")
                        print("Semua data pada daftar nomor telepon berhasil dihapus")
                        print("-----------------------------------------------------")
                        break

        elif option_in_clear_n_backup == "2":
            if len(backup_data) == 0:
                print("---------------------------------")
                print("Tidak ada data untuk dikembalikan")
                print("---------------------------------")
            else:   
                while (True):
                    print("----------------------------------------------")
                    print("Berikut merupakan data yang dapat dikembalikan")
                    print("----------------------------------------------")
                    data_restored = []
                    list_no_backup = []
                    for num in range(len(phone_number_list)):
                        list_no_backup.append(phone_number_list[num]["noTelepon"])
                    for no in range(len(backup_data)):
                        if backup_data[no]["noTelepon"] not in list_no_backup:
                            data_restored.append(backup_data[no])

                    display(data_restored)
                    backup_option = input("\nApakah anda ingin mengembalikan data yang telah dihapus? (\"Yes\" / \"No\") : ").capitalize()
                    if backup_option != "Yes" and backup_option != "No":
                        print("Hanya dapat memilih \"Yes\" / \"No\"")
                    elif backup_option == "No":
                        break
                    elif backup_option == "Yes":
                        phone_number_list.extend(data_restored)
                        backup_data.clear()
                        print("---------------------------------------------")
                        print("Data yang telah dihapus berhasil dikembalikan")
                        print("---------------------------------------------")
                        break
        elif option_in_clear_n_backup == "3":
            break

def menu_exit():
    print("------------------------------------------------------------")
    print("Terima kasih telah menggunakan Yellow Pages Rusun BPJS Kabil")
    print("------------------------------------------------------------")


yellow_pages()
