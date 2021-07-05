budget = float(input())
price_1kg_flour = float(input())
price_1litr_milk = price_1kg_flour * 1.25 / 4
price_1pack_eggs = price_1kg_flour * 75 / 100
counter_cozonacs = 0
counter_eggs_colors = 0

while True:
    budget -= price_1kg_flour + price_1litr_milk + price_1pack_eggs
    if budget >= 0:
        counter_cozonacs += 1
        counter_eggs_colors += 3
        if counter_cozonacs % 3 == 0:
            counter_eggs_colors -= counter_cozonacs - 2

    else:
        budget += price_1kg_flour + price_1litr_milk + price_1pack_eggs
        break


print(f"You made {counter_cozonacs} cozonacs! Now you have {counter_eggs_colors} eggs and {budget:.2f}BGN left.")
print()
