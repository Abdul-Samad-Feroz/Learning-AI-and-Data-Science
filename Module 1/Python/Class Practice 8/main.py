students = ["anas", "sana", "ali", "ahmed", "saad"]

name = input("Enter a Name: ")
if name in students:
    print("Student Found!")
else:
    print("Student not Found!")


# Findig the Index(Position) of an item
position = students.index("ali")
print(position)


if "hassan" in students:
    print(students.index("hassan"))
else:
    print("Student not Found!")


name = input("Enter a Name: ")
if name in students:
    print(f"Student Found! - Index Number: {students.index(name)}")
else:
    print("Student not Found!")

numbers = [10, 30, 20, 40, 10, 90, 10, 10]
print(numbers.count(10))

marks = [10, 50, 60, 50, 10, 90, 10, 10]
print(marks.count(50))

students.insert(1, "haris")
print(students)

numbers.insert(3, 30)
print(numbers)

marks.sort()
print(marks)

print(students)
del students[4]
print(students)

# 2D Lists:
data = [[20, 30, 60], [10, 30, 80], [60, 85, 75]]

print(data[0])
print(data[1][2])
print(data[2][0])


for i in data:
    for j in i:
        print(j)


for student in data:
    total = 0
    for mark in student:
        total += mark
    print(total)

for student in data:
    total = 0
    for mark in student:
        total += mark
    print(total / 3)

student = [["Ali", 80, 75, 88], ["Ahmed", 72, 81, 76], ["Sara", 91, 89, 95]]

for i in student:
    total = 0
    for j in i[1:]:
        total += j
    print(total)
