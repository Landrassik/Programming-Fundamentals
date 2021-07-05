n = int(input())

list = []
result = []

for i in range(1, n + 1):
    num = input()
    list.append(int(num))
comand = input()
for j in list:
    if comand == 'even':
        if j % 2 == 0:
            result.append(j)

    elif comand == 'odd':
        if j % 2 != 0:
            result.append(j)

    elif comand == 'negative':
        if j < 0:
            result.append(j)

    elif comand == 'positive':
        if j >= 0:
            result.append(j)
print(result)