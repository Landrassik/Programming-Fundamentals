nums_in_line = [i for i in input().split(', ')]
result = list(map(lambda x: int(x) % 2, nums_in_line))

print(result)