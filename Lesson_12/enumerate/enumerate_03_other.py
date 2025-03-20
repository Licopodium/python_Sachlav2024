my_tuple = ("status", 'id', 'date', 'assign_to')

for elem in enumerate(my_tuple, start=-1):
    print(elem)

for index, elem in enumerate(my_tuple, start=1):
    print(index, elem)