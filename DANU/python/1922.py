from sys import stdin

def find(a, parent):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a], parent)
    return parent[a]

def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    if b < a:
        parent[a] = b
    else:
        parent[b] = a

n = int(input())
m = int(input())
edges = []

parent = [i for i in range(n + 1)]
ans = 0

for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort(key=lambda x: x[0])

for dis, a, b in edges:
    if find(a, parent) != find(b, parent):
        union(a, b, parent)
        ans += dis

print(ans)