import sys

input_string, letter_count = sys.stdin.read(), [0 for i in range(26)]

for char in input_string:
    if char.islower():
        letter_count[ord(char) - 97] += 1

for index in range(26):
    if letter_count[index] == max(letter_count):
        print(chr(index + 97), end='')
