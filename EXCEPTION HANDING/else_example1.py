try:
    num1 = int(input("Enter your number 1 : "))
    num2 = int(input("Enter your number 2 : "))

    ans = num1 / num2
except Exception as e:
    print(e)
else:
    print(ans)
finally:
    print("THANK YOU FOR USING APPLICATION")