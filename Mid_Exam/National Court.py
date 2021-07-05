worker1 = int(input())
worker2 = int(input())
worker3 = int(input())

mans = int(input())
hours = 0

while mans > 0:
    hours += 1
    if hours % 4 != 0:
        mans = mans - worker1 - worker2 - worker3

print(f"Time needed: {hours}h.")