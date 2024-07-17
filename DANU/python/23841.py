def mirror_image(N, M, lst):
    for i in range(N):
        for j in range(M):
            if lst[i][j] != '.':
                lst[i][M - j - 1] = lst[i][j]
    return lst


def main():
    N, M = map(int, input().split(' '))
    lst = [list(input()) for _ in range(N)]

    mirrored_lst = mirror_image(N, M, lst)

    for row in mirrored_lst:
        print(''.join(row))


if __name__ == "__main__":
    main()
