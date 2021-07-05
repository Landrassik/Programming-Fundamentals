def int_f(x):
    result = x * 2
    return result


def real_f(x):
    result = x * 1.5
    return result


def string_f(x):
    result = f"${x}$"
    return result


command = input()
n = input()

if command == "int":
    data = int_f(int(n))
elif command == 'real':
    data = real_f(int(n))
    data = f"{data:.2f}"
elif command == 'string':
    data = string_f(n)

print(data)