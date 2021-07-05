first_line = [int(i) for i in input(" ").split()]
command = input()

while not command == "End":
    index_of_command = int(command)
    if index_of_command in range(len(first_line)):
        shooting = first_line[index_of_command]
        first_line[index_of_command] = -1

        for i in range(len(first_line)):

            if first_line[i] == -1:
                continue
            if first_line[i] > shooting:
                first_line[i] -= shooting
            else:
                first_line[i] += shooting
    command = input()

print(f"Shot targets: {first_line.count(-1)} -> {' '.join([str(f) for f in first_line])}")