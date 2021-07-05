import re

text = input()
pattern = r"www\.[a-zA-Z0-9-]+\.[a-zA-Z]+(\$|[\.a-z-]+)"
x = []
while text:

    match = re.finditer(pattern, text)
    result = [i.group() for i in match]
    if result:
        x.extend(result)
    text = input()

print(*[j for j in x], sep="\n")