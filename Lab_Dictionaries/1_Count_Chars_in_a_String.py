word = input()

count_word = {}

for i in word:
    if i != " ":
        if i not in count_word:
            count_word[i] = 0
        count_word[i] += 1

for (k, v) in count_word.items():
    print(f"{k} -> {v}")