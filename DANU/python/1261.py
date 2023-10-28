from collections import deque

n, m = map(int, input().split())
graph = []

for _ in range(m):
    graph.append(list(map(int, input())))

dist = [[-1] * n for _ in range(m)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    dist[0][0] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if dist[nx][ny] == -1:
              
                if graph[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y]
                    queue.appendleft([nx, ny])
                else:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append([nx, ny])

bfs(0, 0)
print(dist[m - 1][n - 1])
