def loading_loop(num):
    loading = '['
    num = num / 10
    for i in range(1, 10 + 2):
        if i == 11:
            loading += ']'
        elif i <= num:
            loading += '%'
        else:
            loading += '.'
    return loading


number = int(input())
result = loading_loop(number)
if number < 100:
    print(f'{number}% {result}')
    print('Still loading...')
else:
    print(f'{number}% Complete!')
    print(result)