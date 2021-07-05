num1 = input()

negative = num1.split(' ')

result = []

for i in negative:
    if int(i) < 0:
        result.append(0 - int(i))
    else:
        result.append(0 - int(i))

print(result)