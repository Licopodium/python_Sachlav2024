age = int(input("Enter your age: "))

if 18 <= age <= 120:
    print("You are an adult!")
    print(f"Your age is {age}")
elif age == 18:
    print("Your age is 18.")
elif age != 120:
    print("Not a legal age!")
else:
    print("You need to grow!")

print("-------------------------")

if 18 <= age <= 120:
    print("You are an adult!")
    print(f"Your age is {age}")
if age == 18:
    print("Your age is 18.")
if age != 120:
    print("Not a legal age!")
else:
    print("You need to grow!")

