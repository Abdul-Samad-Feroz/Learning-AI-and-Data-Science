products = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor",
    "Printer",
    "Scanner",
    "Speaker",
    "Webcam",
]

# First 3 products
# Last 3 products
# Products from index 2 to 5
# Every second product
# Products at odd indexes
# Reverse the list
# Last 4 products in reverse order
# First 5 products in reverse order
# Print the first 4 products using a loop
# Print the last 3 products using a loop

print(products[:3])
print(products[-3:])
print(products[2:6])
print(products[0::2])
print(products[1::2])
print(products[::-1])
print(products[:-5:-1])
print(products[4::-1])

for i in products[:4]:
    print(i)

for i in products[-3:]:
    print(i)

prices = [250, 500, 1200, 750, 300]

# find total price
# find most expesive
# find cheapest
# how many products are there

# apply 10 % discount if total >= 2500
# print total, discount, and final amount

# ask user for number of items
# ask price of each item
# add each price to a list
# calculate total
# if total > 2500: discount 10% else 0
# print total, discount, final amount

print(sum(prices))
print(max(prices))
print(min(prices))
print(len(prices))

total = sum(prices)

if total >= 2500:
    discount = total * 10 / 100
    finalAmount = total - discount

print(f"total:{total}")
print(f"Discount:{discount}")
print(f"Final Amount:{finalAmount}")

items = int(input("Enter number of items: "))
price = []
for i in range(items):
    price.append(int(input("Enter price of each item: ")))

total = sum(price)

if total > 2500:
    discount = total * 10 / 100
    finalAmount = total - discount
else:
    discount = 0
    finalAmount = total

print(f"total: {total}")
print(f"Discount: {discount}")
print(f"Final Amount: {finalAmount}")
