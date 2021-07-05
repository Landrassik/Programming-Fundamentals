import re

pattern = r"(?P<Day>\d{2})(?P<x>[/\.\-])(?P<Month>[A-Z][a-z]{2})(?P=x)(?P<Year>\d{4})\b"
data = input()

valid_data = [i.groupdict() for i in re.finditer(pattern, data)]

print("".join([f"Day: {i['Day']}, Month: {i['Month']}, Year: {i['Year']}\n"for i in valid_data]))