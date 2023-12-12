num_players = int(input())
initials_list = []
final_result = []

for _ in range(num_players):
    player_name = input()
    initials_list.append(player_name[0])

unique_initials = set(initials_list)

for initial in unique_initials:
    if initials_list.count(initial) >= 5:
        final_result.append(initial)

if len(final_result) > 0:
    print(''.join(sorted(final_result)))
else:
    print('PREDAJA')
