s = int(input())

for i in range(s) :
  word = list(input().split())
  for j in word :
    print(j[::-1], end=' ')
