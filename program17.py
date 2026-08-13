print("<********************** PASSWORD VERIFICATION ********************>")
correct_password = "admin123"

while True:
    password = input("Enter your password: ")

    if password == correct_password:
        print("Access Granted")
        break
    else:
        print("Wrong Password. Try Again.")