line_nums = input().split(', ')
boundary = 0
list_delete = []

while len(line_nums) > 0:
    for i in range(len(line_nums)-1, -1, -1):
        if boundary < int(line_nums[i]) <= boundary + 10:
            list_delete.append(int(line_nums[i]))
            line_nums.remove(line_nums[i])
    print(f"Group of {boundary + 10}'s: {list(reversed(list_delete))}")
    boundary += 10
    list_delete = []
