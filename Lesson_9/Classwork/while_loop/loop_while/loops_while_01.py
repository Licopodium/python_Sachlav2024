
# a = -10
#
# while a <= 10:
#     print(".......")
#     print(a)
#     a += 1

text = input("Enter your word or 'exit' to finish: ")
print(f"You entered '{text}'")

while text != "exit":
    print(f"You entered '{text}'")
    text = input("Enter your word or 'exit' to finish: ")

print("Bye!")