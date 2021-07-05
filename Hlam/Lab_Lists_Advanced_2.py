todo_notes = input()
total_list = [0] * 10


while not todo_notes == 'End':
    importance, task = todo_notes.split('-')
    importance = int(importance) - 1
    total_list[importance] = task

    todo_notes = input()
result = [i for i in total_list if not i == 0]

print(result)