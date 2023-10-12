import sys
from collections import deque

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    q = deque()
    temp = []
    q.append((a, b))
    temp.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                diff = abs(graph[nx][ny] - graph[x][y])
                if l <= diff <= r:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    temp.append((nx, ny))
    return temp

ans = 0
while True:
    visited = [[0] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)
                if len(country) > 1:
                    flag = True
                    number = sum([graph[x][y] for x, y in country]) // len(country)
                    for x, y in country:
                        graph[x][y] = number
    if not flag:
        break
    ans += 1

print(ans)
