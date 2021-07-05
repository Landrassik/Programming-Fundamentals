quantity = int(input())

quantity_train = [0 for i in range(quantity)]

comand = input()

while comand != 'End':
    data = comand.split()
    if data[0] == 'add':
        number_of_people = int(data[1])
        quantity_train[-1] += number_of_people
    elif data[0] == 'insert':
        index_at_vagon = int(data[1])
        quantity_of_people = int(data[2])
        quantity_train[index_at_vagon] += quantity_of_people
    elif data[0] == 'leave':
        index_at_vagon = int(data[1])
        quantity_of_people = int(data[2])
        quantity_train[index_at_vagon] -= quantity_of_people
    comand = input()
print(quantity_train)
