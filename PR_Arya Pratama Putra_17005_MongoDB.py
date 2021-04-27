import pymongo

print(" Program Demo Operasi CRUD PostgreSQL Database ")
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
    # create a database
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["ProjectDB"]
    print(client.list_database_names())
    
    # create a collection
    col = db ["managementuser"]
    print(db.list_collection_names())

    #create a content or insert
    mylist = [
        { "_id": 1, "name": "John Doe", "pass": "johnwick", "stat": "active"},
        { "_id": 2, "name": "Alice Watson", "pass": "alice", "stat": "active"}
        ]
    x = col.insert_many(mylist)
    #print list of the _id values of the inserted documents:
    print(x.inserted_ids)
    for x in col.find():
        print(x)

elif menu=='2' :
    print("Insert data")
    #insert
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["ProjectDB"]
    col = db ["managementuser"]
    mylist = { "name": "Peter", "pass": "lowstreet", "stat": "active" }
    x = col.insert_one(mylist)
    print(x.inserted_id)
    
    mydict = { "_id": 3, "name": "John", "pass": "Highway 37", "stat": "active" }

    x = col.insert_one(mydict)

elif menu=='3' :
    print("Select/search data")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["ProjectDB"]
    col = db ["managementuser"]
    #search data
    myquery = { "name": "Peter" }
    mydoc = col.find(myquery)
    for x in mydoc:
        print(x)

elif menu=='4' :
    print("Update data")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["ProjectDB"]
    col = db ["managementuser"]
    #update data
    myquery = { "name": "Peter" }
    newvalues = { "$set": { "name": "Idaho" } }
    col.update_one(myquery, newvalues)
    #print "customers" after the update:
    for x in col.find():
        print(x)

elif menu=='5' :
    print("Delete data")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["ProjectDB"]
    col = db ["managementuser"]
    #delete data
    myquery = { "pass": "Highway 37" }
    col.delete_one(myquery)