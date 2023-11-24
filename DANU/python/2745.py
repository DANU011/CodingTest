n, b = input().split()
ary = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n = n[::-1]
res = 0

for i, digit in enumerate(n):
    res += (int(b) ** i) * (ary.index(digit))
print(res)
