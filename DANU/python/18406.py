n = int(input())
score = list(str(n))
half = len(score) // 2

scores = list(map(int, score))
if sum(scores[:half]) == sum(scores[half:]):
    print('LUCKY')
else:
    print('READY')
