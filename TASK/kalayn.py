import logic_jwellers

print("\nWelcome to kalyan Jwellers\N{person with Folded Hands}")
   
status = True
while status:
     
    yourname = input("Enter your name : ")
    gender = input("Enter your Gender(male,female) : ")
    age = int(input("Enter your age : "))

    print("--------------------------------------------------\n")

    productname = input("Enter product name : ")
    productgram = int(input("Enter product gram : "))

    print("----------------------------------------------------\n")

    print(logic_jwellers.shopping(yourname,gender,age,productname,productgram))




    check = input("Do you want to shoping continue ? press y for yes and n for no : ").lower()
    if check == 'y':
        status = True
    elif check == 'n':
        status = False
    else:
        print("Enter vaild input ")