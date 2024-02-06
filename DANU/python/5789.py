test_cases = int(input())

for _ in range(test_cases):
    number = list(input())
    mid_index = len(number) // 2 - 1
    if number[mid_index] == number[-mid_index - 1]:
        print('Do-it')
    else:
        print('Do-it-Not')
