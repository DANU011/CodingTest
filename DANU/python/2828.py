import sys

n, m = map(int, sys.stdin.readline().split())
j = int(sys.stdin.readline())
now = 1
apples = []
ans = 0

for _ in range(j):
    apples.append(int(sys.stdin.readline()))

for apple in apples:
    if now <= apple and now + (m - 1) >= apple:
        pass
    elif now > apple:
        ans += abs(apple - now)
        now = apple
    else:
        ans += apple - (m - 1) - now
        now = apple - (m - 1)

print(ans)
