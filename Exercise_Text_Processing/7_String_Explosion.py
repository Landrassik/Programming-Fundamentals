elements = input()
result = ""
current_explosions = 0

for i in range(len(elements)):
    if elements[i] == ">":
        result += elements[i]
        current_explosions += int(elements[i + 1])
    else:
        if current_explosions == 0:
            result += elements[i]
        else:
            current_explosions -= 1

print(result)