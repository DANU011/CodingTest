# 1. 범위를 반씩 좁혀가는 탐색
# 순차 탐색 - 처음부터 탐색
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1
print('먼저 원소 개수를 입력하고 한 칸 띄고 찾을 문자열을 입력하기')
input_data = input().split()
n = int(input_data[0])
target = input_data[1]
print('앞의 원소 개수만큼 문자열을 입력하기(구분은 띄어쓰기 한 칸)')
array = input().split()
print(sequential_search(n, target, array))

# 이진 탐색 - 반으로 쪼개면서 탐색
## 재귀 함수 이용
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))
result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않음')
else:
    print(result+1)

## 반복문 구현
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))
result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않음')
else:
    print(result+1)