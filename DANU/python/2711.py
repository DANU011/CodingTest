for _ in range(int(input())) :
    i, s = input().split()
    i = int(i)
    s = list(s)
    s.pop(i - 1)
    print(''.join(s))
