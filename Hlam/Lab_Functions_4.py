def total_price(product, n):
    if product == "coffee":
        return 1.50 * n
    elif product == "water":
        return 1.00 * n
    elif product == "coke":
        return 1.40 * n
    elif product == "snacks":
        return 2.00 * n

name_product = input()
quantiti = int(input())

result = total_price(name_product, quantiti)
print(f"{result:.2f}")