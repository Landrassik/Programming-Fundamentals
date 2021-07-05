n = int(input())
kate = False
exit_kate = False
count = 1
command = list(input())
index_exit = []
for i in range(n):
    if "k" in command:
        Kate = command.index("k")
        kate = True
        index_exit = [j for j in range(len(command)) if command[j] == " " or command[j] == "k"]
    chek_command = [j for j in range(len(command)) if command[j] == " " or command[j] == "k"]
    if len(chek_command) != 0 and kate == True:
        for l in chek_command:
            if l in index_exit and kate == True:
                exit_kate = True
                index_exit = chek_command
                count += command.count(" ")
                break
            elif l not in index_exit and kate == True:
                exit_kate = False
                break
    elif len(chek_command) == 0 and kate == True:
        exit_kate = False
        break
    command = list(input())

if exit_kate:
    print(f"Kate got out in {count} moves")
else:
    print("Kate cannot get out")