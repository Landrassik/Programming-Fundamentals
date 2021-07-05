line_with_lut = input().split("|")
command = input()
x = False
while not command == "Yohoho!":
    command = command.split()
    if command[0] == "Loot":
        result = [i for i in command[1:] if not i in line_with_lut]
        result.reverse()
        line_with_lut = result + line_with_lut

    elif command[0] == "Drop":
        index = int(command[1])
        if index in range(len(line_with_lut) + 1):
            line_with_lut.append(line_with_lut.pop(index))

    elif command[0] == "Steal":
        index = int(command[1])
        if index in range(len(line_with_lut) + 1):
            result = [line_with_lut[i] for i in range(len(line_with_lut)) if i >= len(line_with_lut) - index]
            line_with_lut = [f for f in line_with_lut if f not in result]
            print(", ".join(result))
        else:
            print(", ".join(line_with_lut))
            x = True

    command = input()

if x:
    print("Failed treasure hunt.")
else:
    print(f"Average treasure gain: {sum([len(i) for i in line_with_lut]) / len(line_with_lut):.2f} pirate credits.")
