menu1 ="""
    vadapav : 80
    dabeli  : 90
    burger  : 70
    bhel    : 90
    
"""
menu = {
     
   "vadapav" :80,
    "dabeli"  : 90,
    "burger" : 70,
    "bhel"    : 90
    
}
print(menu1)
bill_amt = 0
total_bill=0
status = True
while status:
    
    for i in range(0,len(menu)):
        
        item_name = input("Enter Item Want to Oreder : ").lower()
        item_qty =  int(input("Enter Item Want to Qty : "))

        if item_name in menu:
            bill_amt = item_qty * menu.get(item_name)
            print("bill_amt : ",bill_amt)
            total_bill +=bill_amt         
            order_more = input("Want to add More Item(y/n) : ").upper()
            if order_more == "Y" or order_more == "YES":
                    continue
            else:
                    status =False
                    break  
        else:
            print("Enter Valid Name")
         
    print("TOTAL BILL AMT : ",total_bill)
    
