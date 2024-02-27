contacts={
    "number": 4,
    "students":
    [
        {"name":"Student One", "email":"student1@example.com"},
        {"name":"Student Two", "email":"student2@example.com"},
        {"name":"Student Three", "email":"student3@example.com"},
        {"name":"Student Four", "email":"student4@example.com"}
    ]
}

print("Student emails: ")
for student in contacts["students"]:
    print(student["email"])