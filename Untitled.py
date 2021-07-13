#!/usr/bin/env python
# coding: utf-8

# In[5]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)
if db.is_connected():
        print("Berhasil terhubung ke database")


# In[7]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE db_film")

print("Database berhasil dibuat!")


# In[8]:


import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)
cursor= db.cursor()
sql = """CREATE TABLE tblfilm (
    kode_id INT AUTO_INCREMENT PRIMARY KEY,
    judulfilm VARCHAR(255),
    jenis_film varchar(255)
    
)
"""
cursor.execute(sql)
print("tabel film berhasil dibuat")


# In[9]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)
cursor= db.cursor()
sql = "INSERT INTO tblfilm (JudulFilm, Jenis_Film) VALUES (%s, %s)"
val = ("X-Men: Dark Phoenix", "Action")
cursor.execute(sql,val)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))


# In[10]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)
cursor= db.cursor()
sql = "INSERT INTO tblfilm (JudulFilm, Jenis_Film) VALUES (%s, %s)"
values = [
    ("Aladdin", "Fantasy"),
    ("Godzilla II: King of the Monsters","Fantasy"),
    ("John Wick: Chapter 3 - Parabellum","Action")
]
     
for val in values:
    cursor.execute(sql,val)
    db.commit()

print("{} data ditambahkan".format(cursor.rowcount))


# In[11]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)
cursor= db.cursor()
sql = "SELECT * FROM tblfilm"
cursor.execute(sql)
     
results = cursor.fetchall()

for data in results:
    print(data)


# In[12]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)
cursor= db.cursor()
sql = "SELECT * FROM tblfilm"
cursor.execute(sql)
     
results = cursor.fetchall()

for data in results:
    print(data)


# In[14]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)
cursor= db.cursor()
sql = "UPDATE tblfilm SET JudulFilm=%s, Jenis_Film=%s WHERE Kode_id=%s"
val = ("X-Men: Dark Phoenix", "Fantasy Action", 1)
cursor.execute(sql,val)

db.commit()

print("{} data diubah".format(cursor.rowcount))


# In[15]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)
cursor= db.cursor()
sql = "DELETE FROM tblfilm WHERE Kode_id=%s"
val = (1, )
cursor.execute(sql,val)

db.commit()

print("{} data dihapus".format(cursor.rowcount))


# In[37]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)

def insert_data(db):
    judulfilm = input"Masukkan Judul: ")
    jenis_film = input"Masukkan Jenis: ")
    val = (judulfilm, jenis_film)
    cursor = db.cursor()
    sql = "INSERT INTO tblfilm (judulfilm, Jenis_Film) VALUES (%s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))
    
    def show_data(db):
        cursor = db.cursor()
        sql = "SELECT * FROM tblfilm"
        cursor.execute(sql)
        results = cursor.fetchall()
        
        if cursor.rowcount < 0:
            print("Tidak ada data")
            else:
                for data in results:
                    print(data)
                    
def update_data(db):
    cursor = db.cursor()
    show_data(db)
    kode_id = input("pilih id film> ")
    judulfilm = input("Judul film: ")
    jenis_film = input("Jenis film: ")
    
    sql = "UPDATE tblfilm SET judulfilm=%s, jenis_film=%s WHERE kode_id=%s"
    val = (judulfilm, jenis_film, kode_id)
    cursor.execute(sql, val)
    db.commit
    print("{} data berhasil diubah".format(cursor.rowcount))
    
def delete_data(db):
    cursor = db.cursor()
    show_data(db)
    kode_id = input("pilih kode id> ")
    sql = "DELETE FROM tblfilm WHERE kode_id=%s"
    val = (kode_id,)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))
    
    
def search_data(db):
    cursor = db.cursor()
    keyword = input("Kata kunci: ")
    sql = "SELECT * FROM tblfilm WHERE judulfilm LIKE %s OR jenis_film LIKE %s"
    val = ("%{}%".format(keyword), "%{}%".format(keyword))
    cursor.execute(sql, val)
    result = cursor.fetchall()
    
    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)
            
def show_menu(db):
    print("=== APLIKASI DATABASE FILM ===")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("0. Keluar")
    print("---------------------")
    menu = input("Pilih menu> ")
    
    #clear screen
    os.system("clear")
    
    if menu == "1":
        insert_data(db)
    elif menu == "2":
        show_data(db)
    elif menu == "3":
        update_data(db)
    elif menu == "4":
        delete_data(db)
    elif menu == "5":
        search_data(db)
    elif menu == "0":
        exit()
    else:
        print("Menu salah!")
        
if_name__ == "_main_":
    while(True):
        show_menu(db)


# In[ ]:


def konversiSuhu(suhu):
   drjt = int(suhu[:-1])
   inputan = suhu[-1]

   if inputan.upper() == "C":
     hasil1 = float((9 * drjt) / 5 + 32)
     hasil2 = float(drjt + 273.15)
     hasil3 = float(4/5 * drjt)
     jenisX = "Celcius"
     jenis1 = "Fahrenheit"
     jenis2 = "Kelvin"
     jenis3 = "Reamur"
     print(drjt,jenisX,"=","{:.1f}".format(hasil1),jenis1)
     print(drjt,jenisX,"=","{:.1f}".format(hasil2),jenis2)
     print(drjt,jenisX,"=","{:.1f}".format(hasil3),jenis3)
                
   elif inputan.upper() == "F":
     hasil1 = float((drjt - 32) * 5 / 9)
     hasil2 = float(((drjt - 32) * 5 / 9) + 273.15)
     hasil3 = float(4/9 * (drjt-32))
     jenisX = "Fahrenheit"
     jenis1 = "Celsius"
     jenis2 = "Kelvin"
     jenis3 = "Reamur"
     print(drjt,jenisX,"=","{:.1f}".format(hasil1),jenis1)
     print(drjt,jenisX,"=","{:.1f}".format(hasil2),jenis2)
     print(drjt,jenisX,"=","{:.1f}".format(hasil3),jenis3)

   elif inputan.upper() == "K":
     hasil1 = float(drjt - 273.15)
     hasil2 = float(((drjt - 273.15) * 9 / 5)+32)
     hasil3 = float(4/5 * (drjt-273))
     jenisX = "Kelvin"
     jenis1 = "Celcius"
     jenis2 = "Fahrenheit"
     jenis3 = "Reamur"
     print(drjt,jenisX,"=","{:.1f}".format(hasil1),jenis1)
     print(drjt,jenisX,"=","{:.1f}".format(hasil2),jenis2)
     print(drjt,jenisX,"=","{:.1f}".format(hasil3),jenis3)
     
   elif inputan.upper() == "R":
     hasil1 = float((5/4) * drjt)
     hasil2 = float((9/4 * drjt) + 32)
     hasil3 = float((5/4 * drjt) + 273)
     jenisX = "Reamur"
     jenis1 = "Celcius"
     jenis2 = "Fahrenheit"
     jenis3 = "Kelvin"
     print(drjt,jenisX,"=","{:.1f}".format(hasil1),jenis1)
     print(drjt,jenisX,"=","{:.1f}".format(hasil2),jenis2)
     print(drjt,jenisX,"=","{:.1f}".format(hasil3),jenis3)
     
   else:
      print("Inputan tidak sesuai")


i=0
print("Program Konversi Suhu")
while i==0:
   temp = input("\nMasukan suhu? (Misal: 30C, 20F, 21K, 44R): ")
   konversiSuhu(temp)

   lagi=int(input("Hitung lagi?1=ya & 0=tidak = "))
   if(lagi==1):
      i=0
   elif(lagi!=1):
      i=1


# In[ ]:




