def feb(n, x):
    for i in range(2, n):
        if 0 < len(x) < 3:
            x.append(x[-1] + x[-2])
        else:
            x.append(x[-1] + x[-2] + x[-3])
    return x


n = int(input())
x = [1, 1]
result = feb(n, x)

print(' '.join(str(y) for y in result))