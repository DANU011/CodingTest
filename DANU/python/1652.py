import sys
input_func = sys.stdin.readline

size = int(input_func())
board = [list(input_func().rstrip()) for _ in range(size)]

counts = [0, 0]
for i in range(size):
    row_length, col_length = 0, 0
    for j in range(size):
        if board[i][j] == '.':
            row_length += 1
        else:
            row_length = 0
        if row_length == 2:
            counts[0] += 1

        if board[j][i] == '.':
            col_length += 1
        else:
            col_length = 0
        if col_length == 2:
            counts[1] += 1

print(*counts)
