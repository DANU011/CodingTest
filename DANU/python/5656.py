import sys
cnt=1
while True:
    s=sys.stdin.readline()
    if s[2] =="E" : exit()
    print ("Case %d: "%cnt,end='')
    print( str (eval(s))[0].lower()+str (eval(s))[1:])
    cnt+=1
