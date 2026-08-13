customer_name = input("ENTER CUSTOMER NAME:>")

product_name = input("ENTER PRODUCT NAME:>")

feedback = input("ENTER CUSTOMER FEEDBACK:>")

customer_name  = customer_name .center(50).upper()
product_name = product_name .center(50).upper()
feedback=feedback .capitalize().replace("GOOD","BEST").center(50)

print("*=====*FEEDBACK*=====*")
print("CUSTOMER NAME :>",customer_name)
print("PRODUCT NAME :>",product_name)
print("FEEDBACK :>",feedback)

print("*=====* TQ FOR YOUR FEEDBACK*=====*")