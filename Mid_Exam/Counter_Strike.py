first_line = int(input())
command = input()
great_battle = 0
while not command == "End of battle":

    distance = int(command)
    if first_line >= distance:
        first_line -= distance
        great_battle += 1
        if great_battle % 3 == 0:
            first_line += great_battle
    else:
        print(f"Not enough energy! Game ends with {great_battle} won battles and {first_line} energy")
        break
    command = input()
else:
    print(f"Won battles: {great_battle}. Energy left: {first_line}" )