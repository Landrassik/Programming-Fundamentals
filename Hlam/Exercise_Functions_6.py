def valid_pasword(x):
    result = []
    count_string = 0
    count_numbers = 0
    error_character = 0
    total_character = 0

    for i in x:
        if i.isdigit() == True:
            count_numbers += 1
            total_character += 1
        elif i.isdigit() == False:
            count_string += 1
            total_character += 1
        if not 65 <= ord(i) <= 90:
            if not 97 <= ord(i) <= 122:
                if not 48 <= ord(i) <= 57:
                    error_character += 1

    if not 6 <= total_character <= 10:
        result.append('Password must be between 6 and 10 characters')
    if not error_character == 0:
        result.append('Password must consist only of letters and digits')
    if not count_numbers >= 2:
        result.append('Password must have at least 2 digits')
    if len(result) == 0:
        result.append('Password is valid')
    return result


pasword = input()
result_valid_pasword = valid_pasword(pasword)

for i in result_valid_pasword:
    print(i)