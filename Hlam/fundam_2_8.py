word1 = input()
word2 = input()

result = ""
totall = word1
for i in range(len(word1)):
    result = ""
    for j in range(0, i + 1):
        result += word2[j]
    for l in range(i + 1, len(word1)):
        result += word1[l]
    if totall == result:
        continue
    else:
        print(result)
    totall = result
