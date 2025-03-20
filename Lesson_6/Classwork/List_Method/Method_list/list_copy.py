list_to_add = [4, 5, 6]
my_list = [1 ,2, 3]
my_list.append(list_to_add)
print(my_list)
new_list = my_list.copy()


print(new_list)
print(id(my_list))
print(id(new_list))