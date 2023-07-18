f = open("myfile_example1.txt","a")

for i in range(1,4):
    name = input("Enter your name : ")
    score = int(input("Enter your score : "))
    f.write("\n"+name)
    f.write("\n"+str(score))

f.close()

f = open("myfile_example1.txt","r")
print(f.read())

f.close()