import sys

r, c = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(r)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    q = set([(x, y, board[x][y])])
    local_ans = 1
    while q:
        x, y, ans = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ((0 <= nx < r) and (0 <= ny < c)) and (board[nx][ny] not in ans):
                q.add((nx, ny, ans + board[nx][ny]))
                local_ans = max(local_ans, len(ans) + 1)
    return local_ans

result = bfs(0, 0)
print(result)

# set O(1), deque는 O(N)