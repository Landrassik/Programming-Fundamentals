import re

patern = r"(?<=\s_)[a-zA-Z0-9]+\b"
text = input()

print(",".join([i.group() for i in re.finditer(patern, text)]))
