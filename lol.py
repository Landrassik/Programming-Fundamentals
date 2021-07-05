def x(materials):
    for k, v in materials.items():
        for key, value in instrument.items():
            if k in value:
                if instrument[key][k] + v > 250:
                    instrument[key][k] = v - 250
                    return f"{key} obtained!", materials

                elif instrument[key][k] + v == 250:
                    instrument[key][k] = 0
                    return f"{key} obtained!", materials
                else:
                    instrument[key][k] = instrument[key][k] + v
            else:
                pass

    return False

hlam = []
instrument = {'Shadowmourne': {'Shards': 0}, 'Valanyr': {'Fragments': 0}, 'Dragonwrath': {'Motes': 0}}
component = ['Shards', 'Fragments', 'Motes']
result = False

while result == False:
    metal = input().split()
    y = {metal[i + 1].capitalize(): int(metal[i]) for i in range(0, len(metal), 2) if metal[i + 1].capitalize() == "Shards" or metal[i + 1].capitalize() == 'Fragments' or metal[i + 1].capitalize() == 'Motes'}
    hlam.append({metal[i + 1].capitalize(): int(metal[i]) for i in range(0, len(metal), 2) if not metal[i + 1].capitalize() in component})

    result = x(y)
print(result[0])
filter_dict = dict(sorted(instrument.items(), key=lambda kvp: (kvp[0][1])))
print("\n".join({f'{k}: {v}' for key, value in filter_dict.items() for k, v in value.items()}))
filter_hlam = dict(sorted({k: v for i in hlam for k, v in i.items()}.items(), key=lambda kvp: (kvp[1])))
print("\n".join({f'{k}: {v}' for k, v in filter_hlam.items()}))