# Task 1
products = int(input("how many different products you have purchased? "))

all_products = []
sTotal = 0
for i in range(products):
    # product = []
    name = input(f"Enter Product {i+1} Name: ")
    price = int(input(f"Enter Product {i+1} Price: "))
    quantity = int(input(f"Enter Product {i+1} Quantity: "))
    I_total = price * quantity

    all_products.append({
        "name": name,
        "price": price * quantity
    })

print(all_products)     