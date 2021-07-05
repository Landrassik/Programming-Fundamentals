line_hearts = list(map(int, input().split('@')))
command = input()
jump_in_num_house = 0

while command != 'Love!':
    jump = command.split(" ")
    jump_in_num_house += int(jump[1])
    if jump_in_num_house >= len(line_hearts):
        jump_in_num_house = 0
    if line_hearts[jump_in_num_house] == 0:
        print(f"Place {jump_in_num_house} already had Valentine's day.")
    else:
        line_hearts[jump_in_num_house] -= 2
        if line_hearts[jump_in_num_house] == 0:
            print(f"Place {jump_in_num_house} has Valentine's day.")
    command = input()

print(f"Cupid's last position was {jump_in_num_house}.")

if sum(line_hearts) == 0:
    print("Mission was successful.")
else:
    failed = [f for f in line_hearts if f != 0]
    print(f"Cupid has failed {len(failed)} places.")