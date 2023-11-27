vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    cnt = 0
    sentence = input()
    if sentence == '#' :
        break
    for s in sentence :
        if s in vowel :
            cnt += 1
    print(cnt)
