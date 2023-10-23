import sys
 
n = int(sys.stdin.readline())
 
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))
 
li.sort(reverse=True)
 
result = 0
for i in range(n):
    ans = li[i] - i
    if ans < 0:
        break
    result += li[i] - i
 
print(result)
