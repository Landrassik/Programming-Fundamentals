item_in_colection = input().split("&")
command = input()
while command != 'None':
    command, item = command.split()
    if command == 'Swap Books':
        old_item, new_item = item.split(" | ")
        if old_item in item_in_colection and new_item in item_in_colection:
            temp = 0
            item_in_colection.insert(item_in_colection.index(old_item)+1, new_item)
    elif command == 'Collect':
        if item not in item_in_colection:
            item_in_colection.append(item)


    elif command == 'Drop':
        if item in item_in_colection:
            item_in_colection.remove(item)

    else:
        if item in item_in_colection:
            item_in_colection.remove(item)
            item_in_colection.append(item)

    command = input()

print(', '.join(item_in_colection))