my_list = [10, 20, 30, 40]
print(enumerate(my_list))
print(type(enumerate(my_list)))

print(list(enumerate(my_list)))

for index, item in enumerate(my_list):
    print(index, item)