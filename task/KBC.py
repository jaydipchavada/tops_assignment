price = 0
def que1():
    global price
    print("\n1) bahubali festival is related to")
    mcq = """
            a)islam
            b)hindu
            c)buddhism
            d)jainism
        """
    
    print(mcq)
    choice = input("Enter Your ans : ").lower()
    if choice == 'd':
        print("CURRCT ANS !!!")
        print("YOU WON RS.10000\n")
        price +=10000
    else:
        print("WRONG ANS !!!")
        print(price)

def que2():
    global price
    print("\n2) INDIA PRIME MINISTER ?")
    mcq = """
            a)RAHUL GANDHI
            b)NARENDER MODI
            c)JAY SHAH
            d)LALU YADHAV
        """
    
    print(mcq)
    choice = input("Enter Your ans : ").lower()
    if choice == 'b':
        print("CURRCT ANS !!!")
        print("YOU WON RS.20000\n")
        price +=20000
    else:
        print("WRONG ANS !!!")
        price -= 10000
        print(price)

def que3():
    global price
    print("\n3) MOST POPULER CRICKERT PLAYER ?")
    mcq = """
            a)ROHIT SHARMA
            b)VIRAT KOHLI
            c)DHAWAN
            d)MS DHONI
        """
    
    print(mcq)
    choice = input("Enter Your ans : ").lower()
    if choice == 'd':
        print("CURRCT ANS !!!")
        print("YOU WON RS.30000\n")
        price +=30000
    else:
        print("WRONG ANS !!!")
        print(price)


que1()
que2()
que3()
print("YOU WON TOTAL PRICE : ",price)
