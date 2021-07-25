command = input()
line_dict = {}
result_dict_count_language = {}
baned_line_dict = {}
while not command == "exam finished":
    command = command.split('-')
    if not command[-1] == "banned":
        username, language, points = command[:]
        points = int(points)
        if username not in line_dict:
            line_dict[username] = {'language': language, 'points': points}

        elif username in line_dict:
            if language in line_dict[username]['language'] and points > line_dict[username]['points']:
                line_dict[username] = {'language': language, 'points': points}
        if language not in baned_line_dict:
            baned_line_dict[language] = 0
        baned_line_dict[language] += 1
    else:
        del line_dict[username]

    command = input()
print('Results:')
filter_dict = sorted(line_dict.items(), key=lambda kvp: (-kvp[1]['points'], kvp[0]))
print('\n'.join([f"{key} | {v}" for key, value in filter_dict for k, v in value.items() if k == 'points']))

print('Submissions:')
filter_language = sorted(baned_line_dict.items(), key=lambda kvp: (-kvp[1], kvp[0]))
print("\n".join([f'{k} - {v}' for k, v in filter_language]))