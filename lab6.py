print("******Expenses******")

Expenses = 0.0
food = 0.0
travels = 0.0
shopping = 0.0
other = 0.0


while True:
    value = float(input("enter your value:"))

    if value==-1:
        break


    category =str(input("Enter a category(food/shopping/travels/other):")).lower()

    if category == "food":
        food +=value

    elif category == "shopping":
        shooping +=value

     elif category == "travels":
        travels +=value

     else :
          other += value

        Expenses += value

    

print("\n******expenses details******")
print("food :",food)
print("travel:",travels)
print("shopping:",shopping)
print("other:",other)
print("total Expenses:",Expenses)