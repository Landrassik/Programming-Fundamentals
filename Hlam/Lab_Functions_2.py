def Calculations_numbers(comand, a, b):
    if comand == 'multiply':
        return a * b
    elif comand == 'divide':
        return a / b
    elif comand == 'add':
        return a + b
    elif comand == 'subtract':
        return a - b

comand = input()
first = int(input())
second = int(input())

result = Calculations_numbers(comand, first, second)
print(f"{int(result)}")