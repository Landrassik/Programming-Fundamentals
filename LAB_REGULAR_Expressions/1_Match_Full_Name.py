import re

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
text = input()

valid_name = re.findall(pattern, text)


print(" ".join(valid_name))

