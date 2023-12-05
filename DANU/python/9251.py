import sys

read_line = sys.stdin.readline

word1 = read_line().strip()
word2 = read_line().strip()

length1 = len(word1)
length2 = len(word2)

cache = [0] * length2

for i in range(length1):
    current_max_count = 0

    for j in range(length2):
        if current_max_count < cache[j]:
            current_max_count = cache[j]
        elif word1[i] == word2[j]:
            cache[j] = current_max_count + 1

result = max(cache)
print(result)
