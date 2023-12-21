import sys

input = sys.stdin.readline

n, m = map(int, input().split(' '))
words = dict()

for i in range(n) :
    word = input().rstrip()
    if len(word) >= m :
        if word not in words :
            words[word] = 1
        else :
            words[word] += 1

memory = sorted(words, key = lambda x: (-words[x], -len(x), x))

for i in memory :
    print(i)
