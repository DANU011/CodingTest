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

# 점의 위치 구하기 - 논리 연산자(다른 언어와 혼동하면 안됨)
def solution(dot):
    if (dot[0]>0 and dot[1]>0):
        return 1
    elif (dot[0]<0 and dot[1]>0):
        return 2
    elif (dot[0]<0 and dot[1]<0):
        return 3
    else:
        return 4

# 배열 자르기 - slicing 사용
def solution(numbers, num1, num2):
    answer = numbers[num1 : num2+1]
    return answer