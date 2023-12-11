s = list(input())

for i in range(len(s)):
    if 90 >= ord(s[i]) >= 65:
        if (ord(s[i])+13) > 90:
            s[i] = chr(ord(s[i])-13)
        else:
            s[i] = chr(ord(s[i])+13)
    elif 122 >= ord(s[i]) >= 97:
        if (ord(s[i])+13) > 122:
            s[i] = chr(ord(s[i])-13)
        else:
            s[i] = chr(ord(s[i])+13)
print(*s, sep='')
