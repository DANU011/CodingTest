from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))


# 너비 우선 탐색
def bfs(x, y):
    # 방향 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # deque 생성
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 현위치에서 네방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 이탈 방지 조건
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 벽 진행 불가
            if graph[nx][ny] == 0:
                continue

            # 벽 X 진행
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 마지막 값에서 카운트 값 뽑음
    return graph[N - 1][M - 1]


print(bfs(0, 0))