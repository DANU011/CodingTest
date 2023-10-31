n, t = map(int, input().split())

check = t * (t + 1) // 2

if n < check:
    print(-1)
elif (n - check) % t == 0:
    print(t - 1)
else:
    print(t)
