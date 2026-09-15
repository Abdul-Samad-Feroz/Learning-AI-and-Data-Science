raw_num1 = input("Enter 1st Number: ").strip()
if not raw_num1:
    print("❌ Error: Field cannot be empty!")
    exit()
else:
    try:
        num1 = float(raw_num1)
    except ValueError:
        print("❌ Error: Please enter a valid number!")
        exit()

raw_num2 = input("Enter 2nd Number: ").strip()
if not raw_num2:
    print("❌ Error: Field cannot be empty!")
    exit()
else:
    try:
        num2 = float(raw_num2)
    except ValueError:
        print("❌ Error: Please enter a valid number!")
        exit()

operation = input("Enter Operation you want to perform: ").strip()

if operation == "+":
    print(f"Addition of {num1} and {num2} is:", num1 + num2)
elif operation == "-":
    print(f"Subtraction of {num1} and {num2} is:", num1 - num2)
elif operation == "*":
    print(f"Multiplication of {num1} and {num2} is:", num1 * num2)
elif operation == "/":
    if num2 == 0:
        print("❌ Error: Cannot divide by zero!")
        exit()
    else:
        print(f"Division of {num1} and {num2} is:", num1 / num2)
elif operation == "%":
    if num2 == 0:
        print("❌ Error: Cannot calculate modulus with zero!")
        exit()
    else:
        print(f"Modulus of {num1} and {num2} is:", num1 % num2)
elif not operation:
    print("❌ Error: Field cannot be empty!")
    exit()
else:
    print("Invalid Input!")
