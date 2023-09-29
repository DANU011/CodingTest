from collections import deque

h, w = map(int, input().split())
field = list()
direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]

for _ in range(h):
    field.append(list(input()))

def bfs(rx, ry):
    visited = [[0] * w for _ in range(h)]
    q = deque([[rx, ry]])
    visited[ry][rx] = 1
    max_cnt = 0
    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx, ny = dx + x, dy + y
            if 0 <= nx < w and 0 <= ny < h and field[ny][nx] == 'L' and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                if max_cnt < visited[ny][nx]: max_cnt = visited[ny][nx]
                q.append([nx, ny])
    return max_cnt - 1

answer = 0
for i in range(h):
    for j in range(w):
        if field[i][j] == 'L':
            tmp = bfs(j, i)
            if tmp > answer:
                answer = tmp
print(answer)