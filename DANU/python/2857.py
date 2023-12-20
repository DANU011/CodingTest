result = []
for i in range(1, 6) :
    s = input()
    if 'FBI' in s :
        result.append(i)
if len(result) == 0 :
    print('HE GOT AWAY!')
else :
    print(*result)
