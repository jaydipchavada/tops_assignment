status = True 

while status:
    num = int(input("Enter number : "))
    if num%2==0:
        print("Even number ")
    else:
        print("Odd number ")

    check = input("do you want to contiue ? press y  for yes and n for no :  ")
    if check == 'y' or  check == 'yes' :
        status = True
    else:
        status = False
    
   
else:
    print("exit")