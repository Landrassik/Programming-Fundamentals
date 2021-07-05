import re

text = input()
pattern = r"(#|@)(?P<Word_1>[a-zA-Z]{3,})\1(#|@)(?P<Word_2>[a-zA-Z]{3,})\1"
chek = False
match_word = []
match = re.match(pattern, text)

valid_word = [i.groupdict() for i in re.finditer(pattern, text)]

if valid_word:
    print(f"{len(valid_word)} word pairs found!")
    for index in valid_word:
        word_1, word_2 = index.values()
        if word_1 == word_2[::-1]:
            match_word.append(f"{word_1} <=> {word_2}")
            chek = True

    if chek:
        print("The mirror words are:")
        print(f"{', '.join(match_word)}")

else:
    print("No word pairs found!")
if not chek:
    print("No mirror words!")




