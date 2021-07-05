line_fire = input().split("#")
n_liter_woter = int(input())

type_cells_and_volue = []
cell = []
Effort = 0
Total_Fire = 0

for i in line_fire:
    type_cells_and_volue = i.split(' = ')
    type_of_Fire = type_cells_and_volue[0]
    range_cells = int(type_cells_and_volue[1])

    if type_of_Fire == 'High':
        if not 81 <= range_cells <= 125:
            continue

    elif type_of_Fire == 'Medium':
        if not 51 <= range_cells <= 80:
            continue
    elif type_of_Fire == 'Low':
        if not 1 <= range_cells <= 50:
            continue
    if n_liter_woter < range_cells:
        continue
    cell.append(range_cells)
    n_liter_woter -= range_cells
    Effort += range_cells * 25 / 100
    Total_Fire += range_cells

print('Cells:')
for j in cell:
    print(f" - {j}")
print(f'Effort: {Effort:.2f}')
print(f'Total Fire: {Total_Fire}')

