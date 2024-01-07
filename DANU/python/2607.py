import sys
import copy

n = int(sys.stdin.readline().rstrip())
list1 = list(sys.stdin.readline().rstrip())
answer = 0

for i in range(n-1) :
    list2 = list(sys.stdin.readline().rstrip())
    c_list1 = copy.deepcopy(list1)
    c_list2 = copy.deepcopy(list2)

    for j in list1 :
        if j in list2 :
            list2.remove(j)
            c_list1.remove(j)

    if len(list2) <= 1 and len(c_list1) <= 1 :
        answer += 1

print(answer)
