# 1. Master File Operations
# Opening a file

file = open("example.txt", "w")   # open file for writing
file.write("Hello, world!")
file.close()                      # must close to save changes

# Reading a file

file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# 2. File Modes

# 'r' → Read (file must exist)
# 'w' → Write (creates/overwrites file)
# 'a' → Append (adds to file without deleting)
# 'rb' / 'wb' → Binary read/write (images, PDFs, etc.)


# Append new line
with open("log.txt", "a") as f:
    f.write("New entry added\n")
    f.close()
    

file = open("log.txt", "r")
content = file.read()
print(content)
file.close()


# 3. Context Managers (with)

with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())
        
        
# 4. Working with Different File Formats

with open("notes.txt", "w") as f:
    f.write("First line\nSecond line\n")
    
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)
    
    
# CSV (Comma Separated Values)

import csv

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Score"])
    writer.writerow(["Akash", 95])
    writer.writerow(["Akshay", 88])
    
with open("data.csv", "r") as f:
    content = f.read()
    print(content)
    
# JSON (structured storage)

import json

data = {"name": "Aditya", "age": 25, "city": "Mumbai"}
with open("user.json", "w") as f:
    json.dump(data, f, indent=4)

with open("user.json", "r") as f:
    content = json.load(f)
    print(content)
    

# 5. Deliverable: File Backup Utility

import shutil
import os

def backup_file(source, destination):
    """Backup a file with error handling."""
    try:
        if not os.path.exists(source):
            raise FileNotFoundError(f"Source file {source} does not exist.")

        shutil.copy(source, destination)
        print(f"Backup successful: {source} → {destination}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage
backup_file("example.txt", "backup_example.txt")

