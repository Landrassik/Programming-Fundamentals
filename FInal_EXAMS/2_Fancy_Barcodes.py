import re

n = int(input())
pattern = r"@[\#]+[A-Z][a-zA-Z0-9]{4,}[A-Z]+@[#]+"

while n > 0:
    barcodes = input()
    n -= 1
    match = re.match(pattern, barcodes)
    if match:
        for i in re.finditer(pattern, barcodes):
            i = i.group()
            num = [n for n in re.findall('[\\d]', i)]

            if len(num) == 0:
                print(f"Product group: 00")
            else:
                print(f'Product group: {"".join(num)}')
    else:
        print("Invalid barcode")
exit()