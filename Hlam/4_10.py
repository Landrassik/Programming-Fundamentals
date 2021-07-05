loos_fights = int(input())

helmet_price = float(input()) #шлем
sword_price = float(input()) #меч
shield_price = float(input()) #щит
armor_price = float(input()) #бронь

shield_count = 0

total_suma = 0

for i in range(2, loos_fights + 1):
    if i % 2 == 0:
        total_suma += helmet_price

    if i % 3 == 0:
        total_suma += sword_price

        if i % 2 == 0:
            total_suma += shield_price
            shield_count += 1
            if shield_count % 2 == 0:
                total_suma += armor_price
else:
    print(f"Gladiator expenses: {total_suma:.2f} aureus")