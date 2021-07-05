def string_single_number(num):
    odd = 0
    even = 0
    for string_number in num:
        if int(string_number) % 2 == 0:
            even += int(string_number)
        else:
            odd += int(string_number)

    return [odd, even]




string_single = input()
result = string_single_number(string_single)
even_sum = result[1]
odd_sum = result[0]

print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')