day = int(input("Enter a day number (1-7): "))

if day == 1:
    print("Sunday")
elif day == 2:
    print("Monday")
elif day == 3:
    print("Tuesday")
elif day == 4:
    print("Wednesday")
elif day == 5:
    print("Thursday")
elif day == 6 or day == 7:
    print("Weekend!!!")
else:
    print("Invalid day number. Please enter a number between 1 and 7.")


match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case num if num in range(6, 8): # case 6 | 7
        print("Weekend!")
    case _:
        print("Invalid day number. Please enter a number between 1 and 7.")