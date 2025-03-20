num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second numer: "))

minimum = num1 if num1 < num2 else num2
maximum = num1 if num1 > num2 else num2

print(minimum, maximum)