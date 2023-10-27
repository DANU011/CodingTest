import sys 
input = sys.stdin.readline

n = int(input())
stud = list(map(int, input().split()))
sorted_stud = sorted(stud)
ans = []

for _ in range(n):
    ans.append(sorted_stud.pop(0) + sorted_stud.pop(-1))

print(min(ans))
