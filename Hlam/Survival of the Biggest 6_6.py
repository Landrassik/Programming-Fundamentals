line = input().split(" ")
n = int(input())
line_int = []

for i in line:
    line_int.append(int(i))
for j in range(n):
    line_int.remove(min(line_int))
print(line_int)