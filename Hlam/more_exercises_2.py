
line = input().split()
num = int(input())
start = -1
start_j = 0
lol = line
x = ''
y = []
for number in range(len(line)):

    for i in range(start, len(line), num):
        if i != start:
            x += line[i]
    start = i
    for j in range(start_j, len(line)):
        if line[j] in x:
            continue
        else:
            line.append(line[j])
    start_j = j

for f in x:
    y.append(map(int, f.split(" ")))
print(y)
