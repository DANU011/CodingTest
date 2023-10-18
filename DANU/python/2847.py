n = int(input())
scores = []
count = 0

for _ in range(n):
    scores.append(int(input()))

for i in range(n - 1, 0, -1):
    if scores[i] <= scores[i - 1]:
        count += (scores[i - 1] - scores[i] + 1)
        scores[i - 1] = scores[i] - 1

print(count)