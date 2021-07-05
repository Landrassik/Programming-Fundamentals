def word(iteration_word):
    if len(iteration_word) >= 3:
        num_word = "".join([i for i in iteration_word if i.isdigit()])
        iteration_word = "".join([i for i in iteration_word if not i.isdigit()])
        y = chr(int(num_word))
        y += iteration_word
        y = list(y)
        y[1], y[-1] = y[-1], y[1]
    return "".join(y)


line_password = input().split()
for i in line_password:
    print(word(i), end=" ")