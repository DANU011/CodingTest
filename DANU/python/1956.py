import sys, math

input = sys.stdin.readline

V, E = map(int, input().split())
dist = [[math.inf] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    dist[a][b] = c

for i in range(1, V + 1):
    dist[i][i] = 0

for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = math.inf
for i in range(1, V + 1):
    for j in range(1, V + 1):
        if i == j:
            continue
        if dist[i][j] != math.inf and dist[j][i] != math.inf:
            ans = min(ans, dist[i][j] + dist[j][i])

if ans == math.inf:
    print(-1)
else:
    print(ans)