import re

pattern = r"(^| (?<=\s))-?\d+(\.\d+)?($|(?=\s))"
text = input()

valid_num = [obj.group(0) for obj in re.finditer(pattern, text)]
print("".join(valid_num))