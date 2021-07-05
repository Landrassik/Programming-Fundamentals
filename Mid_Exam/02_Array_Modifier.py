def command_swap(index1, index2, line):
    line[index1], line[index2] = line[index2], line[index1]
    return line


def command_multiply(index1, index2, line):
    line[index1] = line[index1] * line[index2]
    return line


def command_decrease(line):
    result = [i - 1 for i in line]
    return result


line_num = [int(i) for i in input().split()]
command = input()

while not command == "end":

    if not command == "decrease":
        result = line_num
        word_command, index1, index2 = command.split()
        index1 = int(index1)
        index2 = int(index2)

        if word_command == "swap":
            result = command_swap(index1, index2, line_num)
        elif word_command == "multiply":
            result = command_multiply(index1, index2, line_num)

    elif command == "decrease":
        word_command = command
        result = command_decrease(line_num)
    line_num = result
    command = input()
print(", ".join([str(f) for f in result]))