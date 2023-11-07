n, c = map(int, input().split())

grid = []
for _ in range(c):
    grid.append(input())

def bfs(y, x, wb):
    global count
    count += 1
    check[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < c and 0 <= nx < n:
            if grid[ny][nx] == wb and check[ny][nx] == 0:
                bfs(ny, nx, wb)

check = [[0] * n for _ in range(c)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
w, b = 0, 0
for i in range(c):
    for j in range(n):
        if check[i][j] == 0:
            count = 0
            bfs(i, j, grid[i][j])
            if grid[i][j] == 'W':
                w += count * count
            else:
                b += count * count

print(w, b)
