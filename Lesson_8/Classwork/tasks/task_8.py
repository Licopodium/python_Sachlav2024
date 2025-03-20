num_1 = int(input("Enter a first number: "))
num_2 = int(input("Enter a second number: "))
num_3 = int(input("Enter a third number: "))

# if num_1 == num_2 == num_3:
#     print(3)
# elif num_1 == num_2 or num_2 == num_3 or num_1 == num_3:
#     print(2)
# else:
#     print(0)

# or

unique_numbers = len({num_1, num_2, num_3})

if unique_numbers == 1:
    print(3)
elif unique_numbers == 2:
    print(2)
else:
    print(0)