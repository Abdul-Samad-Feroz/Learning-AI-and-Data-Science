print("Anas")
print("Anas")
print("Anas")
print("Anas")
print("Anas")


# For Loop
for i in range(5):
    print("A.Samad")

print(range(5))

for i in range(7):
    print(i)

for i in range(10):
    print(i)

for i in range(11):
    print("Python is fun")

# range(start, stop, step)
for i in range(1, 9, 2):
    print(i)

for i in range(10, -1, -1):
    print(i)


for i in range(2, 21, 2):
    print(i)

for i in range(1, 20, 2):
    print(i)

for i in range(5, 51, 5):
    print(i)


# Loop + Arithmetic

table = int(input("Enter Table number: "))

for i in range(1, 11):
    print(table, "X", i, "=", table * i)

name = input("Enter a Name you want to print: ")
times = int(input("How many times do you want to print this name? "))

for i in range(times):
    print("#", i + 1, name)


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

total = 0
for i in range(10):
    number = 1 + i
    total = number + total
print(total)

totalNum = 0
for i in range(100):
    num = 1 + i
    if num % 2 == 0:
        totalNum = num + totalNum
print("Sum of even numbers from 1 to 100 is:", totalNum)

count = 0
for i in range(20):
    nums = 1 + i
    if nums % 2 == 0:
        count += 1
print("Count of even numbers between 1 to 20 is:", count)
