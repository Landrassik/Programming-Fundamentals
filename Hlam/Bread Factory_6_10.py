line = input().split('|')
coins = 0
coins2 = 0
energy = 100
en = True
total_coins = 100
money = True

for event in line:
    x = event.split("-")
    name = x[0]
    count_num = int(x[1])

    if name == 'rest':
        if energy + count_num <= 100:
            it = 0
            energy += count_num
            print(f'You gained {count_num} energy.')
            print(f'Current energy: {energy}.')
        else:
            print(f'You gained {it} energy.')
            print(f'Current energy: {energy}.')

    elif name == 'order':
        if energy > 30:
            coins += count_num
            coins2 += count_num
            total_coins += count_num
            energy -= 30
            print(f'You earned {coins} coins.')
            coins = 0
        elif energy < 30:
            print('You had to rest!')
            energy += 50
            continue

    else:
        if total_coins - count_num > 0:
            total_coins -= count_num
            print(f'You bought {name}.')
        else:
            print(f'Closed! Cannot afford {name}.')
            money = False
            break
if money:
    print('Day completed!')
    print(f'Coins: {coins2}')
    print(f'Energy: {energy}')


