product_and_count = input()

products_key = {}

while product_and_count != "statistics":
    product_and_count = product_and_count.split(": ")
    key = product_and_count[0]
    value = int(product_and_count[1])

    if key not in products_key:
        products_key[key] = 0
    products_key[key] += value
    product_and_count = input()

print("Products in stock:")
for (key, value) in products_key.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products_key.keys())}")
print(f"Total Quantity: {sum(products_key.values())}")