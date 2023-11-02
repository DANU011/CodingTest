from collections import deque

n, m = map(int, input().split())

in_cnt = dict(zip([i for i in range(1, n + 1)], [0 for _ in range(n)]))
in_edges = dict(zip([i for i in range(1, n + 1)], [[] for _ in range(n)]))
out_edges = dict(zip([i for i in range(1, n + 1)], [[] for _ in range(n)]))

for i in range(m):
    a, b = map(int, input().split())
    in_cnt[b] += 1
    in_edges[b].append(a)
    out_edges[a].append(b)

queue = deque()
for node in in_cnt:
    if in_cnt[node] == 0:
        queue.append(node)

ans = []
while queue:
    a = queue.popleft()
    ans.append(a)

    for k in out_edges[a]:
        in_cnt[k] -= 1
        if in_cnt[k] == 0:
            queue.append(k)

print(*ans)
