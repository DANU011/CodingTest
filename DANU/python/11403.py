import sys
sys.setrecursionlimit(10**4)

input = sys.stdin.readline

def dfs(x):
    for i in range(n):
        if visit[i]==0 and arr[x][i]==1:
            visit[i]=1
            dfs(i)

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

visit = [0]*n

for i in range(n):
    dfs(i)
    for j in range(n):
        if visit[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
    visit = [0]*n