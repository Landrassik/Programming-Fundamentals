line = input()
result = []
for i in range(0, len(line)):
    if not i == 0:
        if ord(line[i - 1]) == ord(line[i]):
            continue
        else:
            result.append(line[i])
    else:
        result.append(line[i])
print("".join(result))