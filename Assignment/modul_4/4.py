"""
4) Write a Python program to read first n lines of a file ?
=>
"""
L = int(input("Enter Number of line want to read : "))
file = open("simple.txt","r")
for i in range(L):
    print(file.readline())
    
file.close()