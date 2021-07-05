party_size = int(input())
days = int(input())

coins = 0
companions = party_size
for i in range(1, days + 1):
    if i % 10 == 0:
        companions -= 2
    if i % 15 == 0:
        companions += 5
    coins += 50
    coins -= companions * 2
    if i % 3 == 0:
        coins -= companions * 3
    if i % 5 == 0:
        coins += companions * 20
        if i % 3 == 0:
            coins -= companions * 2
print(f"{companions} companions received {int(coins/companions)} coins each.")