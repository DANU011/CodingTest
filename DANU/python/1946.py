import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    rank = [list(map(int, input().split())) for _ in range(n)]
    rank.sort(key=lambda x: x[0])
    top = rank[0][1]
    result = 1

    for i in range(1, n):
        if rank[i][1] < top:
            top = rank[i][1]
            result += 1

    print(result)
