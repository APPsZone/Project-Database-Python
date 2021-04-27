import psycopg2

con = psycopg2.connect(
    host="localhost", 
    port = 5432, 
    database = "test",
    user = "postgres",
    password = "appjunior123")

cur = con.cursor()


print(" Program Demo Operasi CRUD PostgresSQL Database ")
print("       Arya Pratama Putra (19/447311/SV/17005)            ")
print("================================================\n")
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
    # create a database named bengkel
    con = psycopg2.connect(
    host="localhost", 
    user = "postgres",
    database = "test",
    port = 5432,
    password = "appjunior123")
    cur = con.cursor()
    # create a table named user
    cur = con.cursor()
    cur.execute("CREATE TABLE insight (nama VARCHAR(60) NOT NULL, penilaian BOOLEAN NOT NULL)")
    con.commit()
elif menu=='2' :
    print("Insert data")
    #insert
    con = psycopg2.connect(
    host="localhost", 
    port = 5432, 
    database = "test",
    user = "postgres",
    password = "appjunior123")
    cur = con.cursor()
    cur.execute('''INSERT INTO usermanagement (name, pass, stat) VALUES('David Bekam', 'bekam', 'active');''')  
    con.commit()
elif menu=='3' :
    print("Select/search data")
    con = psycopg2.connect(
    host="localhost", 
    port = 5432, 
    database = "test",
    user = "postgres",
    password = "appjunior123")
    cur = con.cursor()
    cur.execute("""SELECT * FROM sparepart""")
    query_res = cur.fetchall()
    print(query_res)

elif menu=='4' :
    print("Update data")
    con = psycopg2.connect(
    host="localhost", 
    port = 5432, 
    database = "test",
    user = "postgres",
    password = "appjunior123")
    cur = con.cursor()
    sql1 = "UPDATE usermanagement SET pass = 'etoo' WHERE id = 4"
    cur.execute(sql1)
    con.commit() 
    print(sql1)

elif menu=='5' :
    print("Delete data")
    con = psycopg2.connect(
    host="localhost", 
    port = 5432, 
    database = "test",
    user = "postgres",
    password = "appjunior123")
    cur = con.cursor()
    sql2 = "DELETE FROM usermanagement WHERE id = 4"
    cur.execute(sql2)
    con.commit()
    print(sql2)
cur.close()
con.close()
