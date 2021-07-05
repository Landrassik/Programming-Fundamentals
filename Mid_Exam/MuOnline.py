line_room = input().split("|")
room = 0
hp = 100
bitcoins = 0
for i in line_room:
    comand, number = i.split()
    number = int(number)
    if comand == 'potion':

        if hp + number <= 100 :
            hp += number
            print(f"You healed for {number} hp.")
            print(f"Current health: {hp} hp.")
        else:
            print(f"You healed for {100 - hp} hp.")
            print(f"Current health: 100 hp.")
            hp = 100
    elif comand == 'chest':
        print(f"You found {number} bitcoins.")
        bitcoins += number
    else:
        hp -= number
        if hp > 0:
            print(f"You slayed {comand}.")
        else:
            print(f"You died! Killed by {comand}.")
    room += 1
    if hp <= 0:
        break
if len(line_room) == room and hp > 0:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {hp}")
else:
    print(f"Best room: {room}")