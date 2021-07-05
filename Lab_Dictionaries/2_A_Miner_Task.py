command = input()

line_dict = {}
count = 0
key = None
while not command == "stop":
    count += 1
    if not count % 2 == 0:
        key = command
        if key not in line_dict:
            line_dict[key] = 0
    else:
        value = int(command)
        line_dict[key] += value
        key = None

    command = input()

for (k, v) in line_dict.items():
    print(f"{k} -> {v}")