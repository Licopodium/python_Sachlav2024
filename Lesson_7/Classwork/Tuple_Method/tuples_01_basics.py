my_list = [1, 2, 3, 4, False, 4, "name", False, ()]
my_tuple = (1, 2, 3, 4, False, 4, "name", False, ())

print(my_list)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[3])
print(my_tuple[-2])

print(3 in my_tuple)
print(5 in my_tuple)

print(my_list.__sizeof__())
print(my_tuple.__sizeof__())