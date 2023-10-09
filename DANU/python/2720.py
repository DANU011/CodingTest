changes = [25, 10, 5, 1]
t = int(input())

for _ in range(t):
    c = int(input())
    ans = []

    for i in changes:
        ans.append(c // i)
        c = c % i

    print(*ans)
