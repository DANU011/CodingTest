# BFS queue
from collections import deque

# 컴퓨터의 수
c = int(input())
# 네트워크 쌍 개수
e = int(input())
graph = [[] for _ in range(c+1)]
for _ in range(e):
    a, b = map(int, input().split())
    # 1부터 등장한다는 보장 없음
    graph[a].append(b)
    graph[b].append(a)


# queue
def bfs(x):
    deq = deque([x])
    count = 0
    vist[x] = True
    while deq:
        node = deq.popleft()
        for next_node in graph[node]:
            if not vist[next_node]:
                vist[next_node] = True
                deq.append(next_node)
                count += 1

    return count

vist = [False for _ in range(c+1)]
print(bfs(1))
