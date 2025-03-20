password = input("Enter a password: ")
confirm_password = input("Enter a confirmation password: ")

if len(password) < 7:
    print("Short")
elif password != confirm_password:
    print("Difference")
else:
    print("OK")


