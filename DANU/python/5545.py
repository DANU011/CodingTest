n = int(input())
a, b = map(int, input().split())
c = int(input())
lst, ans = [], 0

for _ in range(n):
    lst.append(int(input()))

lst = sorted(lst, reverse=True)

for i in range(len(lst) + 1):
    price = a + b * i
    ans = max(ans, (c + sum(lst[:i])) // price)

print(ans)
