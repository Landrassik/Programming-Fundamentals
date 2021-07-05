import re

pattern = r">>(?P<name>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)(?!=$)"
command = input()
total_name = []
total_sum = 0

while not command == "Purchase":
    match = re.match(pattern, command)
    if match:
        data = match.groupdict()
        total_name.append(data["name"])
        total_sum += float(data["price"]) * int(data["quantity"])
    command = input()

print(f"Bought furniture:")
if total_name:
    print("\n".join(total_name))
print(f"Total money spend: {total_sum:.2f}")
# >>Sofa<<312.23!3
# >>TV<<300!5
# >>Invalid<!5
# Purchase