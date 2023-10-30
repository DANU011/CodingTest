t = int(input())

for _ in range(t):
    n = int(input())
    stock = list(map(int, input().split()))
    stock.reverse()
    max_val = stock[0]
    ans = 0

    for i in range(1, n):
        if max_val < stock[i]:
            max_val = stock[i]
            continue
        ans += max_val - stock[i]

    print(ans)
