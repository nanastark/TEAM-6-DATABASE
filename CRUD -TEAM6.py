import mysql.connector
import os

db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "Mysqlnyasajidah6",
  database = "perpusnas"
)

def show_data(db):
  cursor = db.cursor()
  sql = "SELECT * FROM `perpustakaan nasional`"
  cursor.execute(sql)
  results = cursor.fetchall()
  if cursor.rowcount < 0:
    print("DATA TIDAK ADA")
  else:
    for data in results:
      print(data)


def searchnamabuku_data(db):
  cursor = db.cursor()
  keyword = input("KATA KUNCI: ")
  sql = "SELECT * FROM `perpustakaan nasional` WHERE nama_buku LIKE \'%{}%\'".format(keyword)
  cursor.execute(sql)
  results = cursor.fetchall()
  if cursor.rowcount < 0:
    print("DATA TIDAK ADA")
  else:
    for data in results:
      print(data)

def searchtahunpenerbitan_data(db):
  cursor = db.cursor()
  keyword = input("TAHUN PENERBITAN: ")
  sql = "SELECT * FROM `perpustakaan nasional` WHERE tahun_penerbitan LIKE \'%{}%\'".format(keyword)
  cursor.execute(sql)
  results = cursor.fetchall()
  if cursor.rowcount < 0:
    print("DATA TIDAK ADA")
  else:
    for data in results:
      print(data)

def searchpenulisbuku_data(db):
  cursor = db.cursor()
  keyword = input("KATA KUNCI: ")
  sql = "SELECT * FROM `perpustakaan nasional` WHERE penulis_buku LIKE \'%{}%\'".format(keyword)
  cursor.execute(sql)
  
  if cursor.rowcount < 0:
    print("DATA TIDAK ADA")
  else:
    results = cursor.fetchall()
    for data in results:
      print(data)

def searchnomorisbn_data(db):
  cursor = db.cursor()
  keyword = input("KATA KUNCI: ")
  sql = "SELECT * FROM `perpustakaan nasional` WHERE nomor_isbn = {}".format(keyword)
  cursor.execute(sql)
  
  if cursor.rowcount < 0:
    print("DATA TIDAK ADA")
  else:
    results = cursor.fetchall()
    for data in results:
      print(data)
    
def penilaianbuku_data(db):
  cursor = db.cursor()
  buku = input("NAMA BUKU: ")
  penulis = input("NAMA PENULIS: ")
  penilian= input("PENILAIAN: ")
  print("")
  print("===== TERIMAKASIH ATAS PENILAIAN ANDA, KAMI SANGAT MENGAPRESIASI =====")
  sql = "INSERT INTO PENILAIAN (judul_buku, penulis_buku, penilaian_buku) VALUES (%s,%s,%s)"
  val = ("{}".format(buku), "{}".format(penulis), "{}".format(penilian))
  cursor.execute(sql, val)
  db.commit()
  print("{} DATA DISIMPAN".format(cursor.rowcount))


def show_menu(db):
  print("")
  print("=============== APLIKASI PERPUSTAKAAN NASIONAL DAERAH JAKARTA ===============")
  print("")
  print("1. Tampilkan Data")
  print("")
  print("2. Cari Nama Buku")
  print("")
  print("3. Cari Tahun Penerbitan")
  print("")
  print("4. Cari Penulis Buku")
  print("")
  print("5. Cari Nomor ISBN")
  print("")
  print("6. Penilaian")
  print("")
  print("0. Keluar")
  print("-------------------------------------------------------------------")
  menu = input("PILIH MENU YANG DIINGINKAN > ")

  #clear screen
  os.system("clear")

  if menu == "1":
     show_data(db)
  elif menu == "2":
     searchnamabuku_data(db)
  elif menu == "3":
     searchtahunpenerbitan_data(db)
  elif menu == "4":
     searchpenulisbuku_data(db)
  elif menu == "5":
     searchnomorisbn_data(db)
  elif menu == "6":
     penilaianbuku_data(db)
  elif menu == "0":
     exit()
  else:
    print("MENU TIDAK ADA")

if __name__ == "__main__":
  while(True):
    show_menu(db)