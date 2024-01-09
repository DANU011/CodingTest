import sys

input_data = sys.stdin.readline
n = int(input_data())
food_info = []

for i in range(n) :
    data = list(input_data().split())
    food_info.append(data[1:])

food_info.sort()

dash = '--'
answer = []

for i in range(n) :
    if i == 0 :
        for j in range(len(food_info[i])) :
            answer.append(dash * j + food_info[i][j])
    else :
        idx = 0
        for j in range(len(food_info[i])) :
            if food_info[i - 1][j] != food_info[i][j] or len(food_info[i - 1]) <= j :
                break
            else :
                idx = j + 1
        for j in range(idx, len(food_info[i])) :
            answer.append(dash * j + food_info[i][j])

for ans in answer :
    print(ans)
