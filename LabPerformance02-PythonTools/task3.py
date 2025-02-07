
n = int(input("Enter the number of students: "))

students = []
for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    age = int(input(f"Enter age of student {i+1}: "))
    grade = int(input(f"Enter grade of student {i+1}: "))
    students.append((name, age, grade))
students = tuple(students)
sorted_students = sorted(students, key=lambda student: student[2])

print("\nStudents sorted by grade:")
for student in sorted_students:
    print(student)
