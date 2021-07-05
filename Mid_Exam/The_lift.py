count_man = int(input())
wagon = list(map(int, input().split()))


for i in range(len(wagon)):
    if wagon[i] < 4:
        free_space = 4 - wagon[i]
        if count_man >= free_space:
            wagon[i] = 4
            count_man -= free_space
        else:
            wagon[i] = wagon[i] + count_man
            count_man = 0
is_empty = False
for wag in wagon:
    if wag < 4:
        is_empty = True
        break
if is_empty:
    print("The lift has empty spots!")
    result = [str(i) for i in wagon]
    print(" ".join(result))
elif count_man > 0:
    print(f"There isn't enough space! {count_man} people in a queue!")
    result = [str(i) for i in wagon]
    print(" ".join(result))
else:
    result = [str(i) for i in wagon]
    print(" ".join(result))

# queue = int(input())
# state = [int(i) for i in input().split(" ")]
# for i in range(len(state)):
#     while state[i] < 4 and queue > 0:
#         state[i] += 1
#         queue -= 1
# new_state = [i for i in state if i != 4]
# if queue == 0:
#     if len(new_state) > 0:
#         print("The lift has empty spots!")
#         print(f"{' '.join(str(x) for x in state)}")
#     else:
#         print(f"{' '.join(str(x) for x in state)}")
# else:
#     print(f"There isn't enough space! {queue} people in a queue!")
#     print(f"{' '.join(str(x) for x in state)}")