from calculator_module import calculate

try:
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    operation = input("Enter math operation (+, -, *, /): ")

    result = calculate(x, y, operation)
    print(f"Result of {x} {operation} {y} is: {result}")

except ValueError as e:
    print(f"Error: {e}")