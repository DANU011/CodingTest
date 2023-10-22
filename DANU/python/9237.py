n = int(input())

data = list(map(int, input().split()))
data.sort(reverse=True)

ans = []
for i in range(n):
    ans.append(data[i]+ 1 + i)

print(max(ans) + 1)
