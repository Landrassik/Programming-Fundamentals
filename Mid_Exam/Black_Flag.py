count_dey = int(input())
gold_in_day = int(input())
result = int(input())

result_gold = 0

for i in range(1, count_dey + 1):
    result_gold += gold_in_day
    if i % 3 == 0:
        result_gold += gold_in_day * 50 / 100
    if i % 5 == 0:
        result_gold -= result_gold * 30 / 100

if result_gold >= result:
    print(f"Ahoy! {result_gold:.2f} plunder gained.")
else:
    print(f"Collected only {result_gold / result * 100:.2f}% of the plunder.")