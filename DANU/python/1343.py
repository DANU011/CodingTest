board = input()

while 'XXXX' in board:
    board = board.replace('XXXX', 'AAAA', 1)

while 'XX' in board:
    board = board.replace('XX', 'BB', 1)

if 'X' in board:
    print(-1)
else:
    print(board)
