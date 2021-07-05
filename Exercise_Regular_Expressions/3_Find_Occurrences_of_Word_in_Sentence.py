import re


text = input()
search = input()

pattern = f"{search}\\b"


count = re.findall(pattern, text, re.IGNORECASE)

print(len(count))