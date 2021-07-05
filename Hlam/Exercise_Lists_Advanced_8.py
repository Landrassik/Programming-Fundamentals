def chek(jump_length):
    if line_house[jump_length] > 2:
        line_house[jump_length] -= 2
    elif line_house[jump_length] == 2:
        line_house[jump_length] = 0
        print(f"Place {jump_length} has Valentine's day.")
    else:
        print(f"Place {jump_length} already had Valentine's day.")


line_house = list(map(int, input().split("@")))
command = input()
start_jump = 0
while not command == "Love!":
    command = command.split()
    jump_length = command[1]
    jump_length = int(jump_length)
    if jump_length + start_jump in range(len(line_house)):
        jump_length += start_jump
        result = chek(jump_length)
        start_jump = jump_length
    else:
        result = chek(0)
        start_jump = 0
    command = input()
if len(line_house) > 0:
    print(f"Cupid's last position was {start_jump}.")
if sum(line_house) == 0:
    print("Mission was successful.")
else:
    failed = [f for f in line_house if f != 0]
    print(f"Cupid has failed {len(failed)} places.")