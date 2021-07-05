import re

emojis = []
text = input()
cool_threshold = 1
count = 0
pattern = r'(:{2}|\*{2})[A-Z][a-z][a-z]+\1'
for num in [int(x) for x in re.findall(r'\d', text)]:
    cool_threshold *= num
for emoji in re.finditer(pattern, text):
    count += 1
    emoji = emoji.group()
    threshold = sum([ord(char) for char in re.findall('[^\:\*]', emoji)])
    if threshold > cool_threshold:
        emojis.append(emoji)

print(f"Cool threshold: {cool_threshold}")
print(f"{count} emojis found in the text. The cool ones are:")
for emoji in emojis:
    print(emoji)