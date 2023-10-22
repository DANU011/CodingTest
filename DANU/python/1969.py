n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(input()))

ans = ''
hamming_distance_sum = 0
for i in range(m):
    a, c, g, t = 0, 0, 0, 0
    for j in range(n):
        if arr[j][i] == 'T':
            t += 1
        elif arr[j][i] == 'A':
            a += 1
        elif arr[j][i] == 'G':
            g += 1
        elif arr[j][i] == 'C':
            c += 1
    if max(a, c, g, t) == a:
        ans += 'A'
        hamming_distance_sum += c + g + t
    elif max(a, c, g, t) == c:
        ans += 'C'
        hamming_distance_sum += a + g + t
    elif max(a, c, g, t) == g:
        ans += 'G'
        hamming_distance_sum += a + c + t
    elif max(a, c, g, t) == t:
        ans += 'T'
        hamming_distance_sum += c + g + a

print(ans)
print(hamming_distance_sum) 