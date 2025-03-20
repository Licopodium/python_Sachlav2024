age = int(input("Enter your age: "))

if 18 < age <= 120:
    print("You are an adult!")
elif age == 18:
    print("Your age is 18.")
else:
    print("You need to grow!")


print("You are an adult!") if 18 < age <= 120 else print("Your age is 18.") if age == 18 else print("You need to grow!")