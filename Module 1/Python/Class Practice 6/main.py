# Array
marks = [10, 20, 30]

total = 0

for i in marks:
    total += i
print(total)


# Slicing

students = ["Ali", "Usman", "Ahmed", "Javed", "Anas"]

print(students[0:3])
# [start, stop]

print("Huzaifa" in students)

name = input("Enter Student Name: ")
if name in students:
    print("Found")
else:
    print("Not found")

print(students)

students.insert(1, "Farhan")
print(students)

students.pop(2)
print(students)

students.remove("Javed")
print(students)

students.insert(2, 55)
print(students)

students.reverse()
print(students)

students.reverse()
print(students)

numbers = [10, 20, 30, 40, 50]
print(numbers[0:2])

print(numbers[1:4])

print(numbers[:3])  # Starts from the beginning and stop before 3
print(numbers[2:])  # Starts at index 2 and go till the end

print(numbers[:])  # From start to end  OR
print(numbers)  # Same as above

print(numbers[-3:])

num = int(input("Enter a Number: "))
if num in numbers:
    print("Found")
else:
    print("Not found")

number = [10, 20, 10, 30, 10, 40, 10, 50]
count = 0
for i in number:
    if i == 10:
        count += 1
print(count)

print(number.count(10))

number.sort()
print(number)

number.sort(reverse=True)
print(number)

letters = ["r", "s", "v", "t", "j", "a", "w"]
letters.sort()
print(letters)

letters.sort(reverse=True)
print(letters)

numberss = [10, 20, 30, 40, 50]

print(max(numberss))
print(min(numberss))
print(sum(numberss))
print(len(numberss))

# Average
print(sum(numberss) / len(numberss))

prices = [250, 500, 1200, 750, 300]

print(sum(prices))
print(max(prices))
print(min(prices))
print(len(prices))
