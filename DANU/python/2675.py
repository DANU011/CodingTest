t = int(input())

for _ in range(t):
    r, s = map(str, input().split())
    r = int(r)
    s_list = list(s)
    
    for char in s_list:
        print(char * r, end='')
    
    print('')
