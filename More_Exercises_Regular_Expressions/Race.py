import re

line = {name: 0 for name in input().split(", ")}
command = input()
pattern = r"(?P<Name>[A-Za-z])"
count = 0
while not command == 'end of race':
    match = "".join([i.group() for i in re.finditer(pattern, command)])

    if match in line:
        sum_km = [int(km.group()) for km in re.finditer('\\d', command)]
        sum_km = sum(sum_km)
        line[match] += sum_km

    command = input()

filter_line = dict(sorted(line.items(), key=lambda x: (-x[1])))
for k in filter_line.keys():
    count += 1
    if count == 1:
        print(f"{count}st place: {k}")
    elif count == 2:
        print(f"{count}nd place: {k}")
    elif count == 3:
        print(f"{count}rd place: {k}")
    else:
        exit()