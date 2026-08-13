first_item = input("Enter the first item: ")
second_item = input("Enter the second item: ")
third_item = input("Enter the third item: ")
fourth_item = input("Enter the fourth item: ")


first_item_price = float(input("Enter the first item price: "))
second_item_price = float(input("Enter the second item price: "))
third_item_price = float(input("Enter the third item price: "))
fourth_item_price = float(input("Enter the fourth item price: "))
 
total = int ( first_item_price+second_item_price+third_item_price+ fourth_item_price)

print("total:",total)


if(total>=200):
     print("YOU WILL GET 10% DISCOUNT!!" , total/10-total)

else:
    print("YOU WILL GET 5% DISCOUNT!! ",total/5-total)