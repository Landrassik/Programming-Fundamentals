line = input().split(', ')
result = []
for i in line:
    if int(i) == 0:
        line.remove(i)
        line.append(i)
for j in line[::]:
    result.append(int(j))
print(result)