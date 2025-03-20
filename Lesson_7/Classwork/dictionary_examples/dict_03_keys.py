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

all_keys = my_dictionary.keys()
print(all_keys)
print(type(all_keys))
print(list(all_keys))
print(tuple(all_keys))