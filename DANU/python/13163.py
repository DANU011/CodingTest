def change_nickname(t):
    for _ in range(t):
        nickname = input().split()
        nickname[0] = 'god'
        print(*nickname, sep='')

if __name__ == "__main__":
    t = int(input())
    change_nickname(t)
