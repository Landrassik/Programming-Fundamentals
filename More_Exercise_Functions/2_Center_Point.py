from math import sqrt


def distance(x1, y1, x2, y2):
    if sqrt((x1 + y1) ** 2 < (x2 + y2) ** 2):
        return int(x1), int(y1)
    elif sqrt((x1 + y1) ** 2 > (x2 + y2) ** 2):
        return int(x2), int(y2)
    else:
        return int(x1), int(y1)


x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())

result = [i for i in distance(x1, x2, y1, y2)]
result.sort()
result = [str(i) for i in result]

if len(result) == len(set(result)):
    print(f"({', '.join(result)})")
else:
    print(f"({''.join(result[0])})")