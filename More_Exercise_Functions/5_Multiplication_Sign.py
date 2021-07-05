def check(a, b, c):
    if a < 0 or b < 0 or c < 0:
        print("negative")
    elif a == 0 or b == 0 or c == 0:
        print("zero")
    else:
        print("positive")


a = int(input())
b = int(input())
c = int(input())

result = check(a, b, c)