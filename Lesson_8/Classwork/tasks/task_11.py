experience = int(input('Enter your experience: (range of 1-3): '))

match experience:
    case 1:
        print("You're a beginner.")
    case 2:
        print("You're an intermediate.")
    case 3:
        print("You're an expert.")
    case _:
        print("There is an invalid choice.")
