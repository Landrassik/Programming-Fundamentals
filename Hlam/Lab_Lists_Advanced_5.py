# count_man = [i for i in input().split()]
# happy_count = int(input())
#
# total_happy = [int(count_man[count]) * happy_count for count in range(len(count_man))]
# than_the_average = [i for i in total_happy if i > sum(total_happy) / len(total_happy)]
#
#
# if len(total_happy) - len(than_the_average) > len(than_the_average):
#     print(f'Score: {len(than_the_average)}/{len(total_happy)}. Employees are not happy!')
# else:
#     print(f'Score: {len(than_the_average)}/{len(total_happy)}. Employees are happy!')
#spisok = ['1', '2', '3']

#result = list(filter(lambda x: int(x) % 2 == 0, map(int, spisok)))
#print(result)

string_at_nums = list(filter(lambda x: int(x) % 2 == 0, map(int, input().split(', '))))
print(string_at_nums)