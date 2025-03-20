my_tuple = (1, "Alex", 3, False, 4, "name", False)
print(type(my_tuple))
print(my_tuple)
print(f"{id(my_tuple) = }")

converted_tuple_to_list = list(my_tuple)
print(type(converted_tuple_to_list))
print(converted_tuple_to_list)
converted_tuple_to_list[1] = "Alexander"
print(converted_tuple_to_list)
my_tuple = tuple(converted_tuple_to_list)
print(my_tuple)
print(f"{id(my_tuple) = }")