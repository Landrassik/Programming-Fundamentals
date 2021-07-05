import re
count_num = []

patern = r"\d+"
text = input()

while not text == "":
    valid_num = re.findall(patern, text)
    count_num.extend(valid_num[:])
    text = input()

print(*count_num)
