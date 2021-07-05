n = int(input())
count_hero = {}

for _ in range(1, n + 1):
    hero, HP, MP = input().split()
    HP = int(HP)
    MP = int(MP)

    if hero not in count_hero:
        count_hero[hero] = {"HP": HP, "MP": MP}

command = input()

while not command == "End":
    command = command.split(" - ")
    if command[0] == "Attack":
        hero_name, MP_needed, spell_name = command[1:]
        MP_needed = int(MP_needed)
        if hero_name in count_hero and count_hero[hero_name]["MP"] >= MP_needed:
            count_hero[hero_name]["MP"] -= MP_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {count_hero[hero_name]['MP']} MP!")
        elif hero_name in count_hero and count_hero[hero_name]["MP"] < MP_needed:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
        else:
            continue

    elif command[0] == "TakeDamage":
        hero_name, damage, attacker = command[1:]
        damage = int(damage)
        if hero_name in count_hero:
            count_hero[hero_name]["HP"] -= damage
        if count_hero[hero_name]["HP"] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {count_hero[hero_name]['HP']} HP left!")
        if count_hero[hero_name]["HP"] <= 0:
            del count_hero[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")


    elif command[0] == "Recharge":
        hero_name, amount = command[1:]
        amount = int(amount)
        if hero_name in count_hero:
            chek = 200 - count_hero[hero_name]["MP"]
            count_hero[hero_name]["MP"] += amount
            if count_hero[hero_name]["MP"] > 200:
                count_hero[hero_name]["MP"] = 200
                print(f"{hero_name} recharged for {chek} MP!")
            else:
                print(f"{hero_name} recharged for {amount} MP!")

    elif command[0] == "Heal":
        hero_name, amount = command[1:]
        amount = int(amount)
        if hero_name in count_hero:
            chek = 100 - count_hero[hero_name]["HP"]
            count_hero[hero_name]["HP"] += amount
            if count_hero[hero_name]["HP"] > 100:
                count_hero[hero_name]["HP"] = 100
                print(f"{hero_name} healed for {chek} HP!")
            else:
                print(f"{hero_name} healed for {amount} HP!")
    command = input()

filter_hero = sorted(count_hero.items(), key=lambda kvp: (-kvp[1]["HP"], kvp[0]))

for k, v in filter_hero:
    print(k)
    print(f"HP: {v['HP']}\nMP: {v['MP']}")

