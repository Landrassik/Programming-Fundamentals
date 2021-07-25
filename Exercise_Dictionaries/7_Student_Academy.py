n = int(input())
line_students = {}
for _ in range(1, n + 1):
    name_student = input()
    grade = float(input())
    if name_student not in line_students: line_students[name_student] = []
    line_students[name_student].append(grade)

line_students = {k: (sum(v) / len(v)) for k, v in line_students.items()}
result_students = {k: v for k, v in line_students.items() if v >= 4.50}

filters_dict = sorted(result_students.items(), key=lambda kvp: (-kvp[1]))
print("\n".join([f'{k} -> {v:.2f}' for k, v in filters_dict]))
