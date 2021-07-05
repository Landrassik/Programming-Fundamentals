def factorial_at_numbers(num):

    n = 1
    for i in range(num, 1, -1):
        n *= i
    return n


def factorial_division(a, b):
    return a / b

num1 = int(input())
num2 = int(input())
calc_factorial_num1 = factorial_at_numbers(num1)
calc_factorial_num2 = factorial_at_numbers(num2)

result = factorial_division(calc_factorial_num1, calc_factorial_num2)

print(f'{result:.2f}')