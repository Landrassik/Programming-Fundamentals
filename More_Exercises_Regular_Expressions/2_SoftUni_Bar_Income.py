import re

command = input()
patern = r"(?<=\%)(?P<Costumer_name>[A-Z][a-z]+)(?=\%)|(?<=\<)(?P<Product>[A-Z]\w+)(?=\>)|(?<=\|)(?P<Count>\d+)(?=\|)|(?P<Price>(\d+.\d+)|(\d+))(?=\$)"

total_money = 0
while not command == "end of shift":
    match = [i.group() for i in re.finditer(patern, command)]
    if len(match) == 4:
        name, product, count, price = match[:]
        total_money += int(count) * float(price)
        print(f"{name}: {product} - {int(count) * float(price):.2f}")

    command = input()
print(f"Total income: {total_money:.2f}")

