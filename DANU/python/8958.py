n = int(input())


for _ in range(0, n):
    cnt, c = 0, 1
    s = list(input())
    
    for j in s:
        if j == 'O' :
            cnt += c
            c += 1
        else:
            c = 1
    print(cnt)
