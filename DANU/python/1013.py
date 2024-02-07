import re
import sys
input_function = sys.stdin.readline

test_cases = int(input_function())
pattern = re.compile('(100+1+|01)+')

for _ in range(test_cases):
    match_result = pattern.fullmatch(input_function().rstrip())
    if match_result is None:
        print('NO')
    else:
        print('YES')
