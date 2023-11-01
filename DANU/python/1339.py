import sys

n = int(sys.stdin.readline())
s = [sys.stdin.readline().strip() for _ in range(n)]
letters = {}

for word in s:
    x = len(word) - 1
    for letter in word:
        if letter in letters:
            letters[letter] += 10 ** x
        else:
            letters[letter] = 10 ** x
        x -= 1

letters_sorted = sorted(letters.values(), reverse=True)
ans = 0
num = 9

for value in letters_sorted:
    ans += value * num
    num -= 1

print(ans)
