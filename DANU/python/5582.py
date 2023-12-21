import sys

str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()

dp = [[0] * len(str2) for _ in range(len(str1))]

for i in range(len(str1)) :
    for j in range(len(str2)) :
        if str1[i] == str2[j] :
            if i - 1 >= 0 and j - 1 >= 0 and dp[i - 1][j - 1] > 0 :
                dp[i][j] = dp[i - 1][j - 1] + 1
            else :
                dp[i][j] = 1

answer = 0
for i in range(len(str1)) :
    for j in range(len(str2)) :
        answer = max(answer, dp[i][j])

print(answer)
