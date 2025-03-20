value = int(input("Enter your age: "))

if value %3==0:
    print("FizzBuzz")
elif value %5==0:
    print("FizzBuzz")
else:
    print(value)

print("-------------------------")

  #  if value % 5 == 0 and value % 3 == 0:
#     print("FizzBuzz")
# else:
#     print(f"{value = }")

# 3. Print "Fizz" if the Value Is a Multiple of Three, and "Buzz" if it's a Multiple of Five
if value % 5 == 0 and value % 3 == 0:
    print("FizzBuzz")
elif value % 3 == 0:
    print("Fizz")
elif value % 5 == 0:
    print("Buzz")
else:
    print(f"{value = }")