word = input()

while not word == "end":
    new_word = word[::-1]
    print(f"{word} = {new_word}")
    word = input()
exit()