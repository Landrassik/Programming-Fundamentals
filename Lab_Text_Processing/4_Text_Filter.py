word = input().split(", ")
text = input()

for i in word:
    while i in text:
        text = text.replace(i, "*" * len(i))

print(text)