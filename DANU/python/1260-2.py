from collections import deque

def bfs(V):
    q = deque([V])  # pop메서드의 시간복잡도가 낮은 덱 내장 메서드를 이용한다
    vist2[V] = True  # V 값을 방문처리
    while q:  # q가 빌때까지 돈다.
        V = q.popleft()  # 큐 첫번째 값 꺼냄
        print(V, end=" ")
        for i in range(1, N + 1):
            if not vist2[i] and graph[V][i]:  # i값 방문하지 않음 && V와 연결
                q.append(i)  # i 값 추가
                vist2[i] = True  # i 값 방문처리


def dfs(V):
    vist1[V] = True  # V값 방문처리
    print(V, end=" ")
    for i in range(1, N + 1):
        if not vist1[i] and graph[V][i]:  # # i값 방문하지 않음 && V와 연결
            dfs(i)  # i 값으로 dfs를 돈다 (더 깊이 탐색)

N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

vist1 = [False] * (N + 1)  # dfs 방문
vist2 = [False] * (N + 1)  # bfs 방문

dfs(V)
print()
bfs(V) 
