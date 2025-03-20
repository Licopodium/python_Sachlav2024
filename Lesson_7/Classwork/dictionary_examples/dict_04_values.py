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

all_values = my_dictionary.values()
print(all_values)
print(type(all_values))
print(list(all_values))
print(tuple(all_values))