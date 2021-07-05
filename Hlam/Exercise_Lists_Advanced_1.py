line_substrings = input().split(", ")
filter_substrings = input().split(", ")
result = [substrings for substrings in line_substrings for fil in filter_substrings if substrings in fil]


print(sorted(set(result), key=line_substrings.index))