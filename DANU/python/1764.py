n, m = map(int,input().split())
a = set()
b = set()

res = []
for _ in range(n):
    a.add(input())
    
for _ in range(m):
    b.add(input())

for i in a :
    if i in b :
        res.append(i)
        
res.sort()

print(len(res))

for i in res :
    print(i)
