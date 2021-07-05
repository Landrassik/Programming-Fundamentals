import string
def asci_table(char):
    result = []
    x = 1
    for c in string.ascii_uppercase:

        if c == char:
            result.append(x)
            result.append(True)
            return result
        x += 1
    x = 1
    for c in string.ascii_lowercase:

        if c == char:
            result.append(x)
            result.append(False)
            return result
        x += 1


line = [i for i in input().split()]

count_num = []

for i in line:
    char_left = ""
    char_right = ""
    num = ""

    for character in range(len(i)):
        if character == 0:
            char_left = i[character]
        elif i[character].isdigit() == True:
            num += i[character]
        else:
            char_right += i[character]

    result_left = asci_table(char_left)
    result_right = asci_table(char_right)
    side = True
    if side:
        num = int(num)
        if result_left[1]:
            num = (num) / result_left[0]
        else:
            num = (num) * result_left[0]

        if result_right[1]:
            num = (num) - result_right[0]
        else:
            num = (num) + result_right[0]
        count_num.append(num)

print(f"{sum(count_num):.2f}")