c = []
for _ in range(8):
    c.append(list(map(str, list(input()))))

n = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            if c[i][j] == 'F':
                n += 1
print(n)