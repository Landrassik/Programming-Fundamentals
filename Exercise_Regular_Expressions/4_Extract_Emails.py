import re

pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-z]+-?[a-z]+(\.[a-z]+)+"
text = input()


valid_mail = [i.group() for i in re.finditer(pattern, text)]

print(*valid_mail, sep="\n")


