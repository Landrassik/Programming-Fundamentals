red_card = input()
card = ''
card_list = []
comand_A = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
comand_B = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

team_A = 11
team_B = 11

for i in range(len(red_card)):
    if red_card[i] != ' ':
        card += red_card[i]
    else:
        card += ','
card_list = card.split(',')

for j in card_list:
    if team_A >= 7 and team_B >= 7:
        if j in comand_A:
            comand_A.remove(j)
            team_A -= 1
        elif j in comand_B:
            comand_B.remove(j)
            team_B -= 1
    else:
        break
if team_A >= 7 and team_B >= 7:
    print(f"Team A - {team_A}; Team B - {team_B}")
elif team_A < 7 or team_B < 7:
    print(f"Team A - {team_A}; Team B - {team_B}")
    print('Game was terminated')
