line_product = input().split('!')
command = input()

while command != 'Go Shopping!':
    command = command.split()
    if len(command) == 2:
        product = command[1]
        if command[0] == 'Urgent':
            if product not in line_product:
                line_product.insert(0, product)
        elif command[0] == 'Unnecessary':
            if product in line_product:
                line_product.remove(product)
        elif command[0] == 'Rearrange':
            if product in line_product:
                line_product.remove(product)
                line_product.append(product)
    elif command[0] == 'Correct':
        old_product = command[1]
        new_product = command[2]
        if old_product in line_product:
            x = line_product.index(old_product)
            line_product[x] = new_product
            # x = line_product.insert(line_product.index(old_product) + 1, new_product)
            # x = line_product.pop(line_product.index(old_product))
    command = input()
print(", ".join(line_product))