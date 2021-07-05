line = int(input())
word = input()

spisoc = []


for i in range(line):
    spisoc += [input()]
print(spisoc)


for j in range(len(spisoc)):
    element = spisoc[j]

    if word not in element:
        spisoc.remove(element)

print(spisoc)