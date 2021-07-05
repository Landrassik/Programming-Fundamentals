import re
monsters = [name for name in input().split(", ")]

pattern = r"(?P<Name>[A-Za-z]+)((?P<Damage>([-+])?[1-8]?[0-9]\.?[0-9]?)|)"

total = {}

for i in monsters:
    match = [j.groupdict() for j in re.finditer(pattern, i)]
    symbol = (''.join([k for k in re.findall("[*/]+", i)]))
    sum_ord = ""
    damage = 0.00
    for num in match:

        for k, v in num.items():
            if k == "Damage" and not v == None:
                damage += float(v)
            elif k == "Name":
                sum_ord += v

    health = [ord(o) for o in sum_ord]
    health = sum(health)
    for l in symbol:
        if l == "*":
            damage *= 2
        else:
            damage /= 2

    if i not in total:
        total[i] = {"health": health, "sum_damage": 0.00}
        total[i]["sum_damage"] += damage


filter_dict = dict(sorted(total.items(), key=lambda x: x[0]))

for k, v in filter_dict.items():

    print(f"{k} - {v['health']} health, {v['sum_damage']:.2f} damage ")