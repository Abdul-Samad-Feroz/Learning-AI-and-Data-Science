# Tuples
x = 10
print(type(x))

x = (10,)
print(type(x))

numbers = (10, 20, 30, 40, 50)
print(numbers[1:3])

print(numbers.count(10))

print(type(numbers))


def get_students():
    return "Ali", 85, 91


details = get_students()
print(details)

student = {"name": "Ali", "age": 18, "city": "Karachi", "postal": 74700}
