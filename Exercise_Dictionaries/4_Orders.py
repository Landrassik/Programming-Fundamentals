command = input()
total_products = {}

while not command == "buy":
    command = command.split()
    name, price, quantity = command[:]
    price, quantity = float(price), float(quantity)
    if name not in total_products: total_products[name] = [price, quantity]
    elif name in total_products: total_products[name][1] += quantity
    if name in total_products and price not in total_products[name]: total_products[name][0] = price
    command = input()
print('\n'.join([f"{k} -> {v[0] * v[1]:.2f}" for k, v in total_products.items()]))
