email = "jaydip@gmail.com"
password = "123456"

u_email = input("Enter email : ")
u_password = input("Enter password : ")

if u_email !=email or u_password !=password:
    
    if u_email!=email and u_password!=password:
        print("Invaild email or password")

    elif u_email != email:
        print("Invaild email")

    elif u_password != password:
        print("Invaild password")
   

else:
    print("vaild email or password")