import pprint
my_dictionary = {
    "name": "alex",
    "age": 36,
    "is_living_in_israel": True,
    "name": "Alexander",
    "username": "Alexander",
    "languages": ['TS', "Python", "Java"],
    "coordinates": {
        'long': 25.67,
        'lat': 12.56
    },
    (12, 14): (),
}

print(len(my_dictionary))
print(my_dictionary)
print(my_dictionary["name"])
# print(my_dictionary["abcabc"]) # Non-existing key -> KeyError

pprint.pprint(my_dictionary)

all_options = {
    1: "A",
    2: "B"
}

print(all_options[1])



