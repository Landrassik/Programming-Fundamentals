from itertools import zip_longest
line_word = input().split()
result = []

a = [ord(i) for i in line_word[0]]
b = [ord(i) for i in line_word[1]]

result = [x * y for x, y in zip_longest(a, b, fillvalue=1)]

print(sum(result))