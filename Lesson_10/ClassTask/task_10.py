def multiply(*arguments):
    a = 1
    for elem in arguments:
        a *= elem
    return a


print(multiply(1, 2, 3))
print(multiply(1, 3))
print(multiply())
print(multiply(0, 2, 3))