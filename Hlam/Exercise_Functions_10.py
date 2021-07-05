array_list = [int(i) for i in input().split(" ")]


def exchange(array, index):
    return array[index + 1:] + array[:index + 1]


def maximum_number(array, type):
    if type == "even":
        max_even = [int(i) for i in array if i % 2 == 0]
        if len(max_even) == 0:
            return "No matches"
        else:
            max_even = max(max_even)
            return len(array) - 1 - array[::-1].index(max_even)
    else:
        max_odd = [int(i) for i in array if i % 2 != 0]
        if len(max_odd) == 0:
            return "No matches"
        else:
            max_odd = max(max_odd)
            return len(array) - 1 - array[::-1].index(max_odd)


def minimum_number(array, type):
    if type == "even":
        min_even = [int(i) for i in array if i % 2 == 0]
        if len(min_even) == 0:
            return "No matches"
        else:
            min_even_element = min(min_even)
            return len(array) - 1 - array[::-1].index(min_even_element)
    else:
        min_odd = [int(i) for i in array if i % 2 != 0]
        if len(min_odd) == 0:
            return "No matches"
        else:
            min_odd_element = min(min_odd)
            return len(array) - 1 - array[::-1].index(min_odd_element)


def first_count(array, type, count):
    if count > len(array):
        return "Invalid count"
    else:
        counting_array = []
        if type == "even":
            for i in range(len(array)):
                if array[i] % 2 == 0 and count > 0:
                    counting_array.append(array[i])
                    count -= 1
        else:
            for i in range(len(array)):
                if array[i] % 2 != 0 and count > 0:
                    counting_array.append(array[i])
                    count -= 1
        return counting_array


def last_count(array, type, count):
    if count > len(array):
        return "Invalid count"
    else:
        if type == "even":
            even_elements = [int(i) for i in array if i % 2 == 0]
            if len(even_elements) == 0:
                return []
            elif len(even_elements) < count:
                return even_elements
            else:
                return even_elements[len(even_elements) - count:]
        else:
            odd_elements = [int(i) for i in array if i % 2 != 0]
            if len(odd_elements) == 0:
                return []
            elif len(odd_elements) < count:
                return odd_elements
            else:
                return odd_elements[len(odd_elements) - count:]


def execute(array, command):
    global array_list
    current_command = command.split(" ")

    if current_command[0] == "exchange":
        index = int(current_command[1])
        if index >= len(array) or index < 0:
            print("Invalid index")
        else:
            array_list = exchange(array, index)
    elif current_command[0] == "max" or current_command[0] == "min":
        if current_command[0] == "max":
            print(maximum_number(array, current_command[1]))
        else:
            print(minimum_number(array, current_command[1]))
    else:
        if current_command[0] == "first":
            number = int(current_command[1])
            print(first_count(array, current_command[2], number))
        else:
            number = int(current_command[1])
            print(last_count(array, current_command[2], number))


while True:
    command = input()
    if command == "end":
        print(array_list)
        break
    else:
        execute(array_list, command)