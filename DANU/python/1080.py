from sys import stdin

def toggle(r, c):
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            a[i][j] ^= 1

n, m = map(int, stdin.readline().split())
a = [list(map(int, stdin.readline().rstrip())) for _ in range(n)]
b = [list(map(int, stdin.readline().rstrip())) for _ in range(n)]

count = 0
for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            toggle(i, j)
            count += 1

print(count if a == b else -1)
