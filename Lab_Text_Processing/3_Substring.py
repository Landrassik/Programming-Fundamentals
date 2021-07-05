word = input()
line = input()

while word in line:
    line = line.replace(word, "")
print(line)