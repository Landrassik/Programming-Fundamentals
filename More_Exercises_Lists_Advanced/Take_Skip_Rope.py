line = input()
total = []

non_numbers = [i for i in line if not i.isnumeric()]
numbers_list = [i for i in line if i.isdigit()]

take_list = [int(numbers_list[i]) for i in range(len(numbers_list)) if i % 2 == 0]
skip_list = [int(numbers_list[i]) for i in range(len(numbers_list)) if not i % 2 == 0]

for i in range(len(take_list)):
    total += non_numbers[:take_list[i]]
    del non_numbers[:take_list[i]]

    for j in range(len(skip_list)):
        if j == i:
            del non_numbers[:skip_list[j]]

print("".join(total))