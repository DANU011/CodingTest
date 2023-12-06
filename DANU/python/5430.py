from collections import deque

test_cases = int(input())

for _ in range(test_cases) :
    operations = input()
    array_length = int(input())
    input_array = input()[1:-1]
    numbers = input_array.split(',')

    queue = deque(numbers)

    reverse_count = 0
    error_flag = False

    if array_length == 0:
        queue = []

    for operation in operations :
        if operation == 'R' :
            reverse_count += 1
        else :
            if len(queue) == 0 :
                print('error')
                error_flag = True
                break
            elif reverse_count % 2 == 1 :
                queue.pop()
            else :
                queue.popleft()

    if not error_flag :
        if reverse_count % 2 == 1 :
            queue.reverse()
        print('[' + ','.join(queue) + ']') 
