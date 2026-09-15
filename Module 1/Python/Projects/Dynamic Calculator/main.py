raw_num1 = input("Enter 1st Number: ").strip()
if not raw_num1:
    print("❌ Error: Field cannot be empty!")
else:
    num1 = float(raw_num1)

raw_num2 = input("Enter 2st Number: ").strip()
if not raw_num2:
    print("❌ Error: Field cannot be empty!")
else:
    num2 = float(raw_num2)

operation = input("Enter Operation you want to perform: ").strip()

if operation == "+":
    print(f"Addition of {num1} and {num2} is:", num1 + num2)
elif operation == "-":
    print(f"Subtraction of {num1} and {num2} is:", num1 - num2)
elif operation == "*":
    print(f"Multiplication of {num1} and {num2} is:", num1 * num2)
elif operation == "/":
    print(f"Division of {num1} and {num2} is:", num1 / num2)
elif operation == "%":
    print(f"Modulus of {num1} and {num2} is:", num1 % num2)
elif not operation:
    print("❌ Error: Field cannot be empty!")
else:
    print("Enter Valid Input!")
