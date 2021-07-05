line = input().split()
n = int(input())
x = []
end = n - 1

while len(line) > 0:
    if end + n in range(len(line)-1):
        for i in line[end::n]:
            x.append(i)
            end = line.index(i)
            line.remove(i)
    else:
        end = len(line) - 1 - n
        for i in line[end::n]:
            x.append(i)
            end = line.index(i)
            line.remove(i)

print("[", end='')
print(','.join(x), sep=',', end=']')