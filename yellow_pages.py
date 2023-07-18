phone_number_list = [
    {"nama" : "Syahid Ahmad", "noTelepon" : "085717117166", "keterangan" : "Penghuni Kamar 110 ", "alamat":"Rusun TB 02", "email" : "syahidamd26@gmail.com", "emergency" : "No"},
    {"nama" : "Novaldy Zein", "noTelepon" : "08223451233", "keterangan" : "Penjual Galon", "alamat":"Rusun BPJS Kabil", "email" : "-", "emergency" : "No"},
    {"nama" : "Handika Handoko", "noTelepon" : "112233445566", "keterangan" : "Maintainance Rusun ", "alamat":"Rusun BPJS Kabil", "email" : "ekihandika@gmail.com",  "emergency" : "No"},
    {"nama" : "Alfi Rafi", "noTelepon" : "07787100011", "keterangan" : "Pemadam Kebakaran", "alamat":"Jl Patimura", "email" : "pemadam_kabil@gmail.com", "emergency" : "Yes"},
    {"nama" : "Rifat Rahmad", "noTelepon" : "07787491000", "keterangan" : "Polsek Nongsa", "alamat":"Jln Kavling Senjulung", "email" : "polseknongsa@gmail.com", "emergency" : "Yes"},
    {"nama" : "Ahmad Atang", "noTelepon" : "085717117166", "keterangan" : "Soto Ayam", "alamat":"Jl Raya Pelabuhan", "email" : "-", "emergency" : "No"},
    {"nama" : "Junior Robertlewandowski", "noTelepon" : "223344556677", "keterangan" : "Penghuni Kamar 113", "alamat":"Rusun TB 02", "email" : "robertjunior@yahoo.com", "emergency" : "No"},
    {"nama" : "Rudi Saptaji", "noTelepon" : "08123123123", "keterangan" : "Soto Kudus", "alamat":"Jln Hang Kesturi", "email" : "-",  "emergency" : "No"},
    {"nama" : "Ros Nalfisah", "noTelepon" : "0778711960", "keterangan" : "Rumah Sakit Soedarsono", "alamat":"Jl Hang Kesturi 2", "email" : "rssudarsono@ymail.com", "emergency" : "Yes"},
    {"nama" : "Beti Sukati", "noTelepon" : "334455667788", "keterangan" : "Ayam Bakar Bu Beti", "alamat":"Jl Hang Kesturi", "email" : "bubetibakaran@gmail.com ", "emergency" : "No"},
]


def display_menu():

    print('''
Selamat Datang di Yellow Pages Rusun BPJS Kabil

    List Menu :
    1. Menampilkan daftar nomor telepon
    2. Menambah nomor telepon baru
    3. Memperbarui data nomor telepon
    4. Menghapus nomor telepon
    5. Menampilkan informasi berdasarkan data yang diketahui
    6. Nomor telepon darurat
    7. Exit program
''')

def display(data):
    print("\nDaftar Nomor Telepon Rusun BPJS Kabil\n")
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

def display_read():
    print("""\nMenampilkan Daftar Nomor Telepon
    
    List Menu :
    1. Menampilkan semua daftar nomor telepon
    2. Cek detail informasi berdasarkan nomor telepon
    3. Kembali ke menu utama
""")
def display_add():
    print("""\nMenambah Nomor Telepon Baru
    
    List Menu :
    1. Menambahkan nomor telepon baru
    2. Kembali ke menu utama
        """)

def display_update():
    print("""Memperbarui Daftar Nomor Telepon
    
    List Menu :
    1. Memperbarui daftar nomor telepon
    2. Kembali ke menu utama
        """)
    
