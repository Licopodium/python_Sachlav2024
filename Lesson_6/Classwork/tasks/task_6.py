numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


a = 0
a += numbers.pop(-1)
a += numbers.pop(0)
a += numbers.pop(12)
a += numbers.pop(7)
print(f"{numbers = }")
print(f"{a = }")
