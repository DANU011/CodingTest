import sys

read_line = sys.stdin.readline
seq_1 = read_line().rstrip()
seq_2 = read_line().rstrip()
seq_3 = read_line().rstrip()

length_1 = len(seq_1)
length_2 = len(seq_2)
length_3 = len(seq_3)

dp_array = [[[0] * (length_3 + 1) for _ in range(length_2 + 1)] for _ in range(length_1 + 1)]

for i in range(1, length_1 + 1) :
    for j in range(1, length_2 + 1) :
        for k in range(1, length_3 + 1) :
            if seq_1[i - 1] == seq_2[j - 1] and seq_2[j - 1] == seq_3[k - 1] :
                dp_array[i][j][k] = dp_array[i - 1][j - 1][k - 1] + 1
            else :
                dp_array[i][j][k] = max(dp_array[i][j][k - 1], dp_array[i][j - 1][k], dp_array[i - 1][j][k])

max_length = -1

for i in range(length_1 + 1) :
    for j in range(length_2 + 1) :
        max_length = max(max(dp_array[i][j]), max_length)

print(max_length)
