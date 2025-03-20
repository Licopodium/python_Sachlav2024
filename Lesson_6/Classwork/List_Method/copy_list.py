list_1 = ["1", "2", "3"]

list_2 = list_1

list_1[0] = "0"

print(list_1)
print(list_2)
print(id(list_1))
print(id(list_2))

list_3 = list_1[:]
list_1[0] = "1"
print(list_1)
print(list_3)
print(id(list_1))
print(id(list_3))