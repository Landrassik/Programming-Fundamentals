collecting_items = [i for i in input().split(", ")]
command = input()

while not command == "Craft!":
    word_command = command.split(" - ")
    if word_command[0] != "Combine Items":
        item = word_command[1]
        if word_command[0] == "Collect" and item not in collecting_items:
            collecting_items.append(item)

        elif word_command[0] == "Drop" and item in collecting_items:
            collecting_items.remove(item)

        elif word_command[0] == "Renew" and item in collecting_items:
            collecting_items.append(item)
            collecting_items.remove(item)

    else:
        olditem, neitem = word_command[1].split(":")
        if olditem in collecting_items:
            index = collecting_items.index(olditem)
            collecting_items.insert(index + 1, neitem)

    command = input()


print(', '.join(collecting_items))