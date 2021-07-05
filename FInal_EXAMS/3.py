command = input()

Mans_dict = {}

while not command == "Results":
    command = command.split(":")
    if command[0] == "Add":
        personName, health, energy = command[1:]
        health, energy = int(health), int(energy)
        if personName not in Mans_dict:
            Mans_dict[personName] = {"health": health, "energy": energy}
        else:
            Mans_dict[personName]["health"] += health

    elif command[0] == "Attack":
        attackerName, defenderName, damage = command[1:]
        damage = int(damage)
        if attackerName in Mans_dict and defenderName in Mans_dict:
            Mans_dict[defenderName]["health"] -= damage
            Mans_dict[attackerName]["energy"] -= 1
            if Mans_dict[defenderName]["health"] <= 0:
                print(f"{defenderName} was disqualified!")
                del Mans_dict[defenderName]
            if Mans_dict[attackerName]["energy"] == 0:
                print(f"{attackerName} was disqualified!")
                del Mans_dict[attackerName]

    elif command[0] == "Delete":
        username = command[1]
        if username == "All":
            Mans_dict.clear()
        else:
            del Mans_dict[username]
    command = input()
if len(Mans_dict) > 0:
    filter_dict = sorted(Mans_dict.items(), key=lambda x: (-x[1]["health"], x[0]))

    print(f"People count: {len(Mans_dict)}")

    for k, v in filter_dict:
        print(f"{k} - {v['health']} - {v['energy']}")
else:
    print(f"People count: {len(Mans_dict)}")