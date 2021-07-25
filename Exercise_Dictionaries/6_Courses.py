command = input()
line_dict = {}
while not command == "end":
    command = ''.join(command.split(":"))
    command = command.split()
    name_course, name_student = " ".join(command[:-2]), " ".join(command[:-3:-1][::-1])
    if name_course not in line_dict: line_dict[name_course] = []
    if name_student not in line_dict[name_course]: line_dict[name_course].append(name_student)
    line_dict[name_course].sort()
    command = input()

filter_dict = sorted(line_dict.items(), key=lambda kvp: (-len(kvp[1])))
for k, v in filter_dict:
    print(f"{k}: {len(v)}")
    for i in v:
        print(f"-- {i}")
