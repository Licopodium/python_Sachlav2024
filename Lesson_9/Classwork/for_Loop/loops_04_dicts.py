information_details = {
    "name": "Alex",
    "age": 36,
    "area": "North",
    "is_working": True
}

# for x in information_details: # keys only
#     print(x)
#
# for single_key in information_details.keys(): # keys only
#     print(single_key)

# for single_value in information_details.values():
#     print(single_value)

for item in information_details.items():
    print(item)

# for item in information_details.items():
#     print(f"{item[0]} - {item[1]}")

for item_key, item_value in information_details.items():
    print(f"{item_key} - {item_value}")
