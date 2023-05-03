# 1. 거스름돈
n = 1760
count = 0
coin_type = [500, 100, 50, 10]

for coin in coin_type:
    count += n // coin
    n %= coin

print(count)

# 2. 큰 수의 법칙
# 1) m의 크기가 커지면 시간 초과됨
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[n - 1]
second = data[n - 2]
result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

# 2) 효율적인 답안
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[n - 1]
second = data[n - 2]

count = (m // (k + 1)) * k
count += m % (k + 1)
result = 0

result += count * first
result += (m - count) * second

print(result)

# 3. 숫자 카드 게임
# 1) min() 함수 이용
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

# 2) 2중 반복문 이용
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)

# 4. 1이 될 때까지
# 내 답안
n, k = map(int, input().split())

result = 0

while n != 1:
    if n % k == 0:
        n //= k
        result += 1
    else:
        n -= 1
        result += 1

print(result)

# 책 풀이 1 - 단순하게 풀기
n, k = map(int, input().split())

result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)

# 책 풀이 2 - 효율적인 답안
n, k = map(int, input().split())

result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)
