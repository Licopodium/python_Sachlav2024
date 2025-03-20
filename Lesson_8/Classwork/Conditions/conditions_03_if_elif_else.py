age = int(input("Enter your age: "))

if 18 < age <= 120:
    print("You are an adult!")
    print(f"Your age is {age}")
elif age > 120:
    print("Not a legal age!")
elif age == 18:
    print("Your age is 18.")
else:
    print("You need to grow!")

print("After if block")