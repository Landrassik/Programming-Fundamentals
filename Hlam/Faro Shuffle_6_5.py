line = input().split(" ")
count_num = int(input())
left = []
right = []

for i in range(1, count_num + 1):
    x = []
    half = int(len(line) / 2)
    left = line[0:half]
    right = line[half::]
    for card in range(len(left)):
        x.append(left[card])
        x.append(right[card])
    line = x
print(line)