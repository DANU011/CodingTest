s = input()

suffix = []
for i in range(len(s)) :
    suffix.append(s[i:])
for j in sorted(suffix) :
    print(j)
