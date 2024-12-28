a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

results = [a + b + c, a * b * c, a * (b + c), (a + b) * c, a + b * c, a * b + c]

print(max(results))



