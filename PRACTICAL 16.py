balance = 1000

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print("Amount deposited successfully!")
    else:
        print("Invalid amount!")

def withdrawal():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount <= 0:
        print("Invalid amount!")
    elif amount <= balance:
        balance -= amount
        print("Withdrawal successful!")
    else:
        print("Insufficient balance!")

def balance_inquiry():
    print("Available Balance:", balance)

while True:
    print("\n--- Banking Menu ---")
    print("1. Deposit")
    print("2. Withdrawal")
    print("3. Balance Inquiry")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        deposit()
    elif choice == "2":
        withdrawal()
    elif choice == "3":
        balance_inquiry()
    elif choice == "4":
        print("Thank you for using our banking system!")
        break
    else:
        print("Invalid choice! Please try again.")