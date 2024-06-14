import sys


def count_direction_changes(N, maps):
    cnt = 1
    for i in range(1, N):
        if maps[i] == 'E' and maps[i - 1] == 'W':
            cnt += 1
    return cnt


def main():
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    maps = data[1]

    result = count_direction_changes(N, maps)
    print(result)


if __name__ == "__main__":
    main()
