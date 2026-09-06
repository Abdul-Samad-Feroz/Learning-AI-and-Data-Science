for i in range(10, 0, -2):
    print(i)

for i in range(1, 6):
    print(i * 10)


total = 0
for i in range(6):
    total = total + i  # Accumulator
print(total)

total = 0
for i in range(11):
    total = total + i
print(total)

total = 0
n = int(input("Enter the Num Range: "))
for i in range(1, n + 1):
    total = total + i
    print(total)

totalNum = 0
for i in range(1, 101):
    if i % 2 == 0:
        totalNum = totalNum + i
print("Sum of even numbers from 1 to 100 is:", totalNum)

totalNum = 0
for i in range(1, 101):
    if i % 2 != 0:
        totalNum = totalNum + i
print("Sum of odd numbers from 1 to 100 is:", totalNum)

count = 0
for i in range(1, 21):
    if i % 2 == 0:
        count = count + 1
print("Count of even numbers between 1 to 20 is:", count)

count = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        count += 1
print(count)

# Student Marks Manager
student = int(input("Enter number of Students: "))
total = 0
passed = 0
failed = 0
largest = 0
smallest = float("inf")
for i in range(student):
    marks = float(input("Enter Marks: "))
    total = total + marks
    if marks >= 50:
        passed = passed + 1
    else:
        failed = failed + 1
    if marks > largest:
        largest = marks
    elif marks < smallest:
        smallest = marks
print("\nLargest Marks:", largest)
print("Smallest Marks:", smallest)
print("Total:", total)
print("Average:", total / student)
print("Passed Students:", passed)
print("Failed Students:", failed)


# Homework Practice
number = int(input("Enter a Number:"))
largest = number

for i in range(4):
    number = int(input("Enter a Number:"))
    if number > largest:
        largest = number
print("Largest:", largest)

number = int(input("Enter a Number:"))
largest = number
