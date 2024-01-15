import sys

num_lines = int(sys.stdin.readline())

numeric_chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

result = []

for _ in range(num_lines) :
    line_chars = list(map(str, sys.stdin.readline().strip('\n')))
    temp = []
    number_str = ''

    for char in line_chars :
        if char in numeric_chars :
            number_str += char
        else:
            if number_str:
                temp.append(int(number_str))
                number_str = ''

    if number_str :
        temp.append(int(number_str))

    result += temp

result.sort()
for number in result :
    print(number)
