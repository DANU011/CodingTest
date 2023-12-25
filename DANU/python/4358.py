import sys

input_function = sys.stdin.readline

word_count = dict()
total_count = 0

while True:
    word = input_function().rstrip()
    if not word:
        break
    word_count[word] = word_count.get(word, 0) + 1
    total_count += 1

for key, value in sorted(word_count.items()):
    ratio = round(value / total_count * 100, 4)
    print('%s %.4f' % (key, ratio))
