import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
cnt = 0

arr = [[-1] * n for _ in range(n)]  
arr[r1][c1] = 0  
queue = deque([(r1, c1)])

directions = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

while queue:  
    r, c = queue.popleft()

    for rr, cc in directions:
        x, y = r + rr, c + cc
        if 0 <= x < n and 0 <= y < n and arr[x][y] == -1:
            arr[x][y] = arr[r][c] + 1
            queue.append((x, y))

print(arr[r2][c2])
