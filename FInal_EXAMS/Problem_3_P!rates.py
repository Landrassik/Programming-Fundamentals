command = input()
line_of_dict = {}
while not command == "Sail":
    town, people, gold = command.split("||")
    people = int(people)
    gold = int(gold)
    if town not in line_of_dict:
        line_of_dict[town] = {"peoples": people, "gold": gold}
    else:
        line_of_dict[town]["peoples"] += people
        line_of_dict[town]["gold"] += gold
    command = input()

command_2 = input()

while not command_2 == "End":
    command_2 = command_2.split("=>")
    if command_2[0] == "Plunder":
        town_after = command_2[1]
        people_after = int(command_2[2])
        gold_after = int(command_2[3])

        line_of_dict[town_after]["peoples"] -= people_after
        line_of_dict[town_after]["gold"] -= gold_after
        print(f"{town_after} plundered! {gold_after} gold stolen, {people_after} citizens killed.")
        if line_of_dict[town_after]["peoples"] <= 0 or line_of_dict[town_after]["gold"] <= 0:
            del line_of_dict[town_after]
            print(f"{town_after} has been wiped off the map!")

    elif command_2[0] == "Prosper":
        town_after = command_2[1]
        gold_after = int(command_2[2])
        if gold_after > 0:
            line_of_dict[town_after]["gold"] += gold_after
            print(f"{gold_after} gold added to the city treasury. {town_after} now has {line_of_dict[town_after]['gold']} gold.")
        else:
            print(f"Gold added cannot be a negative number!")





    command_2 = input()

filter_dict = sorted(line_of_dict.items(), key=lambda kvp: (-kvp[1]["gold"], kvp[0]))

print(f"Ahoy, Captain! There are {len(line_of_dict.keys())} wealthy settlements to go to:")

for k, v in filter_dict:
    print(f"{k} -> Population: {line_of_dict[k]['peoples']} citizens, Gold: {line_of_dict[k]['gold']} kg")