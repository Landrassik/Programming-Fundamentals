string_numbers = [num_str for num_str in input().split('.')]
int_string = int("".join(string_numbers)) + 1

result = [i for i in str(int_string)]


print('.'.join(result))