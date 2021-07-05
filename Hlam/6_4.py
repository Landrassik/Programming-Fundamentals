line = input().split(',')
man = int(input())

start_index = 0
count_many = 0
total = []

for i in range(1, man + 1):
    for j in line[start_index::man]:
        count = int(j)
        count_many += count
    total.append(count_many)
    count_many = 0
    start_index += 1
print(total)
