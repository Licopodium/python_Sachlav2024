number: int = int(input())
print(number > 0)

# with conditional statement
if number > 0:
    print(f"A number '{number}' is positive")
elif number == 0:
    print(f"A number '{number}' is ZERO")
else:
    print(f"A number '{number}' is negative")