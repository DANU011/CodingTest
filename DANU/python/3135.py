x, y = map(int, input().split())
ans = abs(x - y)
num_queries = int(input())

for _ in range(num_queries):
    n = int(input())
    if ans > abs(n - y):
        ans = abs(n - y) + 1

print(ans)
