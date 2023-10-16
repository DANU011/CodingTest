import sys

read = lambda: sys.stdin.readline().rstrip()
n, l = map(int, read().split())
tree_heights = list(map(int, read().split()))

tree_heights.sort()

position = 0
for height in tree_heights:
    if height > l:
        break
    if height <= l:
        l += 1

print(l)
