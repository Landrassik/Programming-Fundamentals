count_stud = int(input())
count_lection = int(input())
initial_bonus = int(input())

fact_stud = []
if count_lection != 0:
    for i in range(count_stud):
        fact_stud.append(int(input()))

    result = round(max(fact_stud) / count_lection * (5 + initial_bonus))
    print(f"Max Bonus: {result}.")
    print(f"The student has attended {max(fact_stud)} lectures.")
else:
    print(f"Max Bonus: 0.")
    print(f"The student has attended 0 lectures.")