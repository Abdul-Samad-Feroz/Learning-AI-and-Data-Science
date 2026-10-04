text = "I love Java"
text = text.replace("Java", "Python")
print(text)

name = input("Enter a Valid name: ")
if name.isalpha():
    print("Valid Name!")
else:
    print("Invalid Name!")

value = "12.5"
print(value.isdigit())

# For alphabets and number both
username = "Ahmed123"
print(username.isalnum())

name = "python"
print(name.islower())

password = input("Enter Password: ")
if password.isalpha():
    print("You have enterd only letter!")
elif password.isdigit():
    print("You have entered only Digit!")
elif password.isalnum():
    print("Password Accepted!")
else:
    print("Error!")

text = "Python is easy"
print(text.find("Python"))

text = "Python is easy and Python is new"
print(text.rfind("Python"))

filename = "Position.final.report.pdf"
position = filename.rfind(".")

extension = filename[position + 1 :]
print(extension)

email = "abc@gmail.com"
result = email.partition("@")

print(result)

# f-string
name = "Abdul Samad"
age = 16

print(f"My name is {name} and my ag is {age}")

average = 10 / 3
print(average)

print(f"{average:.1f}")

salary = 2500000
print(salary)
print(f"Salary: Rs. {salary:,}")

empid = input("Enter Employ id: ")
if empid.startswith("EMP") and len(empid) == 8 and empid[3:].isdigit():
    print("Valid id!")
else:
    print("Invalid Id!")

# # Write a program to validate a specific format
# of a vehicle license plate. The format requires:
# # • The first 3 characters must be alphabetic letters
#  (uppercase or lowercase)
# # • The next character must be a hyphen (-)
# # • The last 3 characters must be digits
# # • Total length must be exactly 7 characters
# # • Sample Valid ID: ABC-123

numberPlate = input("Enter your vehicle licence plate: ")
# print(numberPlate[-3:])

if (
    numberPlate[:3].isalpha()
    and numberPlate[3:4] == "-"
    and numberPlate[-3:].isdigit()
    and len(numberPlate) == 7
):
    print("Correct Format!")
else:
    print("Invalid Format!")
