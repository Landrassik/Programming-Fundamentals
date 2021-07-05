line1 = int(input())
line2 = int(input())
total =""
for i in range(line1, line2 + 1):
    total += chr(i)
    total += " "

print(total)