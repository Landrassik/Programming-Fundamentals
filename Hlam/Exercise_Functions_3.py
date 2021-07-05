def calculates_characters_in_askii(a, b):
    x = ''
    for characters in range(ord(a) + 1, ord(b)):
        x += chr(characters)
        x += ' '
    return x


characters_1 = input()
characters_2 = input()

result = calculates_characters_in_askii(characters_1, characters_2)

print(result)
