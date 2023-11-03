n = int(input())
line = input()

cnt = line.count('LL') - 1
if cnt < 0: cnt = 0

print(n - cnt)
