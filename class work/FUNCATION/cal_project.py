# calculator

menu = """
                menu

        press 1 for addition
        press 2 for multiplication
        press 3 for substraction
        press 4 for division
            
"""

def sum():
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    ans = num1 + num2
    print(ans)    

def mul():
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    ans = num1 * num2
    print(ans)

def sub():
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    ans = num1 - num2
    print(ans)

def div():
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    ans = num1 / num2
    print(ans)

status = True
while status:
    print(menu)
    choice = int(input("Enter your choice : "))
    if choice == 1:
        sum() # calling
    elif choice == 2:
        mul()
    elif choice == 3:
        sub()
    elif choice == 4:
        div()
    else :
        print("Wrong choice")
        break


continue_choice = input("do you want to perfrom more operation press y for yes and press n for no : ")
if continue_choice == 'y':
    status = True
else :
    status = False