# Task 1: Basic Arithmetic Operations
# Perform addition, subtraction, and multiplication on two given numbers.
num1 = 10
num2 = 5

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

print("Task 1: Basic Arithmetic Operations")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}\n")

# Task 2: Complex Arithmetic Expression
# Calculate the result of: x - (y / (1 + x * y))
x = 3
y = 2

complex_result = x - (y / (1 + x * y))

print("Task 2: Complex Arithmetic Expression")
print(f"Result of x - (y / (1 + x * y)): {complex_result}\n")

# Task 3: Regular and Geometric Average
# Find the average of two numbers in two different ways
num3 = 12
num4 = 8

regular_average = (num3 + num4) / 2
geometric_average = (num3 * num4) ** 0.5

print("Task 3: Regular and Geometric Average")
print(f"Regular Average of {num3} and {num4}: {regular_average}")
print(f"Geometric Average of {num3} and {num4}: {geometric_average}\n")

# Task 4: Hypotenuse and Area of a Triangle
# Calculate the hypotenuse and area of a triangle
a = 6
b = 8

# Hypotenuse (using Pythagoras' theorem)
hypotenuse = (a**2 + b**2) ** 0.5

# Area of the triangle
area = 0.5 * a * b

print("Task 4: Hypotenuse and Area of a Triangle")
print(f"Hypotenuse of triangle with sides {a} and {b}: {hypotenuse}")
print(f"Area of triangle with sides {a} and {b}: {area}")
