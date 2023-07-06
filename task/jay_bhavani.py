menu = """"
           vdapav : 40
           dabeli : 30
           bhel   : 70
           burger : 100


"""





menu = {
    "vdapav" : 40,
    "dabeli" : 30,
    "bhel" : 70,
    "burger" : 100
}

Total_bill = 0
amount = 0
order = ()
multiplier = 0
next = 0


print(menu)

status = True

while status:
    amount = 0
    order =input("Enter item name : ").lower()
    multiplier = int(input("How many would you like to order ? : "))

    amount = menu.get(order)
    # if order == 'vadapav':
    #     amount =40
    # elif order == 'dabeli' :
    #     amount = 30
    # elif order == 'bhel':
    #     amount = 70
    # elif order == 'burger' :
    #     amount = 100
    amount = amount*multiplier
    Total_bill = Total_bill + amount
    next = int(input("Press 1 to order further or 2 to exit : "))
    if next == 1 :
        continue
    elif next == 2 :
        status = False
        

print(f"Total bill is {Total_bill}")