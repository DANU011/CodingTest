import math

input_word = input()

word_total = 0
for char in input_word :
    if char.islower() :
        word_total += ord(char) - 96
    else:
        word_total += ord(char) - 38

is_prime = True
for i in range(2, int(math.sqrt(word_total)) + 1) :
    if word_total % i == 0 :
        is_prime = False

if is_prime :
    print('It is a prime word.')
else :
    print('It is not a prime word.')
