legendary_items = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
chek = False
while not chek:
    data = input().split()
    for i in range(0, len(data), 2):
        item = data[i+1].lower()
        count = int(data[i])
        if item in legendary_items:
            legendary_items[item] += count
            if legendary_items[item] >= 250:
                legendary_items[item] = legendary_items[item] - 250
                if item == 'shards': print(f'Shadowmourne obtained!')
                elif item == 'fragments': print(f'Valanyr obtained!')
                elif item == 'motes': print(f'Dragonwrath obtained!')
                chek = True
                break

        elif item not in junk: junk[item] = count
        elif item in junk: junk[item] += count

filter_items = sorted(legendary_items.items(), key=lambda kvp: (-kvp[1], kvp[0]))
filter_junk = sorted(junk.items(), key=lambda x: x[0])
print("\n".join([f'{k}: {v}' for k, v in filter_items]))
print("\n".join([f'{k}: {v}' for k, v in filter_junk]))