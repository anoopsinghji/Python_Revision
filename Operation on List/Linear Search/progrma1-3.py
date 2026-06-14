# search for a student in the list using linear search

students = ["Aman", "Rahul", "Priya", "Neha"]

target = "Priya"

for name in students:
    if name == target:
        print("Student Found")
        break
else:
    print("Student Not Found")