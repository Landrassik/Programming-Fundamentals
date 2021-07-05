n = int(input())

water_tank = 255
total_liter = 0

for i in range(n):
    liters_of_water = int(input())
    if water_tank >= liters_of_water:
        water_tank -= liters_of_water
        total_liter += liters_of_water
    else:
        print("Insufficient capacity!")
print(total_liter)