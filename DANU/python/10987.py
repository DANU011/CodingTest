word = list(map(str, input()))

vowels = ['a', 'e', 'i', 'o', 'u']
cnt = 0

for letter in word:
    if letter in vowels:
        cnt += 1
        
print(cnt)
