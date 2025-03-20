age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are an adult!")
# else:
#     print("You need to grow!")

# print("You are an adult!") if age >= 18 else print("You need to grow!")

message = None
if age >= 18:
    message = "You are an adult!"
else:
    message = "You need to grow!"

print(message)

message = "You are an adult!" if age >= 18 else "You need to grow!"

print(f"{message = }")