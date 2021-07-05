quantity_room = int(input())
quantity = True
count = 0
for room in range(1, quantity_room + 1):
    chairs, n_people = input().split()
    n_people = int(n_people)
    if len(chairs) > n_people:
        count += len(chairs) - n_people
    elif len(chairs) < n_people:
        count = n_people - len(chairs)
        quantity = False
        print(f'{count} more chairs needed in room {room}')
if quantity:
    print(f'Game On, {count} free chairs left')
