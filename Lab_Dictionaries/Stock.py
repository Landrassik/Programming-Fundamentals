line = input().split()
x = {line[i]: line[i + 1] for i in range(0, len(line), 2)}
print("\n".join([f"Sorry, we don't have {i}" if i not in x else f'We have {x[i]} of {i} left' for i in input().split()]))
