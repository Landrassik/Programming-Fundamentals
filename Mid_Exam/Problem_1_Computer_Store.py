comand = input()

money = 0

while comand != "special" and comand != "regular":
    price = float(comand)
    if price > 0:
        money += price
    elif price == 0:
        print('Invalid order!')
    else:
        print('Invalid price!')

    comand = input()

if money != 0:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {money:.2f}$")

    nalog = money * 20 / 100
    money += nalog
    if comand == "special":

        money -= money * 10 / 100


    print(f"Taxes: {nalog:.2f}$")
    print("-----------")
    print(f"Total price: {money:.2f}$")
else:
    print('Invalid order!')