import sys


def can_transform(S, T):
    S = list(S)
    T = list(T)

    while len(S) != len(T):
        if T[-1] == 'A':
            T.pop()
        elif T[-1] == 'B':
            T.pop()
            T.reverse()

    return 1 if S == T else 0


def main():
    input = sys.stdin.read
    data = input().split()
    S = data[0].strip()
    T = data[1].strip()

    result = can_transform(S, T)
    print(result)


if __name__ == "__main__":
    main()
