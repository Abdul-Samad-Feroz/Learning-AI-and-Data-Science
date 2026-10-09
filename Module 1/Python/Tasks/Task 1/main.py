# Task 1
products = int(input("how many different products you have purchased? "))
name = []
price = []
quantity = []
itemTotal = []
for i in range(products):
    print(f"\nProduct {i+1}")
    Name = input("Name: ")
    Price = float(input("Price: "))
    Quantity = int(input("Quantity: "))
    allItem = Price * Quantity
    itemTotal.append(allItem)
    name.append(Name)
    price.append(Price)
    quantity.append(Quantity)

subTotal = sum(itemTotal)


if subTotal >= 10000:
    discount = subTotal * 10 / 100
    finalBill = subTotal - discount
elif subTotal >= 5000:
    discount = subTotal * 5 / 100
    finalBill = subTotal - discount
else:
    discount = 0
    finalBill = subTotal


print("================================")
print("        SUPERMARKET BILL        ")
print("================================\n")

for i in range(products):
    print(f"{name[i]:<13} {quantity[i]:<2} x {price[i]:<5} = {itemTotal[i]}")

print(f"\nSubtotal: {subTotal}")
print(f"Discount: {discount}")
print(f"Final Bill: {finalBill}\n\n")


print("    Thank you for shopping!     ")
print("================================")
