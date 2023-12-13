n, m = input().split()
min_value = 50

for i in range(len(m) - len(n) + 1) :
    cnt = 0
    for j in range(len(n)) :
        if n[j] != m[i + j] :
            cnt += 1
    min_value = min(min_value, cnt)

print(min_value)
