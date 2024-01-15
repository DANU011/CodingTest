import sys
input_func = sys.stdin.readline

n = int(input_func())
files = [input_func().rstrip() for _ in range(n)]

for i in range(n - 1) :
    for j in range(i, n) :
        if files[i][::-1] == files[j] :
            print(len(files[i]), files[i][len(files[i]) // 2])
            exit()
