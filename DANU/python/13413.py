import sys

read = sys.stdin.readline

t = int(read().rstrip())

ans = []
res = 0
arr = []

for _ in range(t):
    n = int(read().rstrip())
    start = list(read().rstrip())
    goal = list(read().rstrip())

    for i in range(n):
        if start[i] != goal[i]:
            arr.append(start[i])

    if arr.count('B') >= arr.count('W'):
        res = arr.count('B')
    else:
        res = arr.count('W')
    ans.append(res)
    arr = []

for answer in ans:
    print(answer)