def display_delete():
    print("""Menghapus Data pada Daftar Nomor Telepon
    
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
    print("""Mencari Kelengkapan Data
    
    List Menu :
    1. Mencari kelengkapan data berdasarkan suatu kata
    2. Kembali ke menu utama
        """)

def display_emergency():
    print("""Daftar Kontak Darurat
    
    List Menu :
    1. Melihat daftar kontak darurat
    2. Kembali ke menu utama
        """)


def exit():
    print("Terimakasih telah menggunakan Yellow Pages Rusun Kabil")

def read_menu():
    while(True):
        display_read()
        option1 = input("Masukan angka menu yang ingin dijalankan : ")
        if option1 == "1" :
            if len(phone_number_list) == 0:
                print("\nDaftar telepon kosong")
            else: 
                display(phone_number_list)

        elif option1 == "2" :
            phone_number = input("Masukan nomor telepon untuk mengetahui detail informasi : ")
            if len(phone_number_list) == 0:
                print("\nDaftar telepon kosong")
            elif phone_number.isnumeric() == False:
                print("\nNomor telepon harus berupa angka")
            else:
                primary_key=[]
                for no in range(len(phone_number_list)):
                    if phone_number_list[no]["noTelepon"] == phone_number:
                        primary_key.append(phone_number_list[no])
                        break
                if len(primary_key) != 0:
                    display(primary_key)
                else: 
                    print("\nNomor telepon belum terdaftar")

        elif option1 == "3":
            break
   
def add_menu():
    while(True):
        display_add()
        option2 = input("Masukan angka menu yang ingin dijalankan : ")    
        if option2 == "1":    
            while (True):
                back_to_menu_2 = False
                all_data_entered = False
                add_number = input(f"Masukan nomor telepon : ")
                if add_number.isnumeric() == False or len(add_number) > 16:
                    print("Nomor telepon harus berupa angka\ndan maksimal 16 angka")
                else:
                    primary_key=[]
                    for no in range(len(phone_number_list)):
                        if phone_number_list[no]["noTelepon"] == add_number:
                            primary_key.append(phone_number_list[no]["noTelepon"])    
                    if len(primary_key) != 0 :
                        print("\nNomor telepon telah terdaftar")
                        break
                    else:
                        while (True):
                            add_first_name = input("Masukan nama depan : ").capitalize()
                            if add_first_name.isalpha() == False or len(add_first_name) > 16:
                                print("Nama depan harus berupa alfabet (a-z)\ndan maksimal 16 karakter")
                            else:
                                break

                        while (True):
                            add_last_name = input("Masukan nama belakang : ").capitalize()
                            if add_last_name.isalpha() == False or len(add_last_name) > 16:
                                print("Nama belakang harus berupa alfabet (a-z)\ndan maksimal 16 karakter")
                            else:
                                break
       
                        while (True):
                            add_information = input("Masukan keterangan terkait nomor telepon : ")
                            if len(add_information) > 32 or add_information == "":
                                print("Apabila tidak ada keterangan, bisa diisi \"-\"\ndan maksimal 32 karakter")
                            else:
                                break

                        while (True):
                            add_email = input("Masukan alamat email : ")
                            if add_email == "-":
                                break
                            elif (len(add_email) > 32)  or (add_email == "") or ("@" not in add_email):
                                print("Apabila tidak mengetahui alamat, bisa diisi \"-\".\nJangan lupa untuk email gunakan \"@\" dan maksimal 32 karakter")
                            else:
                                break

                        while (True):
                            add_address = input("Masukan alamat : ")
                            if len(add_address) > 32  or add_address == "":
                                print("Apabila tidak mengetahui alamat, bisa diisi \"-\"\ndan maksimal 16 karakter")
                            else:
                                break
                            
                        while (True):
                            add_emergency = input("Apakah kontak ini merupakan nomor darurat? (\"Yes\" / \"No\") : ").capitalize()
                            if len(add_emergency) > 3  or add_address == "":
                                print("Hanya dapat diisi \"Yes\" / \"No\"")
                            elif add_emergency == "Yes" or add_emergency == "No":
                                all_data_entered = True
                                break
                        new_list_phone_number = [{"nama": add_first_name+" "+add_last_name , "noTelepon": add_number, "keterangan" : add_information , "alamat" : add_address , "email": add_email , "emergency" : add_emergency }]
                        display(new_list_phone_number)
                            
                        while (True):
                            save_data = input("""Apakah data ingin disimpan? (\"Yes\" / \"No\") : """).capitalize()
                            if save_data != "Yes" and save_data != "No":
                                print("hanya dapat memilih (\"Yes\" / \"No\")")
                            elif save_data == "No":
                                back_to_menu_2 = True
                                break
                            elif save_data == "Yes":
                                phone_number_list.extend(new_list_phone_number)
                                print("\nData Nomor Telepon Baru, Telah Berhasil Disimpan")
                                break
                        if all_data_entered == True:
                            break
                        elif back_to_menu_2 == True:
                            break
        elif option2 == "2":
            break    

def update_menu():
    while(True):
        display_update()
        option3 = input("Masukan angka menu yang ingin dijalankan : ")    
        if option3 == "1":
            while (True):
                back_to_menu_3 = False
                data_updated = False
                add_number_3 = input(f"Masukan nomor telepon untuk memperbarui data : ")
                if add_number_3.isnumeric() == False or len(add_number_3) > 16:
                    print("Nomor telepon harus angka\ndan maksimal 16 angka")
                else:
                    value_update = []
                    no_list = 0
                    for no in range(len(phone_number_list)):
                        if phone_number_list[no]["noTelepon"] == add_number_3:
                            value_update.append(phone_number_list[no]) 
                            no_list = no
                    if len(value_update)==0:
                            print("\nNomor Telepon yang Anda Masukan Tidak Terdaftar\n")
                            break
                    else: 
                        display(value_update)
                        continue_update = False
                        while (True):
                            update_option = input("""\nApakah Anda ingin melanjutkan untuk memperbarui data? ("Yes" / "No") : """).capitalize()
                            if update_option != "Yes" and update_option != "No":
                                print("hanya dapat memilih \"Yes\" / \"No\"")
                            elif update_option == "No":
                                back_to_menu_3 = True
                                break
                            elif update_option == "Yes":
                                continue_update = True
                                break
                        if back_to_menu_3 == True and continue_update == False:
                            break
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
                                            print("Nama depan harus berupa alfabet (a-z)\ndan maksimal 16 karakter")
                                        else:
                                            break
                                    while (True):
                                        new_last_name = input("Masukan nama belakang baru : ").capitalize()
                                        if new_last_name.isalpha() == False or len(new_last_name) > 16:
                                            print("Nama belakang harus berupa alfabet (a-z)\ndan maksimal 16 karakter")
                                        else:
                                            new_data = new_first_name + " " + new_last_name
                                            value_update[0][update_key] = new_data
                                            break
                                            
                                elif option_update == "Nomor":
                                    update_key = "noTelepon"
                                    while (True):
                                        new_number = input(f"Nomor telepon sebelumnya \"{value_update[0][update_key].strip()}\", Masukan nomer telepon baru : ")
                                        primary_key=[]
                                        if new_number.isnumeric() == False or len(new_number) > 16:
                                            print("Nomor telepon harus angka\ndan maksimal 16 angka")
                                        else:    
                                            for no in range(len(phone_number_list)):
                                                if phone_number_list[no]["noTelepon"] == new_number:
                                                    primary_key.append(phone_number_list[no]["noTelepon"])    
                                            if len(primary_key) != 0 :
                                                print("\nNomor telepon telah terdaftar, Silahkan masukan nomor telepon lain\n")
                                            else:
                                                new_data = new_number
                                                value_update[0][update_key] = new_data
                                                break
                                        
                                elif option_update == "Keterangan":
                                    update_key = "keterangan"
                                    new_information = input(f"Keterangan sebelumnya \"{value_update[0][update_key].strip()}\", Masukan keterangan baru : ")
                                    if len(new_information) > 32 or new_information == "":
                                        print("Apabila tidak ada keterangan, bisa diisi \"-\"\ndan maksimal 32 karakter")
                                    else:
                                        new_data = new_information
                                        value_update[update_key] = new_data
                                        break
                                        
                                elif option_update == "Alamat":
                                    update_key = "alamat"
                                    new_address = input(f"Alamat sebelumnya \"{value_update[0][update_key].strip()}\", Masukan alamat baru : ")
                                    if len(new_address) > 32  or new_address == "":
                                        print("Apabila tidak mengetahui alamat, bisa diisi \"-\"\ndan maksimal 16 karakter")
                                    else:
                                        new_data = new_address
                                        value_update[0][update_key] = new_data
                                        break
                                        
                                elif option_update == "Email":
                                    update_key = "email"
                                    new_email = input(f"Email sebelumnya \"{value_update[0][update_key].strip()}\", Masukan email baru : ")
                                    if new_email == "-":
                                        break
                                    elif (len(new_email) > 32)  or (new_email == "") or ("@" not in new_email):
                                        print("Apabila tidak mengetahui email, bisa diisi \"-\".\nJangan lupa untuk email gunakan \"@\" dan maksimal 32 karakter")
                                    else:
                                        new_data = new_email
                                        value_update[0][update_key] = new_data
                                        break
                                        
                                elif option_update == "Darurat":
                                    update_key = "emergency"
                                    new_emergency = input(f"""Nomor merupakan nomor darurat ? Sebelumnya :\"{value_update[0][update_key].strip()}\"
                                                    Masukan keterangan nomor darurat baru ("Yes" / "No") : """).capitalize()
                                    if len(new_emergency) > 3  or new_emergency == "":
                                        print("Hanya dapat diisi (\"Yes\" or \"No\")")
                                    elif new_emergency == "Yes" or new_emergency == "No":
                                        new_data = new_emergency
                                        value_update[0][update_key] = new_data
                                        break

                                if len(new_data) != 0:
                                    display(value_update)
                                    while (True):    
                                        save_new_data = input("""Apakah data baru ingin disimpan? ("Yes" / No") : """).capitalize()
                                        if save_new_data != "Yes" and save_new_data != "No":
                                            print("hanya dapat memilih \"Yes\" / \"No\"")
                                        elif save_new_data == "No":
                                            back_to_menu_3 = True
                                            break
                                        elif save_new_data == "Yes":
                                            phone_number_list[no_list] = value_update[0]
                                            print("Memperbarui data telah berhasil, data telah disimpan")
                                            data_updated = True
                                            break   
                                    if back_to_menu_3 == True:
                                        break
                                    elif data_updated == True:
                                        back_to_menu_3 = True
                                        break        
                if back_to_menu_3 == True:
                    break          

        elif option3 == "2":
            break
def delete_menu():
    while(True):
        display_delete()
        option4 = input("Masukan angka menu yang ingin dijalankan : ")
        if option4 == "1" :
            back_to_menu_4 = False
            add_number_4 = input(f"Masukan nomor telepon untuk menghapus data pada daftar telepon : ")
            if add_number_4.isnumeric() == False or len(add_number_4) > 16:
                print("Nomor telepon harus angka dan maksimal 16 angka")
            else:
                delete_value = []
                no_list = 0
                for no in range(len(phone_number_list)):
                    if phone_number_list[no]["noTelepon"] == add_number_4:
                        delete_value.append(phone_number_list[no]) 
                        no_list = no
                        break
                if len(delete_value)==0:
                        print("\nNomor telepon yang anda masukan tidak terdaftar\n")
                        break
                else: 
                    display(delete_value)
                    continue_delete = False
                    while (True):
                        delete_option = input("""\nApakah anda ingin melanjutkan untuk Menghapus data diatas? ("Yes" / "No") : """).capitalize()
                        if delete_option != "Yes" and delete_option != "No":
                            print("Hanya dapat memilih \"Yes\" / \"No\"")
                        elif delete_option == "No":
                            back_to_menu_4 = True
                            break
                        elif delete_option == "Yes":
                            continue_delete = True
                            break 
                        
                    if back_to_menu_4 == False and continue_delete == True :
                        del phone_number_list[no_list]
                        print(f"Data dengan nomor {delete_value[0]['noTelepon'].strip()}, atas nama \"{delete_value[0]['nama'].strip()}\" berhasil dihapus")
                        back_to_menu_4 = True
        elif option4 == "2":
            break

def search_menu():
    while(True):
        display_search()
        option5 = input("Masukan angka menu yang ingin dijalankan : ")    
        if option5 == "1":    
            while (True):
                data_searched = input(f"Masukan kata kunci untuk mencari data : ").strip()
                data_searched = data_searched.lower()
                if data_searched == "":
                    print("Kata yang dicari harus berupa huruf atau nomor\n")
                else:
                    all_data_found = [] 
                    for no in range (len(phone_number_list)):
                        list_contact = list(phone_number_list[no].values())
                        sentence = (" ".join(list_contact[:-1])).lower()
                        if data_searched in sentence:
                            all_data_found.append(phone_number_list[no])
                    if len(all_data_found) == 0:
                        print("Data tidak ditemukan pada daftar telepon")
                        break
                    else:
                        display(all_data_found)
                        print(f"\nBerikut data yang ditemukan berdasarkan kata \"{data_searched}\"\n")
                        break
                    
        elif option5 == "2":
            break

def emergency_menu():
    while(True):
        display_emergency()
        option6 = input("Masukkan angka Menu yang ingin dijalankan : ")    
        if option6 == "1":    
            emergency_list=[]
            while (True):
                for no in range(len(phone_number_list)):
                    if phone_number_list[no]["emergency"] == "Yes":
                        emergency_list.append(phone_number_list[no]) 
                display(emergency_list)
                print("\nDaftar Diatas Merupakan List Kontak Darurat. Terimakasih\n")
                break
        elif option6 == "2":
            break


def main_menu():
    while(True):
        display_menu()
        menu_option = input("Masukan angka menu yang ingin dijalankan : ")
        if (menu_option == "1"):
            read_menu()
        
        elif (menu_option == "2"):
            add_menu()

        elif (menu_option == "3"):
            update_menu()
            
        elif (menu_option == "4"):
            delete_menu()

        elif (menu_option == "5"):
            search_menu()
        
        elif (menu_option == "6"):
            emergency_menu()
                        
        elif (menu_option == "7"):
            print("\nTerimakasih telah menggunakan Yellow Pages Rusun BPJS Kabil")
            break
        
        else:
            print("Tidak ada menu untuk dijalankan")


main_menu()