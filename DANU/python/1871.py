for _ in range(int(input())) :
    first_part, second_part = input().split('-')
    number = int(second_part)
    total = 0
    for i in range(3) :
        total += (ord(first_part[i]) - 65) * 26**(2 - i)
    print('nice' if abs(total - number) <= 100 else 'not nice')
