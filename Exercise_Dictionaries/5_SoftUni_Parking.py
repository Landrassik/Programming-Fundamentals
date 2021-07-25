n = int(input())
line_name_dict = {}
for i in range(n):
    command = input().split()
    if command[0] == 'register':
        name, num_cars = command[1], command[2]
        if name not in line_name_dict:
            line_name_dict[name] = num_cars
            print(f'{name} registered {num_cars} successfully')
        elif name in line_name_dict: print(f"ERROR: already registered with plate number {line_name_dict[name]}")

    elif command[0] == 'unregister':
        name = command[1]
        if name not in line_name_dict: print(f"ERROR: user {name} not found")
        else:
            del line_name_dict[name]
            print(f"{name} unregistered successfully")
print('\n'.join([f"{k} => {v}" for k, v in line_name_dict.items()]))