n = int(input())

x = ""
y = False

for i in range(n):
    simbol = (input())
    for j in simbol:
        if j == '(':
            x += j
        elif j == ')':
            x += j

    if x == '()':
        x = ""
        y = True

    elif x != "":
        y = False
if y:
    print("BALANCED")
else:
    print("UNBALANCED")
