import sys
from queue import PriorityQueue

def read_input():
    n = int(sys.stdin.readline())
    edges = []
    for _ in range(n):
        line = sys.stdin.readline().strip()
        row = []
        for char in line:
            if 'a' <= char <= 'z':
                row.append(ord(char) - ord('a') + 1)
            elif 'A' <= char <= 'Z':
                row.append(ord(char) - ord('A') + 27)
            else:
                row.append(int(char))
        edges.append(row)
    return n, edges

def create_priority_queue(n, edges):
    total_cost = 0
    heap = PriorityQueue()
    for i in range(n):
        for j in range(n):
            cost = edges[i][j]
            total_cost += cost
            if cost != 0 and i != j:
                heap.put((cost, i, j))
    return total_cost, heap

def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a != root_b:
        if root_a < root_b:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b

def kruskal(n, heap):
    parent = list(range(n))
    count = 0
    used_cost = 0
    while not heap.empty():
        if count >= n - 1:
            break
        weight, a, b = heap.get()
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            used_cost += weight
            count += 1
    return count, used_cost

def main():
    n, edges = read_input()
    total_cost, heap = create_priority_queue(n, edges)
    count, used_cost = kruskal(n, heap)
    if count == n - 1:
        print(total_cost - used_cost)
    else:
        print(-1)

if __name__ == "__main__":
    main()
