import sys
import heapq

input = sys.stdin.readline

INF = sys.maxsize
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dp = [INF] * (V + 1)
dp[K] = 0
heap = []
heapq.heappush(heap, (0, K))

while heap:
    dist, node = heapq.heappop(heap)

    if dist > dp[node]:
        continue

    for next_node, weight in graph[node]:
        next_dist = dist + weight
        if next_dist < dp[next_node]:
            dp[next_node] = next_dist
            heapq.heappush(heap, (next_dist, next_node))

for i in range(1, V + 1):
    if dp[i] == INF:
        print("INF")
    else:
        print(dp[i])