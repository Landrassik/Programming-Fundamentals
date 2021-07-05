def fire(index, war_ship):
    if index in range(len(war_ship)):
        return True
    return False


pirat_ship = [int(i) for i in input().split(">")]
war_ship = [int(i) for i in input().split(">")]
max_hp = int(input())

command = input()

while not command == "Retire":
    command = command.split()

    if command[0] == "Fire":
        index, value = int(command[1]), int(command[2])
        if fire(index, war_ship):
            if war_ship[index] - value <= 0:
                print("You won! The enemy ship has sunken.")
                exit()
            war_ship[index] -= value
        else:
            command = input()
            continue

    elif command[0] == "Defend":
        start_index, end_index, damage = int(command[1]), int(command[2]), int(command[3])
        if fire(start_index, pirat_ship) and fire(end_index, pirat_ship):
            if len(pirat_ship[start_index: end_index + 1]) == len([f for f in pirat_ship[start_index: end_index + 1] if f - damage > 0]):
                pirat_ship[start_index: end_index + 1] = [j - damage for j in pirat_ship[start_index: end_index + 1]]
            else:
                print("You lost! The pirate ship has sunken.")
                exit()
        else:
            command = input()
            continue

    elif command[0] == "Repair":
        index, health = int(command[1]), int(command[2])
        if fire(index, pirat_ship):
            if pirat_ship[index] + health >= max_hp:
                pirat_ship[index] = max_hp
            else:
                pirat_ship[index] += health
    elif command[0] == "Status":
        status = [h for h in pirat_ship if h < max_hp * 0.20]
        print(f"{len(status)} sections need repair.")
    command = input()
print(f"Pirate ship status: {sum(pirat_ship)}")
print(f"Warship status: {sum(war_ship)}")
