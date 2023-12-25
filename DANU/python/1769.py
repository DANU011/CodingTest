number = input()
count = 0

while len(number) > 1 :
    count += 1
    total_sum = 0
    for digit in number :
        total_sum += int(digit)
    number = str(total_sum)

print(count)

if int(number) % 3 == 0 :
    print('YES')
else :
    print('NO')
