# 위에서 아래로
n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))
result = sorted(array, reverse=True)
for i in result:
    print(i, end=' ')

# 성적이 낮은 순서로 학생 출력하기
n = int(input())
array = []
for _ in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))
array = sorted(array, key=lambda x: x[1])
for i in array:
    print(i[0], end=' ')

# 두 배열의 원소 교체
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a1 = sorted(a)
b1 = sorted(b, reverse=True)
for i in range(k):
    if a[i] < b[i]:
        a1[i], b1[i] = b1[i], a1[i]
    else:
        break
print(sum(a1))