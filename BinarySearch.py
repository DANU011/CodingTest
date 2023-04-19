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

# 이진 탐색 - 반으로 쪼개면서 탐색 - 반드시 정렬되어 있어야 함
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

## 반복문 이용
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

# 부품 찾기
## 이진 탐색 이용
import sys
n = int(sys.stdin.readline().rstrip())
array1 = list(map(int, sys.stdin.readline().split()))
array1.sort()
m = int(sys.stdin.readline().rstrip())
array2 = list(map(int, sys.stdin.readline().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return "yes"
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return "no"

for i in array2:
    print(binary_search(array1, i, 0, n - 1), end=' ')

## 계수 정렬 이용
n = int(input())
array1 = [0]*1000001
for i in input().split():
    array1[int(i)] = 1
m = int(input())
array2 = list(map(int, input().split()))
for i in array2:
    if array1[i] == 1:
        print("yes", end=' ')
    else:
        print("no", end=' ')

## 집합 자료형 이용
n = int(input())
array = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))
for i in x:
    if i in array:
        print("yes", end=' ')
    else:
        print("no", end=' ')

# 떡볶이 떡 만들기 - 파라메트릭 서치 문제 -> 이진 탐색 이용(반복문)
n, m = map(int, input().split())
array = list(map(int, input().split()))
start = 0
end = max(array)
result = 0
while start <= end:
    total = 0
    mid = (start + end)//2
    for x in array:
        if x > mid:
            total += x-mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)