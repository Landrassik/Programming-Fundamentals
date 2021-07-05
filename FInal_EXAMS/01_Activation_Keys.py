def Contains(x):
    if x in line:
        return True
    return False

def Slice(start, end):
    x = line[:start] + line[end:]
    return x

def Flip(command, start, end):
    if command[1] == "Upper":
        x = line[:start] + line[start:end].upper() + line[end:]
    elif command[1] == "Lower":
        x = line[:start] + line[start:end].lower() + line[end:]
    return x

line = input()

command = input()

while not command == "Generate":
    command = command.split(">>>")
    if command[0] == "Contains":
        result = Contains(command[1])
        if result:
            print(f"{line} contains {command[1]}")
        else:
            print(f"Substring not found!")

    elif command[0] == "Slice":
        start = int(command[1])
        end = int(command[2])
        line = Slice(start, end)
        print(line)

    elif command[0] == "Flip":
        start = int(command[2])
        end = int(command[3])
        line = Flip(command, start, end)
        print(line)

    command = input()

print(f"Your activation key is: {line}")