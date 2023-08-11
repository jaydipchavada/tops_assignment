import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="")
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS fromm")
mydb.commit()  # Save and execute 


mydb = pymysql.connect(host="localhost", user="root", password="", database="fromm")
mycursor = mydb.cursor()


mycursor.execute("CREATE TABLE IF NOT EXISTS STUDENT (id int primary key auto_increment , name varchar(20), roll_no int, gender varchar(20), hobbies varchar(20), city varchar(20))")
mydb.commit()  # Save and execute 
