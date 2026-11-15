marks = [76, 88, 91]

print(marks[5])


def count():
    return count()


count()

import math

num = int(input("Enter a whole number:"))
print(f"You entered num:{num}")

try:
    num = int(input("Enter a whole number:"))
    print(f"You entered num:{num}")
except ValueError:
    print("This is not a whole number..")

try:
    first = float(input("Enter 1st number:"))
    second = float(input("Enter 2nd number:"))
    result = print(f"Sum of boths numbers are:{first + second}")
except ValueError:
    print("Please enter correct value!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
