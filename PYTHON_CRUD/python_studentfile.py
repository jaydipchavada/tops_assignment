import pymysql
import connection
mydb = pymysql.connect(host="localhost",user="root",password="",database="TOPS_CRUD")
mycursor = mydb.cursor()

menu = """

                        MENU
                    PRESS 1 FOR ADD STUDENT
                    PRESS 2 FOR VIEW STUDENTS
                    PRESS 3 FOR UPDATE STUDENTS
                    PRESS 4 FOR DELETE STUDENTS
                    PRESS 5 FOR SEPCIFIC ONE STUDENTS
                    PRESS 6 FOR EXIT
        """
print(menu)

choice = int(input("Enter your choice : "))
if choice == 1:
    # ADD STUDENT
    name = input("Enter name : ")
    subject = input("Enter subject : ")
    city = input("Enter city : ")
    
    value = (name,subject,city)

    str = "insert into STUDENT (name,subject,city) value ('%s','%s' ,'%s')"
    mycursor.execute(str % value)
    mydb.commit()
    print("successfilly data inserted !!!")

elif choice == 2:
    # VIEW STUDENT
    query = "select * from STUDENT"
    mycursor.execute(query)

    data = mycursor.fetchall()

    print(data)

elif choice == 3:
    #UPDATE STUDENT
    student_id = int(input("Enter the student ID to update: "))
    new_name = input("Enter new name: ")
    new_subject = input("Enter new subject: ")
    new_city = input("Enter new city: ")

    query = "UPDATE STUDENT SET name=%s, subject=%s, city=%s WHERE id=%s"
    values = (new_name, new_subject, new_city, student_id)

    mycursor.execute(query , values)
    mydb.commit()

    print("Successfully updated student data!")

elif choice == 4:
    # DELETE STUDENT
    student_id = int(input("Enter the student ID to delete: "))

    query = "DELETE FROM STUDENT WHERE id=%s"
    value = (student_id,)

    mycursor.execute(query, value)
    mydb.commit()

    print("Successfully deleted the student!")

elif choice == 5:
    # SPECIFIC STUDENT
    student_id = int(input("Enter the student ID to view: "))

    query = "SELECT * FROM STUDENT WHERE id=%s"
    value = (student_id)

    mycursor.execute(query % value)
    data = mycursor.fetchall()

    if len(data) == 0:
        print("Student not found!")
    else:
        print(data)

elif choice == 6:
    # EXIT
    print("Exiting the program.")
    # mycursor.close()  
    # mydb.close()      
    exit()              