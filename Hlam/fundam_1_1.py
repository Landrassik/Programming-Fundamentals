command = input()

count_coffe = 0

while not command == 'END':

    if command.upper() == command:
        if command.upper() == 'CAT'  'DOG':
            count_coffe += 2
        else:
            count_coffe += 1

    elif command.lower() == command:
        count_coffe += 1

    if count_coffe == 5:
        print(f"You need extra sleep")
        exit()
    command = input()
print(count_coffe)