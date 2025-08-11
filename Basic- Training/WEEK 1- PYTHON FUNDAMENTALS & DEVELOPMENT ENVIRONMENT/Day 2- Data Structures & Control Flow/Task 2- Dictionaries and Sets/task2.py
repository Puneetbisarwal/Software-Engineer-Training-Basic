# 1. Basic Dictionary
student = {"name": "Alice", "age": 20, "grade": "A"}

print(student)
# Keys, Values, Items
print(student.keys())   # dict_keys(['name', 'age', 'grade'])
print(student.values()) # dict_values(['Alice', 20, 'A'])
print(student.items())  # dict_items([('name', 'Alice'), ('age', 20), ('grade', 'A')])

# get()
print(student.get("grade"))       # 'A'
print(student.get("height", "N/A")) # Default if key doesn't exist

# update()
student.update({"grade": "B", "city": "New York"})
print(student)

# pop()
removed_age = student.pop("age")
print("Removed age:", removed_age)
print(student)


set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "cherry", "date", "fig"}

# Union
print(set1.union(set2))

# Intersection
print(set1.intersection(set2))

# Difference
print(set1.difference(set2))



# -------------------------------
# STUDENT GRADE MANAGEMENT SYSTEM
# -------------------------------

students = {}  # {roll_no: {"name": str, "grades": set()}}

def add_student(roll_no, name):
    """Add a new student to the system."""
    students[roll_no] = {"name": name, "grades": set()}

def add_grade(roll_no, subject):
    """Add a subject grade to a student."""
    if roll_no in students:
        students[roll_no]["grades"].add(subject)
    else:
        print("Student not found!")

def remove_student(roll_no):
    """Remove a student from the system."""
    return students.pop(roll_no, None)

def display_students():
    """Display all students and their grades."""
    for roll_no, info in students.items():
        print(f"{roll_no}: {info['name']} — Grades: {', '.join(info['grades']) if info['grades'] else 'No grades yet'}")

# Example usage
add_student(1, "Akash")
add_student(2, "Bhavna")

add_grade(1, "Math")
add_grade(1, "Science")
add_grade(2, "English")

display_students()

remove_student(2)
display_students()


