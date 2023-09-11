# DFS 재귀, BFS queue
from collections import deque


def dfs(start):
    vist[start] = True
    print(start, end=" ")

    for i in graph[start]:
        if not vist[i]:
            dfs(i)


def bfs(start):
    queue = deque([start])
    vist[start] = True
    while queue:

        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not vist[i]:
                vist[i] = True
                queue.append(i)


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬
for i in graph:
    i.sort()

# dfs
vist = [False] * (N + 1)
dfs(V)
print()

# bfs
vist = [False] * (N + 1)
bfs(V)