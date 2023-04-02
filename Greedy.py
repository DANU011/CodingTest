# 1. 거스름돈
n = 1760
count = 0
coin_type = [500, 100, 50, 10]
for coin in coin_type:
    count += n//coin
    n %= coin
print(count)

# 2. 큰 수의 법칙
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n-1]
second = data[n-2]
count = (m//(k+1))*k
count += m%(k+1)
result = 0
result += (count)*first
result += (m-count)*second
print(result)

# 3. 숫자 카드 게임
n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
print(result)

# 4. 1이 될 때까지
# 내 답안
n, k = map(int, input().split())
result = 0
while n!=1:
    if n % k == 0:
        n //= k
        result += 1
    else:
        n -= 1
        result += 1
print(result)
# 책 풀이
n, k = map(int, input().split())
result = 0
while True:
    target = (n//k)*k
    result += (n-target)
    n = target
    if n<k:
        break
    result += 1
    n //= k
result += (n-1)
print(result)