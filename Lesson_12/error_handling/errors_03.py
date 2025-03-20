# x = 2
try:
    print(x / 1)
except NameError:
    print("A NameError is occurred.")
else:
    print("Else block - no errors were found!")