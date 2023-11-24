score = input()

alphabets = ['F', 'D', 'C', 'B', 'A']
res = float(alphabets.index(score[0]))

if res > 0:
    if score[1] == '+':
        res += 0.3
    elif score[1] == '-':
        res -= 0.3

print(res)