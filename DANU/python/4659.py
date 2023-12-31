import sys

vowels = ['a', 'e', 'i', 'o', 'u']

while True:
    user_input = list(map(str, sys.stdin.readline().strip()))
    is_valid = False

    if ''.join(user_input) == 'end':
        break

    for char in user_input:
        if char in vowels:
            is_valid = True
            break

    if not is_valid:
        print('<{0}> is not acceptable.'.format(''.join(user_input)))
        continue

    consecutive_vowels = 0
    consecutive_consonants = 0
    previous_char = ''

    for current_char in user_input:
        if current_char in vowels:
            consecutive_vowels += 1
            consecutive_consonants = 0
        else:
            consecutive_vowels = 0
            consecutive_consonants += 1

        if previous_char == current_char:
            if previous_char != 'e' and previous_char != 'o':
                is_valid = False
                break
        else:
            previous_char = current_char

        if consecutive_vowels == 3 or consecutive_consonants == 3:
            is_valid = False
            break

    if is_valid:
        print('<{0}> is acceptable.'.format(''.join(user_input)))
    else:
        print('<{0}> is not acceptable.'.format(''.join(user_input)))
