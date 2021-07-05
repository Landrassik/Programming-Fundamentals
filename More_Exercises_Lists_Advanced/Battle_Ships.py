n = int(input())
start = 0
rectangle = []
count = 0

for i in range(n):
    command = [int(i) for i in input().split()]
    rectangle.append(command)

atak = "".join(input().split())
atak = "".join(atak.split("-"))

for count_atack in range(0, len(atak), 2):
    row, col = atak[start: start + 2]
    row = int(row)
    col = int(col)
    if int(rectangle[row][col]) > 1:
        rectangle[row][col] = rectangle[row][col] - 1
    elif int(rectangle[row][col]) == 1:
        rectangle[row][col] = rectangle[row][col] - 1
        count += 1
    start += 2
print(count)