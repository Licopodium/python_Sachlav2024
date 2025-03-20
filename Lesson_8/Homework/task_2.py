number_of_month = int(input("Enter a number of month (1-12): "))

match number_of_month:
    case 1:
        print("31")
    case 2:
        print("28")
    case 3:
        print("31")
    case 4:
        print("30")
    case 5:
        print("31")
    case 6:
        print("30")
    case 7:
        print("31")
    case 8:
        print("30")
    case 9:
        print("31")
    case 10:
        print("30")
    case 11:
        print("31")
    case 12:
        print("30")

    case _:
        print("Invalid number. Please enter a number of month between 1 and 12.")

        print("-------------------------")

        month = int(input("Enter a month number: "))

        match month:
            case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                print("31")
            case 4 | 6 | 9 | 11:
                print("30")
            case 2:
                print("28")
            case _:
                print("Invalid month")