from collections import Counter

s = input().lower()
cnt = Counter(s)
max_cnt = max(cnt.values())

max_chr = [char for char, count in cnt.items() if count == max_cnt]

if len(max_chr) == 1:
    print(max_chr[0].upper())
else:
    print('?')
