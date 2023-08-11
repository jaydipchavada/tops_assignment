import connection
import pymysql
from tkinter import *
from tkinter import messagebox


# database connection

mydb = pymysql.connect(host="localhost", user="root", password="",database="fromm")
mycursor = mydb.cursor()

# Function to save student data into the database

def save_student_data():
    name = name_entry.get()
    roll_no = int(roll_no_entry.get())
    gender = gender_entry.get()
    hobbies = hobbies_entry.get()
    city = city_entry.get()

    
    
    # Insert the student data into the database table "STUDENT"

    values = (name, roll_no , gender , hobbies , city)
    sql = "INSERT INTO STUDENT (names, roll_no , gender , hobbies , city) VALUES (, '%s','%s','%s' ,'%s')"
    mycursor.execute(sql % values)
    mydb.commit()

    # Show a message box 
    messagebox.showinfo("Success", "Student data saved successfully!")

#Function to update student data into the database

def update_student_data():
    name = name_entry.get()
    roll_no = int(roll_no_entry.get())
    gender = gender_entry.get()
    hobbies = hobbies_entry.get()
    city = city_entry.get()

    # Update the student data in the database table "STUDENT"
    sql = "UPDATE STUDENT SET name=%s, gender=%s, hobbies=%s, city=%s WHERE roll_no=%s"
    values = (name, gender, hobbies, city, roll_no)
    mycursor.execute(sql, values)
    mydb.commit()

    # Show a message box to indicate successful data update
    messagebox.showinfo("Success", "Student data updated successfully!")

#Function to delete student data into the database

def delete_student_data():
    roll_no = int(roll_no_entry.get())

    # Delete the student data from the database table "STUDENT"
    sql = "DELETE FROM STUDENT WHERE roll_no=%s"
    mycursor.execute(sql, roll_no)
    mydb.commit()

    # Show a message box
    messagebox.showinfo("Success", "Delete data saved successfully!")

 


# Create the main application window

screen = Tk()
screen.geometry("500x300")  # width x height
screen.title("Student Form")
title = Label(screen,text = "STUDENT_FROM",font = ('Arial',20,'bold'))
title.pack()

# Labels for input fields

name_label = Label(screen, text="Name :", font=("Arial", 12, "bold"))
name_label.place(x=10, y=100)

roll_no_label = Label(screen, text="Roll No :", font=("Arial", 12, "bold"))
roll_no_label.place(x=10, y=140)

gender_label = Label(screen , text="Gender : ", font=("Arial", 12, "bold"))
gender_label.place(x=10,y=180)

hobbies_label = Label(screen , text="hobbies : ", font=("Arial", 12, "bold"))
hobbies_label.place(x=10,y=220 )

city_label =Label( screen,text ="City : ",font=( "Arial","12"," bold"))
city_label.place(x=10,y=260)

# Entry widgets for input fields

name_entry = Entry(screen, font=("Arial", 12))
name_entry.place(x=120, y=100)

roll_no_entry = Entry(screen, font=("Arial", 12))
roll_no_entry.place(x=120, y=140)

gender_entry = Entry(screen , font=("Arial", 12))
gender_entry.place(x=120,y=180)

hobbies_entry =Entry(screen , font= ("Arial", 12))
hobbies_entry.place(x=120,y=220)

city_entry = Entry(screen, font=("Arial", 12))
city_entry.place(x=120, y=260)

# insert button

insert_btn = Button(screen, text="Submit", font=("Arial", 12, "bold"), command=save_student_data)
insert_btn.place(x=10, y=300)

# update button

update_btn = Button(screen, text="update", font=("Arial", 12, "bold"), command=save_student_data)
update_btn.place(x=100 , y=300)

# delete buttton

delete_btn =Button (screen, text="Delete" , font=("Arial", 12, "bold"), command=delete_student_data)
delete_btn.place(x=190, y=300)




screen.mainloop()
