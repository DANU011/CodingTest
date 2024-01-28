user_input = input()
length = len(user_input)

x, y = 0, 0

for i in range(1, int(length / 2) + 1):
    for j in range(i, length + 1):
        if i * j == length:
            x, y = i, j

for i in range(x):
    for j in range(y):
        print(user_input[i + j * x], end='')
