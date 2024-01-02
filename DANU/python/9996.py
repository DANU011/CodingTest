import re

num_patterns = int(input())
pattern_str = input()
regex_pattern = re.compile('.*'.join(pattern_str.split('*')))

for _ in range(num_patterns) :
    input_string = input()

    if regex_pattern.fullmatch(input_string) :
        print('DA')
    else :
        print('NE')
