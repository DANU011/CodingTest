n = int(input())
m = int(input())
s = input()
answer, index, ioi_count = 0, 0, 0

while index < (m - 1) :
    if s[index:index+3] == 'IOI' :
        index += 2
        ioi_count += 1
        if ioi_count == n :
            answer += 1
            ioi_count -= 1
    else:
        index += 1
        ioi_count = 0

print(answer)
