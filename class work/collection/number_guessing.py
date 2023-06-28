import random

computer = random.randint(1,100)

status = True
while status:
    num = int(input("enter number : "))
    if num > computer:
        print("HINT : Guess lower number  ")
    elif num < computer:
        print("HINT : Guess upper number  ")
    else:
        print("YOU WIN !!!!!!!")
        status = False
        # check = input("do you want to contiue ? press y  for yes and n for no :  ")
        # if check == 'y' or  check == 'yes' :
        #     status = True
        # else:
        #     status = False