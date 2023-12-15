import sys

test_cases = int(sys.stdin.readline().rstrip())

for _ in range(test_cases) :
    num_phone_numbers = int(sys.stdin.readline().rstrip())

    phone_numbers = []
    for _ in range(num_phone_numbers) :
        phone_numbers.append(sys.stdin.readline().rstrip())
    
    phone_numbers.sort()

    is_consistent = True
    for i in range(len(phone_numbers) - 1) :
        if phone_numbers[i] == phone_numbers[i + 1][:len(phone_numbers[i])] :
            is_consistent = False
            break
    
    if is_consistent :
        print('YES')
    else :
        print('NO')
