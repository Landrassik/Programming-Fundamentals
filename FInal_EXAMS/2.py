import re
n = int(input())
pattern = r"(^|(?<=\s))(\$|%)(?P<X>[A-Z][a-z]{2,})\2\: \[[0-9]+\]\|\[[0-9]+\]\|\[[0-9]+\]\|($|(?=\s))"
key = {}
for i in range(n):
    text = input()
    match = re.match(pattern, text)
    if match:
        for j in re.finditer(pattern, text):
            key = j.groupdict()
            j = j.group()
            result = [chr(int(character)) for character in re.findall('[\\d]+', j)]
            print(f"{key['X']}: {''.join(result)}")
    else:
        print(f"Valid message not found!")

