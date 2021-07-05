line = input().split()
comand = input()


while comand != "No Money":
    comand_for = comand.split()
    index_gift = comand_for[1]
    if comand_for[0] == 'OutOfStock':
        for gifts in range(len(line)):
            if line[gifts] == index_gift:
                line[gifts] = "None"

    elif comand_for[0] == 'Required':
        gifts = int(comand_for[2])
        if 0 <= gifts < len(line):
            line[gifts] = index_gift

    elif comand_for[0] == 'JustInCase':
        line[-1] = index_gift
    comand = input()
for i in line:
    if i != 'None':
        print(i, end=" ")