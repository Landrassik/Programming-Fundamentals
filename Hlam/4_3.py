def game(index):
    vertical = []
    for i in range(1, 3 + 1):
        if i == 1:
            vertical += line_1[index]
        elif i == 2:
            vertical += line_2[index]
        elif i == 3:
            vertical += line_3[index]
    return vertical


def game_naiskos(index):
    vertical = []
    for i in range(1, 3 + 1):
        if i == 1:
            vertical += line_1[index]
            index += 1
        elif i == 2:
            vertical += line_2[index]
            index += 1
        elif i == 3:
            vertical += line_3[index]
    return vertical


def game_naiskos_r(index):
    vertical = []
    for i in range(1, 3 + 1):
        if i == 1:
            vertical += line_1[index]
            index -= 1
        elif i == 2:
            vertical += line_2[index]
            index -= 1
        elif i == 3:
            vertical += line_3[index]
    return vertical


def chek(line, gamer):
    count = 0
    for i in line[:]:
        if i == gamer:
            count += 1
        else:
            return False
    return True


line_1 = input().split()
line_2 = input().split()
line_3 = input().split()

vertical_left = game(0)
vertical_center = game(1)
vertical_right = game(2)

left_vertikal_right = game_naiskos(0)
right_vertikal_left = game_naiskos_r(2)

total_line = [line_1, line_2, line_3, vertical_left, vertical_center, vertical_right, left_vertikal_right, right_vertikal_left]
x = False
for i in total_line:
    result = chek(i, "1")
    if result:
        print("First player won")
        x = True
        break

for i in total_line:
    result = chek(i, "2")
    if result:
        print("Second player won")
        x = True
        break

if not x:
    print("Draw!")