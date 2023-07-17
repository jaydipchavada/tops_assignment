WelcomeDisplay = """
                                WELCOME TO FRUIT MARKET

                                1)  MANAGER
                                
                                2)  CUSTOMER
"""
ManagerDisplay = """
                                WELCOME TO FRUIT MARKET

                                1)  Add Fruirt Stock
                                
                                2)  Viwe Stock

                                3)  Update Stock

"""

products = {}       # Creat Blank Dictionary to Store Stock Data 
order = {}      # Creat Blank Dictionary to Store Customer Order Data 
total_bill = 0      # initialize Customer Bill Value  
status = True
while status :
    print(WelcomeDisplay)       # user can see welcome display
    role = int(input("Select Your Role (1/2) :"))       # User have to Select Role
    if role == 1:       # User Select 1) Manager Role
        main_m_status = True
        while main_m_status:
            print(ManagerDisplay)       # Manager Panel
            m_role = int(input("Select Your Role (1/2) :"))
            if m_role == 1:     # Manager Select    1) Add Fruirt Stock 
                m_status = True
                while m_status:
                    sub_product = {}
                    
                    item_name = input("Enter Item Name : ").upper()     # Taking Item Name From User
                    item_qty = int(input("Enter Item Qty : "))      # Taking Item Qty From User
                    item_price = float(input("Enter Item Price : "))        ## Taking Item Price From User

                    if item_name is products :      # Check Item Item Already Exist or not
                        old_qty = products[item_name]['qty']    # Getting Qty of Already Exist Item
                        sub_product["qty"]= item_qty + old_qty      # Updating Qty of Already Exist Item
                    else :
                        sub_product['qty'] = item_qty       # Creat New Item Qty 
                        sub_product['price'] = item_price       # Creat New Item price
                    products[item_name] = sub_product       # Creat New Item With Stock and Price Data
                    
                    check = input("Do you want add more items ? (y/n) : ").upper()      # Check Want to Add More Item Or Not
                    if check == "Y" or check == "YES":
                        m_status = True
                    else:
                        m_status = False            
            
            elif m_role == 2:       # Manager Select    2) Viwe Stock   
                print("\n --------------------------------- STOCK DETAILS ------------------------------------- \n")
                
                for k,v in products.items() :
                    print(f"Item Name : {k} \tQty : {v['qty']} \tPrice :{v['price']} ")  # Display Stock Data

            elif m_role == 3:
                u_status = True
                while u_status :
                    print(" ------------------------------ CURRENT STOCK DETAILS ------------------------------- ")
                    for k,v in products.items() :
                        print(f"Item Name : {k} \tQty : {v['qty']} \tPrice :{v['price']} ")         # Display Stock Data
                    
                    item_name = input("Enter Item Name : ").upper()         # Getting Item Name Want to Update
                    
                    if item_name in products :      # Check Item is exist or not
                        
                        update_qty = int(input("Enter Item Qty : "))        # Getting Updated Item Qty
                        update_price = float(input("Enter Item Price : "))      # Getting Updated Item Price
                        products[item_name]['qty'] = update_qty         # Update Item Qty
                        products[item_name]['price'] = update_price     # # Update Item Price
                        
                    else :
                        print("Item Not Available Please Add Item Firts")       # If Item Not in Stock

                    check = input("want to Update more items ? (y/n) : ").upper()        # Check Want to Update More Item Or Not
                    if check == "Y" or check == "YES":
                        u_status = True
                    else:
                        u_status = False  

            check = input("Back to Manager Panel (y/n) : ").upper()         # Taking Manager input
            if check == "Y":
                main_m_status = True
            else : 
                main_m_status = False
        
    elif role == 2: 
        
        print("\n = = = = = = = = = = = = = = = = = = =  WELCOME TO FRUIT STORE = = = = = = = = = = = = = = = = = = = \n")      # Customer Welcome Message
        c_status = True
        while c_status :
            print("\n = = = = = = = = = = = = = = = = = = =  MENU  = = = = = = = = = = = = = = = = = = = \n")
            for k,v in products.items() :
                print(f"Item Name : {k} \tMax. Order Qty : {v['qty']} \tPrice :{v['price']} ")              # Printing Menu
            
            order_item = input("Enter Name : ").upper()         # Getting Order Item Name
            order_qty = int(input("Enter Qty : "))              # Getting Order Item Qty
            sub_order = {}                                      # Creat Blank Dictionary 
            order[order_item]=sub_order                         # Store sub oder details to main dictionary

            if order_item in products:                          # Check Enter Item is Avialable or Not.

                if order_qty <= products[order_item]['qty']:    # Check Order Qty Is according to Scock Data
                    
                    item_total =order_qty * products[order_item]['price']  # Displai Item Total 
                    print("Item Total : ", item_total)

                    products[order_item]['qty'] -= order_qty            # Update Qty to Stock Data
                    sub_order['qty'] = order_qty                        # add details for Order Summery
                    sub_order['price'] = item_total                     # add details for Order Summery
                    total_bill += item_total                            # Adding Item Total

                    order[order_item]=sub_order                         # Store Ordder Details to Main Order Dictionary
                else :
                    print("You Can't Order More Then Max. Order Qty")   # If Customer Order More Then Max Order Qty
            else : 
                    print("Enter Valid Item Name ")                     # If Customer Enter Name Which is Not not Stock
                

            check = input("Want to order More (y/n) : ").upper()        # Check Cust Want to Oder More Item
            if check == "Y":
                c_status = True
            else : 
                c_status = False

        print("\n = = = = = = = = = = = = = = = = = = =  Order Summary = = = = = = = = = = = = = = = = = = = \n")
        for k,v in order.items():
            print(f"Item : {k} \tQty : {v['qty']} \tRs. : {v['price']}")      # Printing Order Summery
        print("============= \t TOTAL BILL AMT : ",total_bill,"\t ============")      # Printting Total Bill Amt Of Cust Order
    else:
        print("Enter Valid Input")

    check = input("Exit (y/n) : ").upper()          # Check Want to Repet 
    if check == "Y":
        status = False
    else : 
        status = True
