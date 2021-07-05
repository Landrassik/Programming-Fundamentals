word_in_line = [i for i in input().split() if i == i[::-1]]
palindrome = input()

result = word_in_line.count(palindrome)
print(word_in_line)
print(f'Found palindrome {result} times')