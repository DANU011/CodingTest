n = int(input())
f = [list(input()) for _ in range(n)]

c = [[0] * n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if f[i][j] == 'Y' or (f[i][k] == 'Y' and f[k][j] == 'Y'):
                c[i][j] = 1

ans = 0
for row in c:
    ans = max(ans, sum(row))
print(ans)
