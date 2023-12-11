import sys

x = list(sys.stdin.readline().strip())
m = list(sys.stdin.readline().strip())

m_length = len(m)
stack = []
for i in x :
    stack.append(i)
    if stack[len(stack) - m_length:len(stack)] == m :
        for _ in range(m_length) :
            stack.pop()
if stack :
    print(*stack, sep='')
else :
    print('FRULA')
