try :
    num1 = int(input("enter number 1: "))
    num2 = int(input("Enter number 2: "))

    ans = num1 / num2
    print(ans)

except ValueError:
    print("int vallue requied")
except ZeroDivisionError:
    print("cannot be divided by zero")