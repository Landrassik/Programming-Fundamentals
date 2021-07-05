def value_count_index(index, len_line_moving):
    if index in range(len(len_line_moving)):
        return True
    return False


line_moving = [int(i) for i in input().split()]
command = input()

while not command == "End":
    command_name, index, power = command.split()
    index = int(index)
    power = int(power)

    if command_name == "Shoot":
        if value_count_index(index, line_moving):
            if line_moving[index] - power <= 0:
                line_moving.pop(index)
            else:
                line_moving[index] -= power

    elif command_name == "Add":
        if value_count_index(index, line_moving):
            line_moving.insert(index, power)
        else:
            print("Invalid placement!")

    elif command_name == "Strike":
        left_radius = index - power
        right_radius = index + power
        if value_count_index(index, line_moving) and value_count_index(left_radius, line_moving) and value_count_index(right_radius, line_moving):
            del line_moving[left_radius:right_radius + 1]
        else:
            print("Strike missed!")
    command = input()

print("|".join([str(f) for f in line_moving]))