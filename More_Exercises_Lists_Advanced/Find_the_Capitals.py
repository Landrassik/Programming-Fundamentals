line = input()
print([i for i in range(len(line)) if 60 <= ord(line[i]) <= 90])