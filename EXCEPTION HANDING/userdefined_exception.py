class checkodddata(Exception):
    pass

num = int(input("Enter your number : "))
try :
    if num%2==0:
        print("Even number")
    else:
        raise checkodddata
except:
    print("odd data entered")
    