import json

with open("data.json", "r") as file_to_read:
    loaded_data = json.load(file_to_read)
    print(loaded_data)
    print(loaded_data["data"]["name"])
    print(type(loaded_data))