line_numbers = list(map(str, input().split()))
line_string = list(input())
result = ''
character_number = 0

for search in line_numbers:
    search_number = search
    number = [int(x) for x in search_number]
    sum_number = sum(number)
    index = 0
    for i in range(sum_number):
        if i == len(line_string):
            sum_number = sum_number - len(line_string)
    result += line_string.pop(sum_number)
print(result)

#Lists Advanced - More Exercises
#Submit a solution