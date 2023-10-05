n = int(input())
arr = []

def sol():
    answer = 0
    arr.sort(reverse=True)
    for i in range(n):
        arr[i] = arr[i] * (i + 1)
 
    return max(arr)
 
for _ in range(n):
    arr.append(int(input()))
 
print(sol())
