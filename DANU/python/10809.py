s = list(input())
lowercase = 'abcdefghijklmnopqrstuvwxyz'

for char in lowercase:
    if char in s:
        print(s.index(char), end=' ')
    else:
        print(-1, end=' ')
