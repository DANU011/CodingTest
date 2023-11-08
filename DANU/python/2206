import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    row = sys.stdin.readline()
    for j in range(m):
        graph[i][j] = int(row[j])

visited = [[[False, False] for _ in range(m)] for _ in range(n)]

def bfs():
    queue = deque([(0, 0, 0, 0)])  # (x, y, breakable, dist)
    visited[0][0][0] = True
    visited[0][0][1] = True

    while queue:
        x, y, breakable, dist = queue.popleft()

        if x == n - 1 and y == m - 1:
            print(dist + 1)
            return

        adjacent_cells = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for point in adjacent_cells:
            nx, ny = point

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][breakable]:
                if graph[nx][ny] == 0:
                    visited[nx][ny][breakable] = True
                    queue.append((nx, ny, breakable, dist + 1))
                elif breakable == 0:
                    visited[nx][ny][breakable] = True
                    queue.append((nx, ny, 1, dist + 1))

    print(-1)

bfs()
