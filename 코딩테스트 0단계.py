# 짝수의 합 - 'int' object is not iterable
def solution(n):
    sum = 0
    for i in range(1, n+1):
        if i%2==0:
            sum += i
    return sum

# 배열의 평균값 - 함수는 따로 없음
def solution(numbers):
    return sum(numbers)/len(numbers)