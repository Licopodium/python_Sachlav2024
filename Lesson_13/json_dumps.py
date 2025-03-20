import json

dict_to_json = {"name": "John", "age": 30, "city": "New York"}

data = json.dumps(dict_to_json)
print(data) # '{"name": "John", "age": 30, "city": "New York"}' # <- payload
print(type(data))   