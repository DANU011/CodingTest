def is_valid(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return 'NO'
            stack.pop()
    
    return 'YES' if not stack else 'NO'

t = int(input())

for _ in range(t):
    ps = input()
    print(is_valid(ps))
