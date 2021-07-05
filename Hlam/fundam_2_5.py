years = int(input())

years += 1
string_years = ""

while True:
    string_years = str(years)
    if len(string_years) == len(set(string_years)):
        print(string_years)
        break
    else:
        years += 1
