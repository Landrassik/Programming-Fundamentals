import re
n = int(input())

pattern = r"(?<=\@)(?P<Name>[A-Za-z]+)[0-9]?:[1-9][0-9]{1,}!(?P<Command>[AD])!->[1-9][0-9]{1,}"
result_dict = {}
while 0 < n < 100:
    line = input()
    count_letters = [character.group() for character in re.finditer('[starSTAR]', line)]
    number_of_delete = len(count_letters)
    result_ord = [ord(i) - number_of_delete for i in line]
    result_chr = "".join([chr(i) for i in result_ord])

    match = [m.groupdict() for m in re.finditer(pattern, result_chr)]
    for i in match:
        if i['Name'] not in result_dict:
            result_dict[i['Name']] = i['Command']
    n -= 1
count_A = [num for num in result_dict.values() if num == "A"]
count_D = [num for num in result_dict.values() if num == "D"]

filter_result = sorted(result_dict.items(), key=lambda x: x[0], reverse=False)
print(f"Attacked planets: {len(count_A)}")
if len(count_A) > 0:
    print(*[f"-> {k}"for k, v in filter_result if v == 'A'], sep='\n')
print(f"Destroyed planets: {len(count_D)}")
if len(count_D) > 0:
    print(*[f"-> {k}"for k, v in filter_result if v == 'D'], sep='\n')