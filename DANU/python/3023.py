import sys

def read_input():
    R, C = map(int, sys.stdin.readline().split())
    grid = [sys.stdin.readline().strip() for _ in range(R)]
    A, B = map(int, sys.stdin.readline().split())
    return R, C, grid, A, B

def create_expanded_grid(R, C, grid):
    b = [[0 for _ in range(2*C)] for _ in range(2*R)]
    for i in range(R):
        for j in range(C):
            b[i][j] = grid[i][j]
    for i in range(R):
        for j in range(C, 2*C):
            b[i][j] = b[i][2*C-j-1]
    for i in range(R, 2*R):
        for j in range(2*C):
            b[i][j] = b[2*R-i-1][j]
    return b

def toggle_cell(b, A, B):
    if b[A-1][B-1] == '#':
        b[A-1][B-1] = '.'
    else:
        b[A-1][B-1] = '#'

def print_grid(b):
    for row in b:
        print(''.join(row))

def main():
    R, C, grid, A, B = read_input()
    b = create_expanded_grid(R, C, grid)
    toggle_cell(b, A, B)
    print_grid(b)

if __name__ == "__main__":
    main()
