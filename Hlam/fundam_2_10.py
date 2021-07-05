#  Ornament Set – 2$ a piece
#  Tree Skirt – 5$ a piece
#  Tree Garlands – 3$ a piece
#  Tree Lights – 15$ a piece

quantity = int(input())
days = int(input())
x = 0
christmas_spirit = 0
budget = 0
ornament_Set = 2 #nabor
tree_Skirt = 5 #yubka dlya derev
tree_Garlands = 3#girlyandi
tree_Lights = 15#fonari

for i in range(1, days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        budget += ornament_Set * quantity
        christmas_spirit += 5
    if i % 3 == 0:
        budget += (tree_Skirt + tree_Garlands) * quantity
        christmas_spirit += 13
    if i % 5 == 0:
        budget += tree_Lights * quantity
        christmas_spirit += 17
        if i % 3 == 0:
            christmas_spirit += 30


    if i % 10 == 0:
        budget += tree_Skirt + tree_Garlands + tree_Lights
        christmas_spirit -= 20

    if i == days and i % 10 == 0:
        christmas_spirit -= 30





print(f"Total cost: {budget}")
print(f"Total spirit: {christmas_spirit}")