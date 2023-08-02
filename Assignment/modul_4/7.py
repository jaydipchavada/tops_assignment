"""
7) Write a Python program to read a file line by line store it into a variable ?
=>

"""
with open ("simple.txt","r") as f :
        lines = f.readlines()
        print(lines)