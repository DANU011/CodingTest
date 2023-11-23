n = int(input())
first_word = list(input())
first_word_len = len(first_word)
             
for _ in range(n - 1):
    other_words = list(input())
    for i in range(first_word_len):
        if first_word[i] != other_words[i]:
            first_word[i] = '?'

print(''.join(first_word))
