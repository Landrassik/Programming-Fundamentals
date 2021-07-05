line = input()

command = input()

while not command == "Done":
    command = command.split()
    if command[0] == "TakeOdd":
        line = "".join([line[i] for i in range(len(line)) if i % 2 != 0])
        print(line)

    elif command[0] == "Cut":
        index, length = command[1:]
        index = int(index)
        length = int(length)
        line = "".join([del_index for del_index in line[:index]] + [del_index for del_index in line[index + length:]])
        print(line)
    elif command[0] == "Substitute":
        substring, substitute = command[1:]
        if substring in line:
            line = line.replace(substring, substitute)
            print(line)
        else:
            print("Nothing to replace!")


    command = input()
print(f"Your password is: {line}")