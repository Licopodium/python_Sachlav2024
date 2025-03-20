my_dictionary = {
    "name": "alex",
    "age": 36,
    "is_living_in_israel": True,
}

print(my_dictionary["name"])
print(my_dictionary.get("name"))

# print(my_dictionary["nameeeeee"]) # KeyError
print(my_dictionary.get("nameeeeee"))

key_to_find = "nameeeeee"
print(my_dictionary.get(key_to_find, f"A key '{key_to_find}' was not found..."))

key_to_find = "name"
print(my_dictionary.get(key_to_find, f"A key '{key_to_find}' was not found..."))