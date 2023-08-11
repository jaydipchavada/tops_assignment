# pip install pymysql
import pymysql

mydb = pymysql.connect(host="localhost",user="root",password="")

mycursor = mydb.cursor()

# create database in mysql

mycursor.execute("CREATE DATABASE IF NOT EXISTS TOPS_CRUD")
mydb.commit() # SAVE AND EXECUTE

mydb = pymysql.connect(host="localhost",user="root",password="",database="TOPS_CRUD")
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS STUDENT (id int primary key auto_increment , name varchar(20), subject varchar(20), city varchar(20))")
mydb.commit()