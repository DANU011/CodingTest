state = [1, 0, 0]
sequence = input()

for move in sequence :
    if move == 'A' :
        state[0], state[1] = state[1], state[0]
    elif move == 'B' :
        state[1], state[2] = state[2], state[1]
    else :
        state[0], state[2] = state[2], state[0]

print(state.index(1) + 1)
