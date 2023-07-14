import logic

product_name = input("Enter your product : ")
product_qty = int(input("Enter Your Qty : "))
product_category = input("Enter Your Category : ")
product_price = int(input("Enter Your price : "))

print(logic.purchase(product_name,product_category,product_qty,product_price))