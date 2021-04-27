print(" Program Demo Operasi CRUD SQLite Database ")
print("       Lab Komputasi DTM SV UGM            ")
print("===========================================\n")
def main() :
    print("Menu operasi database")
    print("1. Create database dan tabel")
    print("2. Insert data")
    print("3. Select/search data")
    print("4. Update data")
    print("5. Delete data")
    menu=input("Silahkan pilih operasi ( 1/2/3/4/5 ) ? ")
    print("Anda memilih : " + menu)
    if menu=='1' :
        print("Create database dan tabel")
    elif menu=='2' :
        print("Insert data")
    elif menu=='3' :
        print("Select/search data")
    elif menu=='4' :
        print("Update data")
    elif menu=='5' :
        print("Delete data")

    lagi=input("\nUlangi ga (Y/y) ? ")
    if lagi.lower() == "y" :
        main ()
    else :
        print("Program selesai")
    
main()