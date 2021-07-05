line_nums = [int(i) for i in input().split(", ")]
minimum_many = int(input())
start = 0
for i in line_nums:
    if i < minimum_many:
        take_it = minimum_many - i
        if max(line_nums) - take_it >= minimum_many:
            max_many = line_nums.index(max(line_nums))
            line_nums[max_many] -= take_it
            line_nums[start] += take_it
        else:
            print("No equal distribution possible")
            exit()
    start += 1
print(line_nums)