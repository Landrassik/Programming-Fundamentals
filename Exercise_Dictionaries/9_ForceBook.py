command = input()
line_dict = {}

while not command == "Lumpawaroo":
    if '|' in command:
        command = "".join(command.split('|'))
        command = command.split()
        force_Side, force_User = ''.join(command[0:-1]), ''.join(command[-1])
        if force_Side not in line_dict:
            line_dict[force_Side] = []
        if force_User not in line_dict[force_Side]:
            line_dict[force_Side].append(force_User)

    elif '->' in command:
        command = "".join(command.split('->'))
        command = command.split()
        force_User, force_Side = ' '.join(command[0:-1]), ''.join(command[-1])
        for k, v in line_dict.items():
            if force_User in v:
                line_dict[k].remove(force_User)
        if force_Side not in line_dict:
            line_dict[force_Side] = []
        if force_User not in line_dict[force_Side]:
            line_dict[force_Side].append(force_User)

            print(f'{force_User} joins the Lighter side!')
    command = input()
filter_line_dict = sorted(line_dict.items(), key=lambda kvp: (-len(kvp[1])))

for k, v in filter_line_dict:
    if len(v) > 0:
        print(f"Side: {k}, Members: {len(v)}")
        print("\n".join([f'! {i}' for i in sorted(v)]))