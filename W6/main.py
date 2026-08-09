from discount import final_price, TAX_RATE

products = [
    ("Laptop", 85000, 10),
    ("Headphones", 4500, 15),
    ("Phone Case", 800, 5),
    ("USB Cable", 600, 0),
]

print("Tax Rate:", TAX_RATE)

print("\nProducts")

for product in products:

    name = product[0]
    price = product[1]
    discount = product[2]

    final = final_price(price, discount)

    print(name)
    print("Original Price: NPR", price)
    print("Final Price: NPR", round(final, 2))
    print()