n = int(input())
dasom = int(input())
votes = []
count = 0

for _ in range(n - 1):
    votes.append(int(input()))

votes.sort(reverse=True)

if n == 1:
    print(0)
else:
    while votes[0] >= dasom:
        dasom += 1
        votes[0] -= 1
        count += 1
        votes.sort(reverse=True)

    print(count)