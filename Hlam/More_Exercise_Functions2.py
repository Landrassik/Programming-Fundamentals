def distance(num1, num2, num3, num4):
    result_1 = num1 * num2
    result_2 = num3 * num4
    if abs(result_1) < abs(result_2):
        return print(f'({int(num1)}, {int(num2)})({int(num3)}, {int(num4)})')
    elif abs(result_1) > abs(result_2):
        return print(f'({int(num3)}, {int(num4)})({int(num1)}, {int(num2)})')
    return print(f'({int(num1)}, {int(num2)}) ({int(num3)}, {int(num4)})')


def difference(num1, num2, num3, num4, num5, num6, num7, num8):
    result_1 = num1 * num2
    result_2 = num3 * num4

    result_3 = num5 * num6
    result_4 = num7 * num8

    result_at_first = abs(result_1) - abs(result_2)
    result_at_last = abs(result_3) - abs(result_4)

    if abs(result_at_first) > abs(result_at_last):
        return [num1, num2, num3, num4]
    elif abs(result_at_first) < abs(result_at_last):
        return [num5, num6, num7, num8]
    return [num1, num2, num3, num4]


x = float(input())
y = float(input())
x2 = float(input())
y2 = float(input())

last_x = float(input())
last_y = float(input())
last_x2 = float(input())
last_y2 = float(input())
result_difference = difference( x, y, x2, y2, last_x, last_y, last_x2, last_y2)
result_distance = distance(result_difference[0], result_difference[1], result_difference[2], result_difference[3])
