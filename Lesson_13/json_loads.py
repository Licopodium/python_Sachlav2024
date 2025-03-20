import json

json_from_web = '{ "name":"John", "age":30, "city":"New York"}'

data = json.loads(json_from_web)
print(data)
print(data["name"])
print(type(data))