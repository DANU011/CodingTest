import sys

def check_eyfa(n, m, input):
    A, B = "", ""

    for _ in range(n):
        for i in input().rstrip():
            A += i * 2

    for _ in range(n):
        B += input().rstrip()

    return 'Eyfa' if A == B else 'Not Eyfa'

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    result = check_eyfa(n, m, input)
    print(result)

if __name__ == '__main__':
    main()
