n = int(input())

cars_dict = {}

for i in range(n):
    model = input().split("|")
    car, mileage, fuel = model[:]
    mileage, fuel = int(mileage), int(fuel)
    cars_dict[car] = {'mileage': mileage, 'fuel': fuel}

command = input()

while not command == "Stop":
    command = command.split(" : ")

    if command[0] == "Drive":
        car, distance, fuel_of_distance = command[1:]
        distance, fuel_of_distance = int(distance), int(fuel_of_distance)
        if cars_dict[car]['fuel'] >= fuel_of_distance:
            cars_dict[car]['fuel'] -= fuel_of_distance
            cars_dict[car]['mileage'] += distance
            print(f"{car} driven for {distance} kilometers. {fuel_of_distance} liters of fuel consumed.")
        else:
            print(f"Not enough fuel to make that ride")

    elif command[0] == "Refuel":
        car, fuel_of_car = command[1:]
        fuel_of_car = int(fuel_of_car)
        if cars_dict[car]['fuel'] + fuel_of_car >= 75:

            print(f"{car} refueled with {75 - cars_dict[car]['fuel']} liters")
            cars_dict[car]['fuel'] = 75
        else:
            cars_dict[car]['fuel'] += fuel_of_car
            print(f"{car} refueled with {fuel_of_car} liters")

    elif command[0] == "Revert":
        car, kilometers = command[1:]
        kilometers = int(kilometers)
        if cars_dict[car]['mileage'] - kilometers >= 10000:
            cars_dict[car]['mileage'] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")
        else:
            cars_dict[car]['mileage'] = 10000
    if cars_dict[car]['mileage'] >= 100000:
        print(f"Time to sell the {car}!")
        del cars_dict[car]

    command = input()

filter_dict = sorted(cars_dict.items(), key=lambda x: (-x[1]['mileage'], x[0]))

for i, v in filter_dict:
    print(f"{i} -> Mileage: {v['mileage']} kms, Fuel in the tank: {v['fuel']} lt.")