# If Else & Elif Condition Statements
number = int(input("Enter a Number: "))
if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

if num1 > num2:
    print(num1, "is Greater")
elif num1 == num2:
    print("Both numbers are equal")
else:
    print(num2, "is Greater")


marks = float(input("Enter your marks: "))

if marks >= 90:
    print("A Grade")

elif marks >= 80:
    print("B Grade")

elif marks >= 70:
    print("C Grade")

elif marks >= 60:
    print("D Grade")

else:
    print("Fail")

temperature = float(input("Enter currnet Temperature: "))

if temperature >= 40:
    print("Very Hot")

elif temperature >= 30:
    print("Hot")

elif temperature >= 20:
    print("Pleasent")

else:
    print("Cold")


# Logical Operators
age = int(input("Enter your Age: "))
registration = str(input("Are You Registered? Y/N"))

if age >= 16 and (registration == "Y" or registration == "y"):
    print("You are allowed to enter in the competition!!!")
else:
    print("You are not allowed")

userName = input("Enter Username: ")
password = input("Enter Password: ")

if userName == "admin" and password == "1234":
    print("Login Succesful")
else:
    print("Incorrect Username/Password")
