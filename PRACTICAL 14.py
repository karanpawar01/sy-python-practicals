phonebook = {}

print("Welcome to Phonebook Application")

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter mobile number: ")
        phonebook[name] = number
        print("Contact saved successfully!")

    elif choice == "2":
        for name, number in phonebook.items():
            print(name, ":", number)

    elif choice == "3":
        name = input("Enter name to search: ")
        if name in phonebook:
            print("Mobile Number:", phonebook[name])
        else:
            print("Contact not found!")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")