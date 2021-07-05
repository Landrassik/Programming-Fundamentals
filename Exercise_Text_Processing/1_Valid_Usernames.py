line = input().split(", ")

for i in line:
    i_true = True
    if 3 <= len(i) <= 16:
        for j in i:
            if not j.isalnum() == True or j.isspace() == True:
                if j == "-" or j == "_":
                    continue
                else:
                    i_true = False
                    break
    else:
        i_true = False
    if i_true:
        print("".join(i))