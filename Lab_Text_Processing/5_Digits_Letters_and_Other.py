word = input()

int_list = ""
str_list = ""
simvol_list = ""


for i in word:
    if i.isdigit():
        int_list += i
    elif i.isalpha():
        str_list += i
    else:
        simvol_list += i
print(int_list)
print(str_list)
print(simvol_list)