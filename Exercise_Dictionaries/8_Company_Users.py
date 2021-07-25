command = input().split()
line_dict = {}
while not command[0] == "End":
    name_company, id_name = command[0], command[-1]
    if name_company not in line_dict: line_dict[name_company] = []
    if id_name not in line_dict[name_company]: line_dict[name_company].append(id_name)
    command = input().split()
filter_line_dict = sorted(line_dict.items(), key=lambda kvp: kvp[0])

for k, v in filter_line_dict:
    print(k)
    for i in v:
        print(f"-- {i}")