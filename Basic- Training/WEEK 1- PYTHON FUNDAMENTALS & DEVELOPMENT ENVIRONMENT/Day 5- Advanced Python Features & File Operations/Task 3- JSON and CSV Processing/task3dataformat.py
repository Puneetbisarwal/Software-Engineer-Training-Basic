# 4. Deliverable: Data Format Converter (JSON ↔ CSV ↔ Python objects)

import json
import csv

def json_to_csv(json_file, csv_file):
    with open(json_file, "r") as jf:
        data = json.load(jf)  # Expect list of dicts

    with open(csv_file, "w", newline="") as cf:
        writer = csv.DictWriter(cf, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def csv_to_json(csv_file, json_file):
    with open(csv_file, "r") as cf:
        reader = csv.DictReader(cf)
        data = list(reader)

    with open(json_file, "w") as jf:
        json.dump(data, jf, indent=4)

def python_to_json(obj, json_file):
    with open(json_file, "w") as jf:
        json.dump(obj, jf, indent=4)

def json_to_python(json_file):
    with open(json_file, "r") as jf:
        return json.load(jf)
    

if __name__ == "__main__":
    # Test Python object to JSON and back
    py_data = [
        {"Name": "Aditya", "Age": 18, "City": "Delhi"},
        {"Name": "Rahul", "Age": 22, "City": "Mumbai"}
    ]
    python_to_json(py_data, "test_people.json")
    loaded_py = json_to_python("test_people.json")
    print("Loaded from JSON->Python Object:", loaded_py)

    # Test JSON to CSV
    json_to_csv("test_people.json", "test_people.csv")
    print("CSV created from JSON.")

    # Test CSV to JSON
    csv_to_json("test_people.csv", "test_people_from_csv.json")
    print("JSON created from CSV.")

    # Load back from the new JSON
    loaded_from_csv_json = json_to_python("test_people_from_csv.json")
    print("Loaded from CSV->JSON:", loaded_from_csv_json)
