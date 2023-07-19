import datetime

vaccation = """


                vaccation  2023 


"""
print(vaccation)

name = input("Enter your name : ").upper()
email =str(input("Enter Your email : ")).lower()
age = int(input("Enter your age : "))
gender = input("Enter your gender : ").upper()
vaccingname = input("Enter vaccingname : ").upper()
vaccationdoze = int(input("Enter Your doze(1/2) : "))

#date = datetime.datetime.now()
today = str(datetime.date.today())
a = today

print("------------------------------------------------")

f = open("ID"+str(a)+".txt","a")

f.write("\n name : "+name)
f.write("\n email : "+email)
f.write("\n age : " +str(age))
f.write("\n gender : "+gender)
f.write("\n vaccingname : "+vaccingname)
f.write("\n vaccationdoze(1/2) : "+str(vaccationdoze)+"\n")
f.write(str(today))

f.close()



#print("today = ",date.today())
# print("month = ",today.month)
# print("year = ",today.year)