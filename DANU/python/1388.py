import sys

n, m = map(int, sys.stdin.readline().split())

place = []
for _ in range(n):
    place.append(list(sys.stdin.readline()))

def dfs(row, col):
    if place[row][col] == "-":
        place[row][col] = 1
        for a in [1, -1]:
            Y = col + a
            if (0 < Y < m) and place[row][Y] == "-":
                dfs(row, Y)
    if place[row][col] == "|":
        place[row][col] = 1
        for b in [1, -1]:
            X = row + b
            if (0 < X < n) and place[X][col] == "|":
                dfs(X, col)

count = 0
for i in range(n):
    for j in range(m):
        if place[i][j] == '-' or place[i][j] == "|":
            dfs(i, j)
            count += 1

print(count)
