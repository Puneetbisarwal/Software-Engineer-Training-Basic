# 2. CSV Module Basics

import csv

rows = [
    ["Name", "Age", "City"],
    ["Ajay", 25, "Pata"],
    ["Aditya", 30, "Goa"]
]

with open("people.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
    
# Reading CSV

with open("people.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# Using DictWriter / DictReader

# Writing
with open("people_dict.csv", "w", newline="") as f:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Name": "Akash", "Age": 25, "City": "Patna"})
    writer.writerow({"Name": "Nimish", "Age": 30, "City": "Goa"})

# Reading
with open("people_dict.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], row["Age"])
        print(row)
        

# 3. Data Serialization & Deserialization

import json

json_data = '[{"Name": "Arjun", "Age": 23}, {"Name": "Varun", "Age": 26}]'
py_obj = json.loads(json_data)   # JSON → Python list
print(py_obj[0]["Name"])         # Access "Arjun"
print(py_obj[1]["Name"])         # Access "Varun"

