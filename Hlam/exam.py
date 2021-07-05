days_of_adventure = int(input())
count_of_players = int(input())
grope_energy = float(input())
 # буду в цикле получать продцкты на сутки на одгошл чедовека
water_per_day_for_one_person = float(input())
food_per_day_for_one_person = float(input())


total_water = days_of_adventure * count_of_players * water_per_day_for_one_person
total_food = days_of_adventure * count_of_players * food_per_day_for_one_person
# для каждого дня расчитываем потерю энергии
for i in range(1, days_of_adventure + 1):
    if grope_energy >= 0:
        energy_lost = float(input()) # энергия которую теряют каждый день
        grope_energy -= energy_lost
    else:
        break

    if i % 2 == 0:
        grope_energy += grope_energy * 0.05
        total_water -= total_water * 0.30

    if i % 3 == 0:
        grope_energy += grope_energy * 0.10
        total_food -= total_food / count_of_players

if grope_energy != 0:
    print(f'You are ready for the quest. You will be left with - {grope_energy:.2f} energy!')
else:
    print(f'You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.')