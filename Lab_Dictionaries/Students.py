line_dict = {}
students = input()
while ":" in students:
    name, id, course = students.split(":")
    if course not in line_dict: line_dict[course] = []
    line_dict[course].append({id: name})
    students = input()

for k, v in line_dict.items():
    if k == ' '.join(students.split("_")):
        print('\n'.join([f"{value} - {key}" for i in v for key, value in i.items()]))