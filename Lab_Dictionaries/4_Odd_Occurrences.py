line_word = [j.lower() for j in input().split()]
line_dict = {i: 0 for i in line_word if line_word.count(i) % 2 != 0}
print(" ".join([i for i in line_dict.keys()]))