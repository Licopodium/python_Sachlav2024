my_dictionary = {
    "name": "alex",
    "age": 36,
    "is_living_in_israel": True,
    "username": "Alexander",
    "languages": ['TS', "Python", "Java"],
    "coordinates": {
        'long': 25.67,
        'lat': 12.56
    },
}

all_items = my_dictionary.items()
print(all_items)
print(type(all_items))
print(list(all_items))
print(tuple(all_items))

# for pair in my_dictionary.items():
#     print(f"{pair[0]} - {pair[1]}")