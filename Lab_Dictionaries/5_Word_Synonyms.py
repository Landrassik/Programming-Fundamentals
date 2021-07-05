n_word = int(input())

sinonim = {}

for i in range(n_word):
    key_word = input()
    value_word = input()

    if key_word not in sinonim:
        sinonim[key_word] = value_word

    else:
        sinonim[key_word] += ", "
        sinonim[key_word] += value_word

for (k, v) in sinonim.items():
    print(f"{k} - {v}")