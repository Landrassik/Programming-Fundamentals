line_car = input().split()
granica = len(line_car) // 2

left_car = line_car[:granica:]
right_car = line_car[:granica:-1]

count_car = left_car, right_car
result = 0

for i in range(len(count_car)):
    for f in count_car[i]:
        if int(f) != 0:
            result += int(f)
        else:
            result *= 0.8
    if i == 0:
        left_car = result
    right_car = result
    result = 0
if right_car > left_car and right_car != left_car:
    result = left_car
    print(f"The winner is left with total time: {result:.1f}")
else:
    result = right_car
    print(f"The winner is right with total time: {result:.1f}")

