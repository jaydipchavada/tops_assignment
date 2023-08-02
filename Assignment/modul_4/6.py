"""
6) Write a Python program to read a file line by line and store it into a list ?
=>

"""
fname = open("simple.txt","r")
a = fname.readlines()
print(a)