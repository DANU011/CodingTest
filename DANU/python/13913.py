from collections import deque

n, k = map(int, input().split())
visited = [False] * (200001)

def bfs(start):
    queue = deque()
    queue.append([start, 0, [start]])
    visited[start] = True

    if start > k:
        return start - k, [int(x) for x in range(start, k - 1, -1)]

    while queue:
        current, count, path = queue.popleft()

        if current == k:
            return count, path

        next_positions = [current - 1, current + 1, current * 2]
        for next_pos in next_positions:
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                new_path = path + [next_pos]
                queue.append([next_pos, count + 1, new_path])

answer_count, answer_path = bfs(n)

print(answer_count)
for step in answer_path:
    print(step, end=' ')
