# 1. JSON Module Basics
# Serialization (Python → JSON string)

import json

data = {"name": "Ajay", "age": 25, "city": "Patna"}
json_str = json.dumps(data)  # Python dict → JSON string
print(json_str)


# Deserialization (JSON string → Python object)

data_back = json.loads(json_str)
print(data_back["name"], data_back["age"])  # "Ajay", 25
print(data_back)


# File-based Operations

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

with open("data.json", "r") as f:
    data_file = json.load(f)
    print(data_file["name"], data_file["city"])  # "Ajay", "Patna"
    print(data_file)
