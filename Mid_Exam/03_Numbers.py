line_number = [int(i) for i in input().split()]
avarge = sum(line_number) / len(line_number)
avarge = round(avarge, 2)

if len(line_number) > 1:
    result = [j for j in line_number if j > avarge]
    result = sorted(result)
    result.reverse()
    result_5 = [result[h] for h in range(len(result)) if h < 5]

    print(" ".join(list(map(str, result_5))))
else:
    print("No")