# define functions for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# prompt the user to enter two numbers and select an operation
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Select operation:")
print("1. Add")
print("2. Sub")
print("3. Multi")
print("4. Div")

# take user input for operation choice
choice = input("Enter choice (1/2/3/4): ")

# perform the selected operation and print the result
if choice == '1':
    print(num1, "+", num2, "=", add(num1,num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1,num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1,num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1,num2))

else:
    print("Invalid input")
