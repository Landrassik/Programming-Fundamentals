num = input().split()
string = list(input())

total = ""

for i in num:
    sum_num = 0
    for j in i:
        sum_num += int(j)

    start = 0
    check_len = 0

    while check_len <= sum_num:

        result = string[start]
        if start >= len(string) - 1:
            start = 0
            check_len += 1
            continue
        start += 1
        check_len += 1

    total += result
    string.remove(result)
print(total)