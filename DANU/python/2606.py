#  컴퓨터의 정보를 제시할 때 언제가 1번부터 등장한다는 언급이 없음 -> 무방향 그래프
#  a와 b가 연결되었다는 정보를 저장한다면 반드시 graph[a]와 graph[b]에 동시에 연결 정보를 저장해야 함.

# DFS stack

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


# stack
def dfs(x):
    stack = [x]
    vist[x] = True
    count = 0
    while stack:
        node = stack.pop()
        for next_node in graph[node]:
            if not vist[next_node]:
                vist[next_node] = True
                stack.append(next_node)
                count += 1
    return count

vist = [False for _ in range(c+1)]
print(dfs(1))
