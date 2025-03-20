my_tuple = (1, 2, 3, 4, False, 4, "name", False, [])

print(my_tuple.index(3))
print(my_tuple.index("name"))
print(my_tuple.index(False))
print(my_tuple.index(True))
# print(my_tuple.index("0")) # ValueError

print(my_tuple.count("0"))
print(my_tuple.count(False))
print(my_tuple.count("name"))
print(my_tuple.count(True))
