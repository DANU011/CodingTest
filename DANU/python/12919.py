import sys

source_str = list(input())
target_str = list(input())

def dfs(target) :
    if target == source_str :
        print(1)
        sys.exit()

    if not target :
        return 0

    if target[-1] == 'A' :
        dfs(target[:-1])

    if target[0] == 'B' :
        dfs(target[1:][::-1])

dfs(target_str)
print(0)
