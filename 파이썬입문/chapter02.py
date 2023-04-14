import math

# 실습문제
# 1.
n = input('성명 입력>> ')
k = int(input('국어 성적>> '))
e = int(input('영어 성적>> '))
m = int(input('수학 성적>> '))
sum_score = k+e+m
avg_score = sum_score/3
print('성명 :', n)
print('국어 :', k)
print('영어 :', e)
print('수학 :', m)
print('총점 :', sum_score)
print('평균 :', avg_score)

# 2.
r = int(input('원의 반지름 입력>> '))
l = math.pi*2*r
a = math.pi*(r**2)
print('반지름이 {}인 원 둘레의 길이는 {}이고 넓이는 {}입니다.'.format(r, l, a))

# 3.
n1 = int(input('첫번째 정수 입력>> '))
n2 = int(input('두번째 정수 입력>> '))
n3 = int(input('세번째 정수 입력>> '))
max_num = max(n1, max(n2, n3))
min_num = min(n1, min(n2, n3))
print('가장 큰 수는 %d입니다.' % max_num)
print('가장 작은 수는 %d입니다.' % min_num)

# 4.
area1 = int(input('평 입력>> '))
area2 = area1 * 3.3058
print('{}평은 {}제곱미터입니다.'.format(area1, area2))