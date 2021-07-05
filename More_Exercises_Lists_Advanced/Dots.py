def vertikal(rows):
    x = False
    count = 0
    start = 0
    total_point = 0
    for _ in rows[::]:
        point_in_rows = [j for i in rows[start: start + 2] for j in range(len(i)) if i[j] == "."]
        start += 1
        if len(point_in_rows) > len(set(point_in_rows)):
            x = True
            count += (len(point_in_rows) - len(set(point_in_rows)))
            total_point += count
            count = 0
        else:
            x = False
            if total_point < count:
                total_point = count
                count = 0

    return total_point


def horizon(rows_column):
    total_count = 0
    start = 0
    count = 0
    for i in rows_column[start: start + 2]:
        for y in range(len(i)):
            if y != len(i) - 1:
                if i[y] == "." and i[y + 1] == ".":
                    count += 1
                elif i[y] == "." and i[y - 1] == ".":
                    count += 1
        start += 1
        if total_count < count:
            total_count = count
            count = 0
    return total_count


rows = int(input())
count_rows = []

for row in range(rows):
    count_rows.append(input().split())

x = vertikal(count_rows)
a = horizon(count_rows)
print(x + a)