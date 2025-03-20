my_tuple = tuple(["1", "2"])
print(my_tuple)

my_tuple_2 = ("a", 'b', "c")
print(my_tuple_2)

not_tuple = ("abc")
print(not_tuple)
print(type(not_tuple))

new_tuple = ("abc",)
print(new_tuple)
print(type(new_tuple))

tuple_no_brackets = "a", 3, True, ['a', 'b'], (1, ["a", "c"])
print(tuple_no_brackets)
print(tuple_no_brackets[-1][1][0])
print(len(tuple_no_brackets))