import heapq

n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]  
dy = [0, 1, 0, -1]  
distances = [[1e10] * m for _ in range(n)]
time_taken = 0

def bfs():
    global time_taken
    queue = []
    heapq.heappush(queue, (cheese[0][0], 0, 0))
    distances[0][0] = cheese[0][0]
    
    while queue:
        cost, r, c = heapq.heappop(queue)
        time_taken = cost
        if cost > distances[r][c]:
            continue
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if cost + cheese[nr][nc] < distances[nr][nc]:
                distances[nr][nc] = cost + cheese[nr][nc]
                heapq.heappush(queue, (distances[nr][nc], nr, nc))

bfs()

print(time_taken)

for i in range(n):
    for j in range(m):
        if not cheese[i][j]:
            distances[i][j] = 0

remaining_cheese = 0
if time_taken != 0:
    for row in distances:
        remaining_cheese += row.count(time_taken)

print(remaining_cheese)
