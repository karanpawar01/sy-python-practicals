print("====expenses====")
expenses=0.0
food=0.0
shopping=0.0
travel=0.0
other=0.0 


while True:
    value=float(input("Enter your amount"))
    if value==-1:
            break

    category=str(input("Enter a category(food/shopping/trvael/others):")).lower()  

    if category=="food":
        food +=value
    elif category=="shopping":
        shopping +=value
    elif category=="travel":
        travel +=value
    else:
        other +=value

    expenses += value

print("\n===== Expense Summary =====")
print("Food:", food)
print("Shopping:", shopping)
print("Travel:", travel)
print("Other:", other)
print("Total Expenses:", expenses)