import sys
from collections import deque

def bfs(node):
    queue = deque()
    queue.append(node)
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if check[n] == 0:
                check[n] = check[node] + 1
                queue.append(n)

n = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]

s, e = map(int, sys.stdin.readline().split())

for _ in range(int(sys.stdin.readline())):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

check = [0] * (n + 1)

bfs(s)

print(check[e] if check[e] > 0 else -1)
